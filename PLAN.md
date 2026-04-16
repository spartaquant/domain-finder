# Goal

Comprehensively improve the visual design of the Domain Finder app — better spacing, typography, micro-interactions, table readability, and mobile responsiveness — while keeping the dark theme and vanilla HTML/CSS/JS stack.

# Approach

The app is a single `static/index.html` file (~930 lines) containing all CSS and JS inline. The design is functional but can be significantly polished. We'll make targeted CSS and minor HTML improvements across these areas:

1. **Layout & spacing** — Add a subtle gradient background, increase card elevation with soft box-shadows, improve vertical rhythm between sections, and add a sticky header.
2. **Typography & hierarchy** — Improve the header with a tagline or subtitle treatment, better card title styling, and consistent font sizing.
3. **Keywords section** — Make keyword tags more visually distinct with better hover states, add a count badge, and improve the input row layout.
4. **Progress bar** — Make it taller with a pulsing animation during active checks, add a percentage label.
5. **Table improvements** — Add alternating row shading, sticky header row, better hover states, improved status badges with icons, wider score bars, and better action button styling.
6. **Filter chips** — Add transition animations, count badges on status filters, and a more distinct active state.
7. **Micro-interactions** — Smooth fade-in for new table rows, button press effects, subtle transitions on cards.
8. **Mobile** — Collapse filters into a scrollable row, make the table horizontally scrollable with a fade hint, stack action buttons vertically.
9. **Empty & loading states** — Add an animated illustration/icon for the empty state, a skeleton loader or spinner.
10. **Footer** — Add a minimal footer with app info.

All changes stay within `static/index.html`. No backend changes needed.

# Tasks

- [ ] 1. **Background & global styles** — Replace flat `--bg` with a subtle radial gradient. Add smooth scrolling to `html`. Add a `::selection` style using the accent color.

- [ ] 2. **Header redesign** — Make the header sticky with a backdrop blur and bottom border on scroll. Enlarge the logo with a subtle animation on hover. Add a subtle text gradient to the title.

- [ ] 3. **Card elevation** — Add layered `box-shadow` to `.card` for depth. Add a subtle left-border accent on hover. Increase padding slightly. Add `transition` for hover effects.

- [ ] 4. **Keywords section polish** — Restyle `.kw-tag` with softer rounded corners and a subtle gradient background. Improve the remove button (`×`) with a red background circle on hover. Add a smooth entry animation when new keywords are added. Improve `.kw-input-row` with a joined input+button look.

- [ ] 5. **Button improvements** — Add a subtle gradient to `.btn-primary` instead of flat color. Add active/pressed state (`transform: scale(0.97)`). Add focus-visible ring for accessibility. Improve disabled state.

- [ ] 6. **Progress bar enhancement** — Increase height to 8px. Add an animated shimmer/stripe effect during active checking. Show percentage text next to the bar. Add a glow effect matching the gradient.

- [ ] 7. **Filter chips redesign** — Make active chips more prominent with a filled background + slight shadow. Add a smooth color transition. Add result count badges inside filter chips (update JS to inject counts into chip text).

- [ ] 8. **Search input improvements** — Add a search icon (SVG) inside the input using `background-image` or a `::before` pseudo-element wrapper. Add a clear button when text is present.

- [ ] 9. **Table header sticky + style** — Make `thead` sticky with `position: sticky; top: 0` and a background color. Add a bottom shadow on the header for depth. Improve sort arrow visibility and add hover underline on sortable columns.

- [ ] 10. **Table row improvements** — Add subtle alternating row backgrounds (`tr:nth-child(even)`). Improve hover highlight with a left accent border. Add a fade-in animation for rows as results stream in. Increase row height slightly for breathing room.

- [ ] 11. **Status badges upgrade** — Make badges slightly larger with an icon (checkmark for available, X for registered, ? for unknown) instead of just a dot. Add a subtle pulse animation on "likely available" badges.

- [ ] 12. **Score bar improvements** — Widen the score bar to 70px. Add rounded end caps. Show the numeric score in bold. Color-code the bar fill based on score (green for high, yellow mid, red low) instead of the fixed gradient.

- [ ] 13. **Action buttons polish** — Make action buttons more visually distinct. Add icon-only mode on smaller screens. Improve the "copied" flash with a checkmark icon and green background.

- [ ] 14. **Multiselect dropdown polish** — Add a subtle scale-in animation when opening. Improve option hover states. Add checkmarks next to selected items. Add a max-height scroll shadow (fade) at top/bottom.

- [ ] 15. **Result counters redesign** — Restyle counters as small cards/pills with background colors matching their status. Add icons next to each counter.

- [ ] 16. **Empty state improvement** — Add an SVG illustration (a magnifying glass or globe icon). Improve typography with a headline + subtext. Add a CTA button suggesting to run a check.

- [ ] 17. **Add CSS animations** — Define `@keyframes fadeIn` for row entry. Define `@keyframes shimmer` for the progress bar. Define `@keyframes pulse` for the available badge. Add `transition` to all interactive elements.

- [ ] 18. **Mobile responsive improvements** — At `max-width: 768px`: stack the header vertically, make filter chips horizontally scrollable with `overflow-x: auto`, reduce card padding, make the registrar selector wrap cleanly, ensure action buttons don't overflow.

- [ ] 19. **Scrollbar styling** — Add custom dark-themed scrollbar styles using `::-webkit-scrollbar` for consistency with the dark theme.

- [ ] 20. **Final polish pass** — Review all spacing for consistency (use multiples of 4px). Ensure all color transitions are smooth. Test the full flow visually: keywords → generate → streaming results → filtering.

# Risks / Open questions

- **Single file size** — All changes are in one HTML file which is already ~930 lines. The file will grow but should remain manageable for a single-page app.
- **Browser compatibility** — `backdrop-filter: blur()` for the sticky header doesn't work in all browsers. We'll add a solid fallback background.
- **Performance** — CSS animations on table rows could impact performance with thousands of rows. We'll use `will-change` sparingly and keep animations simple (opacity/transform only).
- **Streaming results** — The fade-in animation for table rows needs to work with the existing `innerHTML` bulk update approach in `renderTable()`. May need to add animation classes via JS after render.
