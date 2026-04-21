# Goal
Replace the near-empty `CLAUDE.md` (currently just `TEST`) with a comprehensive project instruction file so future AI assistants have accurate context on the Domain Finder app's stack, layout, conventions, and constraints.

---

# Approach
This is a **documentation-only task** — no application code changes. I'll write a single file at the repo root describing what's actually in the codebase today, then commit it.

The content will be derived from what's already on disk: `app.py` (FastAPI + aiohttp + WebSocket), `requirements.txt` (3 deps), `static/index.html` (single-file vanilla frontend with dark/light CSS theme variables), `README.md`, `RUN.md` (Docker preview config), and `.gitignore`. I will **not invent** commands, tools, test frameworks, or conventions that are not visible in the repo — e.g. there is no test suite, no linter config, no Makefile, so those sections will either be omitted or explicitly called out as absent.

> **Constraint:** CLAUDE.md must reflect reality. If a convention isn't enforced by code or config, it shouldn't appear as a rule.

Key facts that must appear:
- **Single-module backend** (`app.py`) — resist premature splitting
- **Single-file frontend** (`static/index.html`) — all CSS/JS inline, theme via `data-theme` + CSS variables
- **Cache file** (`domain_status_cache.json`) is gitignored and written at runtime
- **Port 4706** per README, but preview Dockerfile uses 8000 — worth noting
- **WebSocket protocol** (`/ws/check`) has a specific message shape (`init`, `batch`, `done`, `error`) worth documenting for future edits

---

# Architecture

```diagram
                   ┌─────────────────────────┐
                   │  static/index.html      │
                   │  (vanilla HTML/CSS/JS,  │
                   │   dark + light themes)  │
                   └───────────┬─────────────┘
                               │ WebSocket /ws/check
                               ▼
                   ┌─────────────────────────┐
                   │  app.py  (FastAPI)      │
                   │  • generate_candidates  │
                   │  • fetch_domain_status  │
                   │  • ws_check (streaming) │
                   └───────┬─────────┬───────┘
                           │         │
                 aiohttp   │         │  read/write
                           ▼         ▼
              ┌────────────────┐   ┌───────────────────────────┐
              │ Verisign RDAP  │   │ domain_status_cache.json  │
              │ (external)     │   │ (gitignored, runtime)     │
              └────────────────┘   └───────────────────────────┘
```

---

# Tasks

### Phase 1: Draft CLAUDE.md content
- Overwrite `/workspace/CLAUDE.md` (currently `TEST`) with sections:
  - Project name + one-paragraph description
  - Tech stack (Python 3.10+, FastAPI, uvicorn, aiohttp; vanilla frontend; no DB)
  - Repository layout (`app.py`, `static/index.html`, `requirements.txt`, `RUN.md`, `README.md`, runtime `domain_status_cache.json`)
  - Development setup (install + run commands copied from README, plus Docker preview note from `RUN.md`)
  - Code conventions (single-module backend; single-file frontend; CSS variables + `data-theme` for theming; async/aiohttp semaphore-bounded concurrency; WebSocket message schema)
  - Constraints & architectural decisions (no test suite, no linter config, cache is runtime/gitignored, RDAP is `.com`-only via Verisign endpoint, port mismatch between README `4706` and preview `8000`)
- **Complexity:** Low

### Phase 2: Commit to repo
- Stage `CLAUDE.md` only (leave `GANTT_CONTEXT.md` untracked — it appears to be an ephemeral planning context file)
- Commit with a short conventional message (e.g. `docs: add comprehensive CLAUDE.md for AI assistants`)
- Do **not** push — leave that to the user
- **Complexity:** Low

---

# Risks / Open questions
- **Risk:** Overstating conventions. There is no linter, formatter, or test runner configured — the plan must not invent rules that aren't enforced in the repo.
- **Risk:** Port inconsistency. `README.md` says `4706`, `RUN.md` uses `8000`. I will document both and note the discrepancy rather than silently pick one.
- **Open question:** Should CLAUDE.md forbid splitting `app.py` into multiple modules? The current code is intentionally single-file; I'll note this as an observed pattern ("resist premature splitting") without making it a hard rule.
- **Open question:** Should `GANTT_CONTEXT.md` (currently untracked) be added to `.gitignore`? Out of scope for this task — flagging only.

---

# Non-goals
- Not modifying `app.py`, `static/index.html`, or any application code.
- Not adding tests, linters, formatters, or CI config.
- Not changing `README.md`, `RUN.md`, or `.gitignore`.
- Not pushing the commit to a remote.
