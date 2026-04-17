# Goal
Make the **Reset** button in the Keywords card restore the full prefilled keyword list that was shown at page load, and make the reset feel complete (no leftover typed input, highlight, or filter state).

---

# Approach
The wiring already exists: the Reset button at `static/index.html:319` calls `resetKeywords()` (line 506-509), which does `keywords = [...DEFAULT_KEYWORDS]` + `renderKeywords()`. If the user is seeing it not behave as expected, it's almost certainly because **leftover UI state** (the `kwInput` text, match highlights, and the keyword-filter multiselect) makes the reset look incomplete — e.g. dimmed tags stay dimmed if there's still text in the input.

The fix is small and local to `static/index.html`: harden `resetKeywords()` so it clears the input, clears its highlight state, refreshes the keyword-multiselect options (so any stale selection doesn't linger), and re-renders the results table. **No backend change.**

> Keep the change surgical — don't touch `startCheck`, cache logic, or the RDAP flow. The prefilled list source of truth is the `DEFAULT_KEYWORDS` constant in `static/index.html:430-443`, which mirrors `app.py:25-40`.

---

# Architecture

```diagram
[Reset button]
      |
      v
  resetKeywords()  ──►  keywords = [...DEFAULT_KEYWORDS]
      |                         │
      |                         ├─► renderKeywords()          (rebuild tag pills)
      |                         ├─► clear kwInput value       (NEW)
      |                         ├─► highlightMatchingKeywords (NEW — clears kw-match/kw-dim)
      |                         ├─► selectedKeywords.clear()  (NEW — drop stale filter tags)
      |                         ├─► populateKwDropdown()      (NEW — refresh multiselect)
      |                         └─► renderTable()             (NEW — results reflect new kw set)
```

---

# Tasks

### Phase 1: Harden `resetKeywords()` in `static/index.html`
- In `resetKeywords()` (line 506-509), after assigning `keywords = [...DEFAULT_KEYWORDS]`:
  - Clear the text input: `document.getElementById("kwInput").value = "";`
  - Call `renderKeywords()` (already there).
  - Call `highlightMatchingKeywords()` so any `kw-match` / `kw-dim` classes are cleared.
  - Clear `selectedKeywords` (the position-filter multiselect) so reset also drops stale filter chips.
  - Call `populateKwDropdown()` so the multiselect options reflect the new keyword list.
  - Call `renderTable()` so the already-displayed results re-filter against the restored keyword set.
- **Complexity:** Low

### Phase 2: Manual verification in browser
- Run the app (`uvicorn app:app --reload`) and load the page.
- Remove several default keyword tags (click the × on each). Type partial text in the input. Click **Reset**.
- Verify: all prefilled defaults are back, the input is empty, no tags are dimmed, and any selected filter-keywords are cleared.
- **Complexity:** Low

---

# Risks / Open questions
- **Risk:** If results have been loaded, clearing `selectedKeywords` will visibly shift the results table (more rows shown). This is intended — a true "reset" should not leave stale filters — but worth confirming.
- **Open question:** Should Reset also close the results card / clear the `results` array, or only touch the keyword inputs? The plan above intentionally leaves `results` alone (prefilled keywords ≠ search results). Flag if you want results cleared too.

---

# Non-goals
- Not changing `DEFAULT_KEYWORDS` content or its backend mirror in `app.py`.
- Not adding a confirm-dialog before reset.
- Not clearing completed result rows, progress counters, or the WebSocket connection state.
