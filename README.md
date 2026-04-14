# Domain Finder

A web app that generates domain name combinations from keyword pairs and checks their availability via RDAP (Verisign `.com` registry).

## Features

- **Keyword management** - Start with 100+ default keywords, add/remove as needed
- **Smart combinations** - Generates all 2-word pairs in both orders (alphaforge + forgealpha), filters by length and quality
- **Live availability checking** - Real-time progress via WebSocket, checks against Verisign RDAP
- **Result caching** - Previously checked domains are cached locally to avoid redundant lookups
- **Scoring** - Domains are scored based on length, keyword quality, and pronounceability
- **Filterable table** - Filter by status (likely available / registered / unknown), search by name, sort by any column
- **Keyword position filter** - Select a keyword (e.g. "alpha") and filter to show only domains where it appears as prefix (alphaXXX) or suffix (XXXalpha)

## Setup

### Requirements

- Python 3.10+
- pip

### Install

```bash
pip install -r requirements.txt
```

### Run

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 4706
```

Then open [http://localhost:4706](http://localhost:4706) in your browser.

## Usage

1. Review/edit the keyword list (add comma-separated words, click X to remove)
2. Click **Generate & Check Domains** to start
3. Watch results stream in live with the progress bar
4. Use filters to find available domains:
   - **Status filter** - Show only likely available, registered, or unknown
   - **Search** - Type to filter by domain name or keyword
   - **Keyword filter** - Select a specific keyword and choose "Keyword first" or "Keyword last" to see prefix/suffix combinations
   - **Sort** - Click any column header to sort

## How it works

- Generates all unordered 2-keyword combinations
- For each pair, creates both orderings (word1+word2 and word2+word1)
- Filters out names that are too short (<4), too long (>14), or have triple-repeated characters
- Checks `.com` availability via the [Verisign RDAP API](https://rdap.verisign.com)
- Caches results in `domain_status_cache.json` for future runs

## Tech stack

- **Backend**: FastAPI + aiohttp (async RDAP lookups)
- **Frontend**: Vanilla HTML/CSS/JS with a dark theme
- **Protocol**: WebSocket for live streaming results
