# Goal
Modernize the Domain Finder UI with improved visual hierarchy, polished components, micro-interactions, and a more refined dark theme — all within the existing single-file `static/index.html`.

# Approach
The app currently has a solid functional foundation but looks like a developer tool rather than a polished product. The redesign will focus on:

- **Visual hierarchy**: Use glassmorphism-style cards with subtle backdrop blur and layered surfaces to create depth. Add gradient accents and better spacing to guide the eye.
- **Header & branding**: Animated gradient logo, subtitle styling, and a more commanding top section.
- **Stats dashboard**: Replace the inline progress stats with a row of summary stat cards (total, available, registered, unknown) that update live — giving the results section a dashboard feel.
- **Table polish**: Alternating row tints, smoother hover states, sticky header, better badge and score bar designs. Larger touch targets for action buttons.
- **Keyword section**: Collapsible keyword area (since 100+ tags dominate the page), better tag styling with subtle gradients, and a count badge.
- **Animations**: CSS transitions on card entry, progress bar pulse animation, smooth filter transitions, and a skeleton/shimmer loading state while checking.
- **Typography**: Tighten the type scale, add font-weight contrast, improve label/value pairing in stats.
- **Responsive**: Better mobile layout for filters row and table (horizontal scroll with shadow hint).
- **Empty state**: Add a simple SVG illustration and more helpful messaging.
- **Footer**: Minimal footer with app info.

All changes stay in `static/index.html` — no new files, no build tools, no framework dependencies.

# Tasks

1. **Revamp CSS variables, base styles & glassmorphism cards**
   - Update color palette: richer surface layers, softer borders, more vibrant accents
   - Add glassmorphism utility: `backdrop-filter: blur()`, semi-transparent backgrounds
   - Add CSS keyframe animations: `fadeIn`, `slideUp`, `pulse` for progress bar, `shimmer` for loading
   - Improve base typography: tighter line-heights for headings, better font-weight scale
   - Add subtle background texture or gradient mesh to `body`

2. **Redesign header, keyword section & action buttons**
   - Header: gradient text on the title, animated logo with hover effect, better subtitle styling
   - Keywords: make the section collapsible with a toggle (show/hide with count badge like "Keywords (98)")
   - Keyword tags: softer background, rounded pill shape, better hover/remove animation
   - Action buttons: larger primary CTA with gradient background, icon animation on hover, better disabled state
   - Add a divider or visual break between keywords section and results

3. **Build live stats dashboard cards & improve progress bar**
   - Replace inline progress stats with 4 mini stat cards in a grid row: Total, Available, Registered, Unknown — each with an icon, large number, and colored accent border
   - Animate number changes with a brief scale pulse
   - Progress bar: add glow effect, animated gradient, and percentage label
   - Add a subtle "checking..." shimmer animation on the progress section while active

4. **Polish results table, filters & registrar selector**
   - Table: sticky `thead`, alternating row backgrounds, larger padding, better column widths
   - Domain name column: subtle gradient text or accent color for available domains
   - Score bar: wider, with a tooltip showing exact score, smoother gradient
   - Status badges: add subtle box-shadow glow matching their color
   - Filter chips: pill shape with icon indicators, animated active state transition
   - Search input: add a search icon inside the input (CSS pseudo-element or inline SVG)
   - Registrar selector: style as a segmented control rather than plain chips
   - Keyword multiselect: better dropdown shadow, smoother open/close animation
   - Action buttons in table: better spacing, hover lift effect
   - Empty state: add a simple inline SVG graphic (magnifying glass or globe) and friendlier copy

5. **Add responsive improvements & finishing touches**
   - Mobile: stack stat cards 2x2, collapse filters into a scrollable row, table horizontal scroll with fade-edge hint
   - Add smooth scroll behavior
   - Add `prefers-reduced-motion` media query to disable animations for accessibility
   - Add a minimal footer with "Domain Finder — powered by RDAP"
   - Ensure all interactive elements have visible focus styles for keyboard navigation

# Risks / Open questions
- **Performance with 100+ keyword tags**: The collapsible section mitigates this, but rendering 100+ DOM elements with animations may be sluggish on low-end devices. May need to limit animation to visible tags.
- **Backdrop-filter support**: Glassmorphism relies on `backdrop-filter` which has good but not universal support. Will include a solid-color fallback.
- **Single file size**: All CSS/JS is inline. After the redesign the file will be larger (~40-50KB). This is fine for a local tool but worth noting.
- **No design mockup**: Without a specific design reference, the improvements are based on modern dark-theme dashboard conventions. The user may want to adjust specific colors or layout choices after seeing the result.
