# Domain Finder

Domain Finder is a FastAPI web app that generates candidate `.com` domain names by combining pairs of keywords (both orderings, filtered by length and quality heuristics) and checks their availability against the Verisign RDAP API. Results stream back to a single-page vanilla frontend over a WebSocket as they are fetched, with previously-seen domains served instantly from a local JSON cache.

## Tech stack

- **Language**: Python 3.10+
- **Web framework**: FastAPI (>=0.110.0)
- **ASGI server**: uvicorn[standard] (>=0.29.0)
- **HTTP client**: aiohttp (>=3.9.0) — async RDAP lookups
- **Package manager**: `pip` with `requirements.txt` (no `pyproject.toml`, no lockfile)
- **Frontend**: vanilla HTML/CSS/JS in a single file — no build step, no bundler, no framework
- **Database**: none. Runtime state is a single JSON file (`domain_status_cache.json`) written by the backend
- **Tests**: no test framework is configured; there is no test suite
- **Lint/format**: no linter, formatter, or type checker is configured

## Repository layout

- `app.py` — FastAPI backend, kept as a **single module**. Contains config constants, cache helpers, candidate generation, the async RDAP fetcher, the `/ws/check` WebSocket endpoint, and the `/` + `/static` routes that serve the frontend.
- `static/index.html` — the **entire frontend**, roughly 1,000 lines of HTML with inline CSS and JavaScript. Handles keyword editing, connects to the WebSocket, renders streamed results into a filterable/sortable table, and supports a dark/light theme toggle.
- `requirements.txt` — the 3 runtime dependencies (`fastapi`, `uvicorn[standard]`, `aiohttp`).
- `README.md` — user-facing documentation: features, setup, usage, and a brief explanation of how the domain scoring and availability check work.
- `RUN.md` — Docker preview configuration. Uses YAML frontmatter (`port: 8000`) followed by a Dockerfile code block based on `python:3.12-slim`.
- `.gitignore` — ignores `__pycache__/`, `*.pyc`, `.env`, `venv/`, `.venv/`, and the runtime cache files (`domain_status_cache.json`, `domain_status_cache.json.tmp`).
- `domain_status_cache.json` — **runtime-generated** JSON map of `domain -> status`. Written by the backend after live RDAP lookups. **Gitignored** — never commit it.

## Development setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app (command from `README.md`):

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 4706
```

The app then serves at [http://localhost:4706](http://localhost:4706).

**Port discrepancy — read this before changing ports.** `README.md` and the command above use port **4706**, but `RUN.md` (the Docker preview config) declares `port: 8000` in its frontmatter and the embedded Dockerfile also `EXPOSE`s / binds to **8000**. Both are intentional for their respective contexts (local dev vs. preview container); if you edit one, check whether the other needs to match.

There is **no test command, no lint command, no formatter command, and no `Makefile`**. Changes must be verified manually by running the server and exercising the UI.

## WebSocket protocol

The frontend talks to the backend over a single WebSocket endpoint: **`/ws/check`** (defined in `app.py` around lines 136–266). The message flow is:

**Client → server** (one message, immediately after connect):

```json
{
  "keywords": ["alpha", "forge", "..."],
  "recheck_unknown": false
}
```

- `keywords` (`string[]`): list of keywords to combine. If omitted, the server falls back to `DEFAULT_KEYWORDS` in `app.py`.
- `recheck_unknown` (`boolean`): when `true`, any cached entry whose status starts with `unknown` is treated as a cache miss and re-fetched.

**Server → client** messages (all JSON, identified by `type`):

1. `{"type": "init", "total": <int>, "cached": <int>, "to_fetch": <int>, "keywords_used": <int>}` — sent once, summarises the work.
2. `{"type": "batch", "items": [ ...candidate objects... ], "checked": <int>}` — sent one or more times. A single "fast" batch is sent up front for all cache hits; subsequent batches stream in as live RDAP lookups complete (flushed every `BATCH_SIZE = 20` results).
3. `{"type": "done", "total_checked": <int>}` — sent once after all lookups finish.
4. `{"type": "error", "message": "<str>"}` — sent instead of `done` if an unhandled exception occurs server-side.

Each **candidate item** inside a `batch` has the shape:

| Field    | Type                                                | Notes                                                                              |
| -------- | --------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `word1`  | `string`                                            | First keyword of the pair (normalised: lowercased, non-alphanumerics stripped).    |
| `word2`  | `string`                                            | Second keyword of the pair.                                                        |
| `name`   | `string`                                            | Concatenation of the two words in one of the two orderings.                        |
| `domain` | `string`                                            | `"{name}.com"`.                                                                    |
| `score`  | `number`                                            | Heuristic score from `score_name()` — higher is better.                            |
| `rank`   | `integer`                                           | 1-based order in which this item was resolved (cached items first, then live).     |
| `status` | `"registered" \| "likely_available" \| "unknown"`   | From RDAP: 200 → `registered`, 404 → `likely_available`, anything else → `unknown`. |
| `source` | `"cache" \| "live"`                                 | Whether the status came from `domain_status_cache.json` or a live RDAP lookup.     |

The cache is read once at the start of the request, then updated in-memory as live lookups complete; it is flushed to disk every 50 results and once more at the end.

## Code conventions

These are patterns **observed in the current code**, not rules enforced by tooling. Preserve them unless the task explicitly requires otherwise.

- **Single-module backend.** All backend logic lives in `app.py`. Config constants (`RDAP_URL`, `APP_DIR`, `CACHE_FILE`, `MIN_LEN`, `MAX_LEN`, `REQUEST_TIMEOUT`, `CONCURRENCY = 50`, `BATCH_SIZE = 20`, `DEFAULT_KEYWORDS`) sit at the top of the file. Resist splitting into multiple modules or packages unless the task explicitly calls for it.
- **Async I/O with bounded concurrency.** Live RDAP lookups are issued through a shared `aiohttp.ClientSession` and gated by `asyncio.Semaphore(CONCURRENCY)`. A separate `asyncio.Lock` guards shared mutable state (the `cache` dict, the `pending_batch` list, the `checked` counter); a third `send_lock` serialises `ws.send_json` calls. Keep this pattern when adding new async work — don't drop the semaphore or introduce unprotected shared state.
- **Single-file frontend.** `static/index.html` contains the full UI: markup, inline `<style>` CSS, and inline `<script>` JS — no external assets, no build step, no bundler. Resist adding a build pipeline, a framework, or a separate CSS/JS file.
- **Theming via CSS custom properties + `data-theme`.** Colours are declared as CSS variables on `:root` (dark defaults) and overridden under `[data-theme="light"]`. The attribute is set on `<html>` from `localStorage` on page load and toggled by a theme button. New styling should read from these variables rather than hard-coding colours.
- **Keyword normalisation.** `normalize_keywords()` lowercases input, strips non-alphanumerics, and deduplicates while preserving order. `is_reasonable_name()` rejects names outside `[MIN_LEN, MAX_LEN]`, non-alphanumeric names, and names with any character repeated 3+ times in a row. Any new candidate-filtering logic should go through these helpers.
- **Cache write semantics.** `save_cache()` writes the full JSON blob with `indent=2, sort_keys=True` and swallows write errors with a `[WARN]` print. Preserve the sort/indent so diffs stay readable if the file is ever inspected manually.

## Constraints and architectural decisions

- **RDAP is `.com`-only.** The Verisign endpoint (`https://rdap.verisign.com/com/v1/domain/{}`) is hardcoded. Supporting other TLDs would require routing to different RDAP servers — not a drop-in change.
- **Cache is a runtime JSON file.** `domain_status_cache.json` is written in the project directory at runtime, is listed in `.gitignore`, and **must never be committed**. Treat it as disposable state — the app regenerates entries on demand.
- **Port mismatch is known.** `README.md` and the documented `uvicorn` command use port **4706**; `RUN.md`'s Docker preview config uses port **8000**. This is intentional per-context; do not "fix" one without considering the other.
- **No test suite, no CI.** There are no automated tests, no linter, no formatter, and no CI configuration. All changes must be verified manually by running the server (`python -m uvicorn app:app --host 0.0.0.0 --port 4706`) and exercising the UI in a browser — generate domains, stream results, toggle filters, toggle the theme.
- **No database, no auth, no multi-user state.** The app is single-user and single-process. The WebSocket endpoint accepts any connection and runs the full check on demand; cache mutations are not coordinated across processes.
