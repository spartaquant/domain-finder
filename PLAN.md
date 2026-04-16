# Goal
Modernize and polish the Domain Finder UI with better visual hierarchy, micro-interactions, layout improvements, and a more refined dark-theme aesthetic — all within the existing single-file vanilla HTML/CSS/JS architecture.

# Approach
The app already has a solid dark theme foundation. The improvements focus on **visual polish** rather than restructuring: better spacing, subtle animations, improved component design, and a more professional feel. Everything stays in `static/index.html` — no build tools or frameworks added.

Key design decisions:
- Keep the existing color palette (indigo accent + dark navy bg) but refine it with better contrast and depth
- Add subtle glassmorphism to cards for modern depth
- Improve the keyword section with a collapsible container so the 100+ tags don't dominate the page
- Add smooth transitions and micro-animations for status changes, progress, and table rows
- Improve the table with better row styling, sticky header, and row entrance animations
- Add a proper initial state / landing view before any search is run
- Improve mobile layout

# Tasks

1. **Header & branding polish**
   - Add a subtle gradient text effect to the title
   - Animate the logo icon with a gentle pulse/glow
   - Add a tagline or description below the header
   - Add a favicon via inline SVG data URI

2. **Card & layout refinements**
   - Add subtle glassmorphism effect to cards (backdrop-filter blur + translucent bg)
   - Improve card shadows with layered box-shadows for depth
   - Add hover lift effect on interactive cards
   - Improve spacing between sections
   - Add section dividers or visual grouping

3. **Keywords section overhaul**
   - Make the keywords area collapsible with a toggle showing count (e.g. "Keywords (97) ▾")
   - Cap the default visible height with a smooth expand/collapse animation
   - Improve tag styling with slightly rounded pill shapes
   - Add a subtle entrance animation when tags are added
   - Better visual feedback when hovering to remove

4. **Buttons, filters & controls polish**
   - Add ripple or press feedback on the primary CTA button
   - Improve filter chips with smoother active-state transitions
   - Add icon to the search input (magnifying glass)
   - Improve the multiselect dropdown with better shadows and animations
   - Style the registrar selector as a proper toggle group
   - Add loading spinner to the "Generate & Check" button while running

5. **Progress & stats improvements**
   - Replace the thin progress bar with a more prominent animated bar with glow effect
   - Add stat cards (total, available, registered, unknown) as a mini dashboard row with count-up animation
   - Add a pulsing dot or spinner indicator while checking is in progress
   - Smooth number transitions on counters

6. **Table & results polish**
   - Add sticky table header so column names stay visible on scroll
   - Subtle alternating row tinting for readability
   - Row entrance animation (fade-in slide-up) as results stream in
   - Improve status badges with subtle icon animations
   - Better score bar with gradient and rounded ends
   - Add hover preview or tooltip on domain names
   - Virtual scroll or "show more" pagination if >200 rows to prevent DOM bloat

7. **Empty & initial states**
   - Design a welcoming initial state with an illustration/icon and call-to-action before first search
   - Improve the "no results match" empty state with a more helpful message and icon
   - Add a subtle background pattern or gradient to the page

8. **Responsive & finishing touches**
   - Improve mobile layout: stack filters vertically, full-width buttons, collapsible sections
   - Add smooth scroll-to-results when checking begins
   - Add a "back to top" button when scrolled down
   - Add CSS transitions on all interactive state changes
   - Ensure focus-visible outlines for accessibility

# Risks / Open questions
- **Glassmorphism browser support**: `backdrop-filter` is not supported in older Firefox versions — will add a solid fallback background
- **Performance with large tables**: Adding row animations for 5000+ rows could cause jank — animations should only apply to newly added rows, not re-renders
- **Single file size**: All CSS/JS stays in one HTML file which is already ~900 lines — this will grow but remains manageable for a tool like this
- **Font loading**: Currently loads Inter + JetBrains Mono from Google Fonts — no change needed, but slow connections may see FOUT
