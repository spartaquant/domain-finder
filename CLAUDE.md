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
