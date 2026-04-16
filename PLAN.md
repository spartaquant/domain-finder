# Goal
Modernize the Domain Finder UI with better visual polish, animations, layout improvements, and UX refinements — all within the single `static/index.html` file.

# Approach
The app is a single HTML file with inline CSS and JS. The current dark theme is solid but feels flat and utilitarian. We'll add depth, motion, and better information hierarchy while keeping the same tech stack (no build tools, no frameworks). Every change stays in `static/index.html`.

Key design directions:
- **Depth & layering**: Subtle glassmorphism on cards, soft glow effects, layered shadows
- **Motion**: CSS transitions for results streaming in, smooth filter changes, animated progress
- **Information hierarchy**: Stat cards with visual weight, collapsible keywords section, count badges on filter chips
- **Polish**: Gradient text in header, shimmer on progress bar, toast notifications instead of `alert()`, SVG favicon, better empty states
- **Table UX**: Pagination for large result sets, smoother row rendering

# Tasks

- [ ] **1. Background & atmosphere** — Add a subtle radial gradient or noise texture to `body`/`.app` for visual depth. Add a faint grid or dot pattern overlay.

- [ ] **2. Header upgrade** — Make the logo larger with a glow/pulse animation. Add gradient text to "Domain Finder". Add a subtle tagline or domain count beneath.

- [ ] **3. Glassmorphism cards** — Add `backdrop-filter: blur()` and semi-transparent backgrounds to `.card`. Add softer, layered box-shadows. Add a subtle top-border gradient accent line on cards.

- [ ] **4. Collapsible keywords section** — Add a toggle button to collapse/expand the keywords area. Show keyword count in the header. Default to collapsed after first run to save screen space. Animate the expand/collapse with `max-height` transition.

- [ ] **5. Stat cards row** — Replace the plain `.result-counters` text with styled mini-cards (icon + number + label). Use color-coded left borders or backgrounds. Make them update with a counting animation when values change.

- [ ] **6. Filter chips with counts** — Add badge counts to each filter chip showing how many results match (e.g., "Likely Available (42)"). Update counts reactively as results stream in.

- [ ] **7. Progress bar polish** — Add a shimmer/sweep animation on the progress bar fill. Add ETA or rate display (e.g., "~120/sec"). Make the bar glow subtly while active.

- [ ] **8. Table improvements** — Add staggered fade-in for new rows. Improve hover state with a left accent border. Add alternating row subtle tinting. Add pagination (50 rows per page) with page controls below the table to prevent DOM bloat with thousands of rows.

- [ ] **9. Toast notification system** — Replace `alert()` calls with a lightweight toast system. Toast appears in bottom-right, auto-dismisses after 4s. Use for errors and "copied" feedback. Style with status colors (green/red/yellow).

- [ ] **10. Empty & loading states** — Add a simple SVG illustration or icon to the empty state. Add a skeleton shimmer effect while results are loading (before first batch arrives).

- [ ] **11. SVG favicon** — Add an inline SVG favicon via `<link rel="icon">` data URI using the existing gradient purple/indigo logo style.

- [ ] **12. Responsive polish** — Improve mobile layout: stack stat cards vertically, make table horizontally scrollable with a scroll hint shadow, ensure filter chips wrap gracefully, make keyword section work well on narrow screens.

- [ ] **13. Micro-interactions** — Add hover scale on buttons. Add a subtle bounce on the "Generate" button. Add a ripple or press effect on filter chips. Add smooth color transitions on status badge changes.

- [ ] **14. Scroll-to-top / sticky header for results** — Make the results table header sticky so column names stay visible while scrolling. Add a floating "scroll to top" button when scrolled down.

# Risks / Open questions
- **Performance with many rows**: Pagination (task 8) is important — the current approach renders all rows into the DOM which can lag with 5000+ results. Virtual scrolling would be ideal but complex; pagination is simpler and sufficient.
- **backdrop-filter support**: Glassmorphism relies on `backdrop-filter` which works in all modern browsers but may look flat in older ones. We'll add a solid fallback background.
- **Single file size**: All CSS/JS stays inline. The file will grow but should remain under 50KB which is fine for a tool like this.
- **Subjective taste**: "Improve design" is broad — the plan focuses on polish and UX rather than a complete redesign. The dark theme and color palette stay the same.
