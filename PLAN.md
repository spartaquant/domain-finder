# Goal

Improve the visual design and UX of the Domain Finder web app without changing backend logic.

# Approach

The app is a single-file frontend (`static/index.html`, ~930 lines) with inline CSS and JS. The current design is functional but feels flat and cluttered — especially with 100+ keyword tags, dense filter rows, and a plain data table. The plan focuses on **visual polish, layout improvements, and better information hierarchy** while keeping the single-file vanilla HTML/CSS/JS architecture.

Key design decisions:
- **Keep it single-file** — no build tools, no frameworks. All changes stay in `static/index.html`.
- **Improve hierarchy** — use spacing, typography weight, and subtle backgrounds to separate sections visually.
- **Reduce clutter** — collapse the keyword section by default (show count + expand toggle), consolidate filter controls into a single toolbar row.
- **Modernize the table** — add row striping, sticky header, better status badges, and hover effects.
- **Add micro-interactions** — smooth transitions on progress, subtle animations on new results appearing, better button feedback.
- **Improve the progress experience** — animated gradient bar, pulsing stats, skeleton placeholder while loading.
- **Add a favicon** — inline SVG data URI favicon matching the logo.

# Tasks

- [ ] **1. Add inline SVG favicon** — Add a `<link rel="icon">` with a data URI matching the purple gradient logo square.

- [ ] **2. Improve header** — Add a subtle bottom border and a tagline with result stats summary. Add a subtle background gradient at the top of the page for depth.

- [ ] **3. Collapsible keywords section** — Show keyword count and a compact summary by default (first ~20 tags visible, rest hidden). Add "Show all N keywords" / "Collapse" toggle button. This prevents the huge wall of 100+ tags from dominating the page on load.

- [ ] **4. Improve keyword tag styling** — Slightly larger tags with better padding, smoother hover transitions, and a subtle scale effect on hover. Add a count badge next to the section title.

- [ ] **5. Consolidate filter toolbar** — Combine the status filter chips, domain search input, and keyword position filter into a single well-designed toolbar row with logical grouping. Use a compact inline layout instead of stacking three separate rows.

- [ ] **6. Improve progress bar** — Animated gradient (moving shimmer effect while active), slightly taller bar (8px), rounded pill shape. Add a percentage label. Pulse/glow effect on the available count as it increments.

- [ ] **7. Modernize the results table** — Add alternating row backgrounds (subtle zebra striping), sticky `thead`, better cell padding, and slightly larger domain names. Make the score bar wider and more prominent. Improve status badges with slightly larger pills and bolder colors.

- [ ] **8. Add result card stats bar** — Above the table, add a horizontal stats bar with colored indicators: total domains, available (green), registered (red), unknown (yellow) — using larger numbers and small spark-like indicators instead of plain text counters.

- [ ] **9. Better empty/loading states** — Add a subtle illustration or icon for the empty state. While checking is in progress and table is empty, show a skeleton placeholder (3-4 pulsing rows) instead of nothing.

- [ ] **10. Improve action buttons** — Larger click targets, better visual distinction between Copy and Register. Add a subtle tooltip-style hover label. Make the register button more prominent with a filled style.

- [ ] **11. Add smooth transitions for new results** — When new batch rows appear in the table, add a subtle fade-in CSS animation so results don't just pop in abruptly.

- [ ] **12. Responsive polish** — Improve the mobile layout: stack filter toolbar vertically, make table horizontally scrollable with a visible scroll hint, ensure keyword section collapses well on small screens.

- [ ] **13. Add subtle page background texture** — Add a very faint dot grid or noise pattern to the background for visual depth (CSS only, no external images — use a tiny inline SVG or CSS gradient pattern).

- [ ] **14. Polish scrollbar styling** — Add custom dark-themed scrollbar styles for WebKit browsers (thin, dark track, accent-colored thumb) to match the dark theme.

# Risks / Open questions

- **Performance with large tables**: The current approach renders all rows via `innerHTML`. With 5000+ domains this can cause jank. The plan doesn't add virtual scrolling (that would be a larger change), but the fade-in animation should be lightweight (CSS-only, no JS animation loops).
- **Font loading**: The app loads Inter and JetBrains Mono from Google Fonts. No change planned, but if the user wants to self-host fonts or reduce external dependencies, that's a separate task.
- **Single-file size**: After these changes the file will be ~1200-1400 lines. Still manageable for a single-file app but approaching the limit where splitting into separate CSS/JS files might be worth considering in the future.
- **Browser compatibility**: Custom scrollbar styles and some CSS features (`:has()`, `backdrop-filter`) are WebKit/Blink only. The plan uses progressive enhancement — the app will still work in Firefox, just without custom scrollbars.
