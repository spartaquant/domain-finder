import asyncio
import itertools
import json
import re
from pathlib import Path
from typing import Dict, List

import aiohttp
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# ── Config ──────────────────────────────────────────────────────────────
RDAP_URL = "https://rdap.verisign.com/com/v1/domain/{}"
CACHE_FILE = "domain_status_cache.json"
MIN_LEN = 4
MAX_LEN = 14
REQUEST_TIMEOUT = 8
CONCURRENCY = 15

DEFAULT_KEYWORDS = [
    "base", "feed", "trading", "view", "alpha", "market", "prime", "signal",
    "trace", "radar", "mosaic", "intel", "forge", "flow", "iq", "alphawatch",
    "tower", "guru", "nova", "sage", "zen", "sparta", "quant", "live", "news",
    "watch", "echo", "shadow", "ghost", "lab", "x", "ray", "constellation",
    "star", "qube", "lead", "track", "idea", "observer", "horizon", "feat",
    "tech", "ai", "digest", "insight", "pulse", "core", "nexus", "matrix",
    "vantage", "apex", "asphalt", "catalyst", "cortex", "echelon", "elevate",
    "fusion", "genesis", "helix", "infinity", "keystone", "lighthouse",
    "momentum", "odyssey", "revolution", "spectrum", "titan", "velocity",
    "zenith", "vortex", "warp", "xenon", "sig", "al", "alyx", "yx", "zeta",
    "omega", "delta", "sigma", "kappa", "lambda", "theta", "phi", "chi",
    "way", "edge", "vista", "ster", "ify", "ium", "ex", "exy", "nix", "onyx",
    "vibe", "vibes", "vibez", "xy", "all", "road", "water", "bridge", "sky",
    "cloud", "in", "meta", "abc", "hyper", "scale",
]

# ── Cache helpers ───────────────────────────────────────────────────────
def load_cache() -> Dict[str, str]:
    path = Path(CACHE_FILE)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_cache(cache: Dict[str, str]) -> None:
    tmp = f"{CACHE_FILE}.tmp"
    Path(tmp).write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")
    Path(tmp).replace(CACHE_FILE)


# ── Domain logic (reused from original script) ─────────────────────────
def normalize_keywords(words: List[str]) -> List[str]:
    seen: set[str] = set()
    clean: list[str] = []
    for w in words:
        w = re.sub(r"[^a-z0-9]", "", w.strip().lower())
        if w and w not in seen:
            seen.add(w)
            clean.append(w)
    return clean


def is_reasonable_name(name: str) -> bool:
    if not (MIN_LEN <= len(name) <= MAX_LEN):
        return False
    if not re.fullmatch(r"[a-z0-9]+", name):
        return False
    if re.search(r"(.)\1{2,}", name):
        return False
    return True


def score_name(name: str, w1: str, w2: str) -> float:
    score = 100.0 - len(name) * 2
    preferred = {
        "alpha": 4, "quant": 4, "forge": 3, "signal": 3, "radar": 3,
        "nova": 2, "zen": 2, "sparta": 4, "qube": 3, "lab": 2,
        "tech": 2, "ai": 2, "iq": 2,
    }
    score += preferred.get(w1, 0) + preferred.get(w2, 0)
    generic = {"news", "live", "view", "watch", "idea", "lead", "track"}
    if w1 in generic:
        score -= 3
    if w2 in generic:
        score -= 3
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{5,}", name):
        score -= 8
    return round(score, 2)


def generate_candidates(words: List[str]) -> List[dict]:
    words = normalize_keywords(words)
    candidates = []
    for w1, w2 in itertools.combinations(words, 2):
        for name in (f"{w1}{w2}", f"{w2}{w1}"):
            if is_reasonable_name(name):
                candidates.append({
                    "word1": w1,
                    "word2": w2,
                    "name": name,
                    "domain": f"{name}.com",
                    "score": score_name(name, w1, w2),
                })
    candidates.sort(key=lambda c: c["score"], reverse=True)
    return candidates


async def fetch_domain_status(session: aiohttp.ClientSession, domain: str) -> str:
    url = RDAP_URL.format(domain)
    try:
        async with session.get(
            url, timeout=REQUEST_TIMEOUT,
            headers={"Accept": "application/rdap+json"},
        ) as resp:
            if resp.status == 200:
                return "registered"
            if resp.status == 404:
                return "likely_available"
            return f"unknown"
    except asyncio.TimeoutError:
        return "unknown"
    except aiohttp.ClientError:
        return "unknown"


# ── WebSocket endpoint for live progress ────────────────────────────────
@app.websocket("/ws/check")
async def ws_check(ws: WebSocket):
    await ws.accept()
    try:
        data = await ws.receive_json()
        keywords: List[str] = data.get("keywords", DEFAULT_KEYWORDS)
        candidates = generate_candidates(keywords)

        await ws.send_json({
            "type": "init",
            "total": len(candidates),
            "keywords_used": len(normalize_keywords(keywords)),
        })

        cache = load_cache()
        semaphore = asyncio.Semaphore(CONCURRENCY)
        checked = 0
        results: list[dict] = []
        lock = asyncio.Lock()

        timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT + 2)
        connector = aiohttp.TCPConnector(limit_per_host=CONCURRENCY)

        async def check_and_report(item: dict):
            nonlocal checked
            domain = item["domain"]

            # Check cache first
            cached = cache.get(domain)
            if cached and cached not in ("unknown", "unknown_timeout"):
                item["status"] = cached
                item["source"] = "cache"
            else:
                async with semaphore:
                    item["status"] = await fetch_domain_status(session, domain)
                    item["source"] = "live"
                    async with lock:
                        cache[domain] = item["status"]

            async with lock:
                checked += 1
                item["rank"] = checked
                results.append(item)

            await ws.send_json({"type": "result", "item": item, "checked": checked})

        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            tasks = [check_and_report(c) for c in candidates]
            await asyncio.gather(*tasks)

        save_cache(cache)
        await ws.send_json({"type": "done", "total_checked": checked})

    except WebSocketDisconnect:
        pass
    except Exception as e:
        try:
            await ws.send_json({"type": "error", "message": str(e)})
        except Exception:
            pass


# ── Serve frontend ──────────────────────────────────────────────────────
@app.get("/")
async def index():
    return FileResponse("static/index.html")


app.mount("/static", StaticFiles(directory="static"), name="static")
