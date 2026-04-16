# Goal

Improve the visual design and UX polish of the Domain Finder web app while keeping the single-file vanilla HTML/CSS/JS architecture.

# Approach

The current design is functional with a decent dark theme, but feels utilitarian. The improvements focus on visual hierarchy, spacing, micro-interactions, and layout refinements that make the app feel more polished and professional — without adding frameworks or changing the backend.

Key design decisions:
- **Keep the single-file approach** — all changes stay in `static/index.html`
- **Preserve the dark color palette** but refine it with better contrast and depth
- **Focus on the results table** since that's where users spend most of their time
- **Add subtle animations** for state transitions (results appearing, progress, filters)
- **Improve information density** — the filter/control area currently takes too many vertical rows

# Tasks

1. **Refine visual foundation (colors, typography, spacing)**
   - Add subtle background texture/gradient to body instead of flat color
   - Improve card depth with subtle box-shadows and slightly refined border colors
   - Tighten spacing between sections for better visual flow
   - Add a subtle gradient or glow accent to the header logo
   - Improve the header with a tagline area and better visual weight

2. **Redesign the keywords section**
   - Make the keywords area collapsible (collapsed by default after first run) with a toggle showing keyword count
   - Add a max-height with smooth scroll so large keyword lists don't dominate the page
   - Improve tag styling with slightly more visual distinction
   - Add a subtle entry animation when new keywords are added

3. **Consolidate and polish the filter/controls bar**
   - Combine the status filters, search input, and keyword position filter into a single compact toolbar row
   - Use a more compact layout: search on the left, status chips in the center, keyword filter on the right
   - Add result count badges directly on the filter chips (e.g., "Available (42)")
   - Style the active filter chip with a glow effect instead of just a color swap

4. **Upgrade the results table**
   - Add alternating row backgrounds (very subtle) for easier scanning
   - Improve the domain name column with slightly larger, bolder text
   - Add a subtle row entrance animation as results stream in
   - Make the score bar wider and more prominent with a gradient that shifts from blue to purple to green based on score
   - Add hover cards/tooltips showing quick info on hover
   - Improve the status badges with a subtle pulse animation for "likely available" domains
   - Add row highlighting — available domains get a very faint green left-border accent

5. **Improve progress and state feedback**
   - Redesign the progress bar to be thicker with animated gradient shimmer while active
   - Add a pulsing dot or spinner next to "Checking..." text during active scan
   - Add a completion celebration state (subtle flash or counter animation when done)
   - Show a skeleton/placeholder state in the table before results arrive
   - Improve the empty state with a better illustration/icon

6. **Add responsive polish and micro-interactions**
   - Smooth transitions on all filter/sort state changes
   - Button press/click feedback (scale-down micro-animation)
   - Smooth scroll to results card when check starts
   - Improve mobile layout: stack filters vertically, make table horizontally scrollable with frozen first column
   - Add a "scroll to top" floating button when scrolled down in long result lists
   - Add favicon as inline SVG data URI

# Risks / Open questions

- **Performance with large result sets**: Row entrance animations should be limited to the first render batch to avoid jank with thousands of rows. Use `will-change` and `contain` CSS properties.
- **Keywords collapse state**: Need to decide if collapsed state persists across runs (localStorage) or resets each session. Defaulting to session-only.
- **Filter bar consolidation**: Fitting all controls on one row may be tight on smaller screens — may need a two-row layout below 1024px breakpoint.
