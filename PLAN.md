# Goal

Modernize and polish the Domain Finder UI — improve visual hierarchy, spacing, micro-interactions, and overall feel while keeping the single-file vanilla HTML/CSS/JS architecture.

# Approach

The current design is a solid dark-theme foundation but feels flat and utilitarian. The improvements focus on five areas:

1. **Visual hierarchy & layout** — Add a hero/title section with a subtle gradient or animated background accent, improve card depth with layered shadows instead of flat borders, and add section spacing rhythm.

2. **Typography & readability** — Increase base font sizes slightly, improve contrast ratios, add better visual weight differentiation between labels and values.

3. **Micro-interactions & polish** — Add smooth transitions on card hover, button press states, skeleton loading placeholders while checking, animated progress bar with pulse/shimmer effect, and smooth table row entrance animations.

4. **Component upgrades** — Redesign keyword tags with better padding and a pill shape, improve the status badges with subtle glow effects, add a sticky table header for scrolling, improve the filter chips with count badges, and make the results table rows feel more like cards on mobile.

5. **Responsive & UX improvements** — Better mobile layout for the filters/search area, add a "scroll to top" when results load, improve the empty state with an illustration-style SVG, add subtle background grid/dot pattern for depth.

All changes stay within `static/index.html` — no new files or dependencies beyond Google Fonts already in use.

# Tasks

- [ ] 1. **Upgrade CSS variables & base styles** — Add new CSS custom properties for shadows, gradients, and animation timings. Add a subtle dot-grid background pattern to `body`. Improve the `--surface` color layering for better card depth.

- [ ] 2. **Redesign header** — Make the logo larger with an animated gradient. Add a subtitle with a typewriter or fade effect. Add a subtle divider line below the header.

- [ ] 3. **Improve card component** — Add layered box-shadows for depth (not just borders). Add subtle hover lift on cards. Improve internal padding and spacing rhythm.

- [ ] 4. **Redesign keyword tags** — Larger touch targets, better pill shape, smoother hover transitions, add a subtle entrance animation when rendered. Improve the highlight (match/dim) states with better contrast.

- [ ] 5. **Upgrade buttons** — Add press/active states with scale transform. Add subtle box-shadow glow on primary button. Improve disabled state styling.

- [ ] 6. **Enhance progress bar** — Add shimmer/pulse animation while active. Show a percentage label. Add a subtle glow effect on the fill bar. Improve the stats row layout.

- [ ] 7. **Improve filter chips** — Add count badges (e.g., "Likely Available (42)") that update live. Add a subtle background pulse when count changes. Better active state with glow.

- [ ] 8. **Polish results table** — Add sticky header on scroll. Improve row hover effect with left accent border. Add subtle entrance animation for new rows. Improve score bar visual (gradient + rounded). Better action button hover states.

- [ ] 9. **Upgrade status badges** — Add subtle glow/shadow matching the status color. Slightly larger with better padding. Improve the dot indicator animation (pulse for "likely available").

- [ ] 10. **Improve mobile responsiveness** — Stack filters vertically on small screens. Make table horizontally scrollable with a fade edge indicator. Improve touch targets for all interactive elements.

- [ ] 11. **Add empty/loading states** — Add an SVG illustration for the empty state. Add skeleton placeholder rows during loading. Add a "no results yet — click Generate" initial state.

- [ ] 12. **Add finishing touches** — Smooth scroll behavior. Subtle fade-in on page load. Add `::selection` color. Improve focus ring styles for accessibility. Add a footer with minimal branding.

# Risks / Open questions

- **Performance**: Table entrance animations on 1000+ rows could be janky — will limit animations to visible rows or first batch only.
- **Font loading**: Already using Google Fonts (Inter + JetBrains Mono) so no new network requests needed.
- **Single file size**: The HTML file is already ~900 lines. These changes will grow it but keeping everything in one file is the established pattern.
