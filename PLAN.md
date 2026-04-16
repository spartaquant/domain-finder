# Goal

Visually polish and refine the Domain Finder UI — improve spacing, typography, component styling, and micro-interactions while keeping the existing dark theme and all functionality intact.

# Approach

The app is a single `static/index.html` file with inline CSS and JS. All changes are frontend-only. The strategy is to elevate the existing design with modern touches — better visual hierarchy, subtle animations, refined components, and more polished details — without changing the app's structure or behavior.

Key design directions:
- **Refined color palette**: Slightly adjust surface/border colors for better contrast and depth. Add subtle gradients and glow effects to key interactive elements.
- **Better typography & spacing**: Increase whitespace between sections, improve line heights, and add more visual breathing room throughout.
- **Component upgrades**: Polish the keyword tags, table rows, buttons, filter chips, and progress bar with smoother transitions, hover states, and subtle shadows.
- **Visual hierarchy**: Make the header more prominent, add section dividers or subtle backgrounds, and ensure the most important information (available domains) stands out.
- **Micro-interactions**: Add smooth transitions for table row hovers, button clicks, filter state changes, and status badge appearances.
- **Table improvements**: Alternating row tints, better cell spacing, sticky header, and improved score bar visualization.

All changes stay within the single `index.html` file. No new dependencies — just refined CSS and minor HTML tweaks.

# Tasks

1. **Refine color palette & global styles**
   - Adjust CSS custom properties: softer surface colors, slightly more contrast on borders, richer accent tones
   - Add a subtle radial gradient or noise texture to the body background for depth
   - Improve the `::selection` style and scrollbar styling for a more cohesive feel
   - Add smooth `scroll-behavior` and improved focus-visible outlines for accessibility

2. **Upgrade header & layout**
   - Make the logo larger with a subtle animated gradient or glow effect
   - Add a thin decorative accent line or gradient border below the header
   - Increase overall section spacing (cards, actions row, progress)
   - Add a subtle footer with muted text

3. **Polish keyword tags & input area**
   - Refine keyword tag styling: slightly rounded, subtle inner shadow, smoother hover transitions
   - Improve the input field with a subtle focus glow/ring effect
   - Add a smooth entrance animation when new tags appear
   - Better visual separation between the keyword area and input row (e.g. subtle divider)

4. **Enhance buttons, filters & progress bar**
   - Add subtle box-shadow and hover lift/glow to primary buttons
   - Refine filter chips with smoother active-state transitions and a subtle background pulse
   - Upgrade the progress bar: taller track, animated gradient fill, subtle glow on the leading edge
   - Add a shimmer/pulse animation while checking is in progress
   - Improve the registrar selector styling to match the refined filter chips

5. **Redesign table & results presentation**
   - Add alternating row backgrounds (very subtle tint difference)
   - Make the table header sticky with a backdrop blur effect
   - Improve score bar: taller, rounded, with a gradient that shifts based on score value
   - Refine status badges: slightly larger, with subtle background blur/glow
   - Better hover state on rows: left accent border or gentle highlight
   - Improve action buttons with cleaner icon styling and smoother hover transitions
   - Polish the empty state with a subtle icon or illustration

6. **Add micro-interactions & finishing touches**
   - Smooth fade-in for the results card when it first appears
   - Add `transition` to table rows for smoother batch rendering
   - Subtle scale transform on button hover/active states
   - Smooth transitions on filter chip state changes
   - Add a gentle loading skeleton or shimmer placeholder while waiting for first results
   - Ensure the multiselect dropdown has a refined shadow and border treatment

# Risks / Open questions

- **Performance**: Adding CSS animations/transitions to hundreds of table rows could cause jank during batch rendering. Keep transitions lightweight (opacity, background-color only on tbody rows) and avoid transforms on large lists.
- **Font loading**: The app already uses Google Fonts (Inter, JetBrains Mono). No changes needed here, but if the connection is slow, fallbacks should still look good.
- **Scope creep**: "Polish" is subjective — the plan focuses on CSS refinements and minor HTML tweaks only. No structural changes, no new features, no JS logic changes.
