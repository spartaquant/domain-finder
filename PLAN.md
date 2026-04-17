# Goal
Modernize the Domain Finder UI with a more polished, cohesive visual design — better typography, hierarchy, density, and micro-interactions — without changing functionality.

# Approach
The current UI in `static/index.html` is a single-file dark theme that works, but it feels generic: flat cards, uniform spacing, weak visual hierarchy between the "setup" area (keywords + actions) and the "results" area, and very utilitarian header/filters. The redesign will stay in that single file (no framework churn) but introduce a richer visual system.

Key moves:
- **Two-tone layered dark palette** with subtle gradients and soft ambient glows so the page doesn't look flat. Keep accessibility-grade contrast for text.
- **Stronger hero/header** with a compact brand mark, a tagline, and live stats that animate in once a run completes — giving the top of the page identity and reward.
- **Restructure the top block** into a sticky "control bar" that groups keywords + primary action + progress, so the user always has context during long runs.
- **Table refresh**: zebra rows, sticky header, better status pills (with icons not just dots), score column rendered as a segmented gauge, clearer hover/focus states, row-level quick-copy on hover.
- **Filters redesign**: convert the two filter-chip rows into a unified, segmented-control-style toolbar with an integrated search input and a visible result count.
- **Micro-interactions**: smoother transitions, skeleton loading state before first results arrive, flash animation when new rows stream in, toasts instead of `alert()` for errors, subtle progress-bar shimmer while running.
- **Responsive polish**: collapse table to card list under ~640px, make sticky bar compact on scroll, ensure multiselect dropdown stays in-viewport.
- **Empty/initial states**: the big empty table area on first load gets an illustrated empty state that guides the user to press the start button.

No backend changes. All work is in `static/index.html` (CSS + small JS additions for the new interactions). The existing WebSocket protocol and DOM hooks stay intact so behavior is unchanged.

# Tasks

1. **Design system refresh (CSS variables, typography, base)**
   - Expanded token set: add `--surface3`, `--elev-*` shadows, `--accent-2` (cyan/teal), gradient tokens, softer `--border` at lower opacity.
   - Import a display font (e.g. Space Grotesk or keep Inter but add weight 800 display usage) for the hero headline; keep Inter for body and JetBrains Mono for domains.
   - Add a subtle radial-gradient background behind the app container.

2. **Header / hero rework**
   - Larger, gradient-stroked logo mark; headline + subhead with muted caption.
   - Optional "session stats" strip (keywords count, cached domains, last run duration) shown as small pill metrics — only visible after first run.

3. **Control bar (keywords + actions + progress merged)**
   - Merge the keywords card, action row, and progress bar into one cohesive "command deck" card with clearer sub-sections.
   - When a run is active, card gets a shimmer border or soft glowing accent to signal live state.
   - Make the primary "Generate & Check" button larger / more prominent with a subtle gradient and hover lift.
   - Keywords get a slightly tighter chip style with hover affordance that reveals the × instead of always showing it.

4. **Results toolbar & filters**
   - Replace two stacked filter-chip rows with a single segmented-control bar: status filters on the left, keyword filter + position toggle in the middle, search on the right.
   - Show result counters inline within the toolbar (e.g. "142 likely available · 820 registered · 30 unknown").
   - Sticky toolbar within the results card when the table scrolls.

5. **Table redesign**
   - Sticky table header, zebra rows, tighter row height.
   - Redesigned status badges: add tiny inline icons (check/x/question) instead of only a colored dot, and softer pill shape.
   - Score column: segmented 5-bar gauge (instead of single bar) colored by percentile; numeric score on the right in tabular-nums.
   - Row hover: subtle row-highlight + slide-in quick copy/register buttons (reduce always-visible button clutter).
   - Responsive: under 640px, each row renders as a compact card with domain headline + inline badges + action row.

6. **Feedback & micro-interactions**
   - Replace `alert()` with a toast component (top-right stack, auto-dismiss).
   - Skeleton rows while waiting for first batch after clicking start.
   - New rows fade-in briefly when streamed (CSS keyframe on insert).
   - Copy button: ✓ flash already exists — extend same treatment to the registrar button when `copyOnClick` fires.

7. **Accessibility & keyboard polish**
   - Ensure 4.5:1 contrast on muted text over new surfaces.
   - Visible `:focus-visible` rings on all interactive elements (buttons, chips, multiselect, registrar pills).
   - Keyword chip remove button becomes a proper `<button>` for keyboard access; ditto the sort headers (`role="button"` + aria-sort).
   - Respect `prefers-reduced-motion` by disabling shimmer/fade animations.

8. **QA & cross-browser sweep**
   - Verify in Chrome, Firefox, Safari at desktop and mobile breakpoints.
   - Smoke-test a full run: start → streaming → done → filter → sort → register click → recheck unknowns.
   - Confirm cache, WebSocket, and registrar deep-links all still function (no JS regressions).

# Risks / Open questions
- **Scope vs. restraint** — this is a visual polish task, not a rewrite. If any redesign element conflicts with existing behavior (e.g. multiselect dropdown positioning, WebSocket error handling), prefer minimal changes over broader refactors.
- **Font loading** — adding a display font is a small perf hit; can use `font-display: swap` and preconnect (already done). Acceptable.
- **Sticky toolbar inside a card** — may feel weird on short result lists; consider only enabling sticky when results > N.
- **Alert → toast** — need a tiny toast helper; keep it vanilla JS, no library.
- **Light mode?** — not in scope unless the user requests it; the redesign stays dark-themed.
