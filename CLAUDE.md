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
