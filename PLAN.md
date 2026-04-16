# Goal

Polish the Domain Finder UI with modern design improvements — better visual hierarchy, micro-interactions, layout refinements, and overall aesthetic uplift — all within the existing single-file `static/index.html`.

# Approach

The app already has a solid dark-theme foundation. The improvements focus on **visual polish** rather than structural rewrites: better spacing, subtle animations, improved component styling, and modern touches like glassmorphism cards, gradient accents, and animated feedback. All changes stay in `static/index.html` (inline CSS + JS).

Key design decisions:
- **Keep the single-file architecture** — no build tools, no external CSS frameworks
- **Enhance, don't replace** — preserve the existing color palette and layout structure
- **Focus on feel** — smooth transitions, hover states, and feedback make it feel premium
- **Improve information density** — summary stat cards above the table, better use of space

# Tasks

- [ ] **1. Upgrade header** — Add a subtle gradient text effect on the title, animate the logo with a hover glow, and add a thin gradient divider line below the header
- [ ] **2. Modernize cards** — Add subtle glassmorphism (backdrop blur + semi-transparent bg), softer box-shadow, and a faint gradient border on hover
- [ ] **3. Improve keyword tags area** — Make the keywords area scrollable with a max-height, add a smooth expand/collapse toggle ("Show all / Show less"), add a subtle entrance animation for tags, and improve the tag hover/remove interaction
- [ ] **4. Polish buttons** — Add press/active scale transform, improve disabled state, add a subtle gradient shine on the primary button, and a loading spinner state for the "Generate & Check" button while running
- [ ] **5. Enhance progress bar** — Add a pulsing glow animation while active, animated gradient stripes, and a completion celebration flash
- [ ] **6. Improve filter chips** — Add count badges on each filter chip (e.g., "Likely Available (42)"), animate the active state transition, and add a subtle background pulse when counts change
- [ ] **7. Add summary stat cards** — Insert a row of 4 small stat cards above the table (Total, Available, Registered, Unknown) with icons and colored accents, replacing the plain text counters
- [ ] **8. Upgrade table styling** — Sticky header with blur backdrop, subtle alternating row tinting, improved hover highlight with left accent border, smoother sort indicator transitions, and a fade-in animation for new rows
- [ ] **9. Improve status badges** — Add a subtle pulse animation on "likely available" badges, slightly larger and more readable, with an icon instead of a plain dot
- [ ] **10. Polish action buttons** — Better hover elevate effect, smoother copy-flash animation with a checkmark icon, and improved register button with registrar brand color accent
- [ ] **11. Add micro-animations** — Smooth fade-in for the results card on first appearance, scroll-linked subtle parallax on header, and transition for filter changes (fade out/in table rows)
- [ ] **12. Improve empty state** — Add an illustrated SVG empty state graphic (magnifying glass or globe), better typography, and a subtle floating animation
- [ ] **13. Enhance multiselect dropdown** — Add a smooth open/close slide animation, improve the tag pill styling with a gradient accent, and better keyboard navigation highlighting
- [ ] **14. Responsive refinements** — Improve mobile layout for stat cards (2x2 grid), ensure filter chips wrap nicely, and make the table horizontally scrollable with a scroll hint shadow
- [ ] **15. Add a minimal footer** — Small muted footer with "Domain Finder" and a subtle gradient line, keeping the page feeling complete

# Risks / Open questions

- **Performance**: Adding too many CSS animations/backdrop-filters could affect performance on low-end devices during large table renders. Keep animations simple and use `will-change` sparingly.
- **Scope**: "Improve design" is open-ended — this plan covers visual polish. If the user wants structural/UX changes (e.g., different layout, new features, mobile-first redesign), the scope would expand.
- **Browser support**: `backdrop-filter` (glassmorphism) is not supported in older Firefox versions — should include a fallback.
- **Table rendering perf**: Fade-in animations on table rows with 5000+ rows could be laggy. Should limit animation to visible/first-N rows only.
