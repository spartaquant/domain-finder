# Goal
Improve the visual design of the Domain Finder web app for a more polished, modern look while keeping the existing dark theme and vanilla HTML/CSS/JS stack.

# Approach
The app is a single `static/index.html` file (~930 lines) with inline CSS and JS. The current design is functional but utilitarian — flat cards, basic table, cramped keyword tags, and no visual hierarchy beyond font sizes. The improvements will focus on polish, spacing, visual hierarchy, and micro-interactions without changing any backend code or app functionality.

Key design decisions:
- **Keep the single-file architecture** — no build tools, no CSS frameworks
- **Enhance the existing dark palette** rather than replacing it — add subtle gradients, glows, and depth
- **Improve information density** — the keyword area and results table are the core of the UX and need the most attention
- **Add tasteful motion** — subtle transitions on interactive elements, smooth progress animations
- **Better initial state** — the app currently shows nothing until you run a check; add a welcoming empty state

# Tasks

1. **Header & layout polish**
   - Add a subtle gradient mesh or noise texture to the page background for depth
   - Redesign the header with a larger logo, subtle glow effect, and a tagline
   - Add a sticky/fixed summary bar that shows key stats when scrolling past the progress area
   - Improve overall spacing and max-width rhythm

2. **Keywords section redesign**
   - Make keyword tags larger and more readable with better padding and font size
   - Add a count badge showing total keywords
   - Add smooth entrance animation when tags are added
   - Improve the input area with a clearer visual affordance (icon, better placeholder)
   - Group action buttons (Add/Reset) more clearly with better visual weight

3. **Progress & stats visual upgrade**
   - Redesign the progress bar — thicker, with animated gradient, glow effect, and percentage label
   - Add animated stat counters (available/registered/unknown) as card-style widgets instead of inline text
   - Add a subtle pulse animation while checking is in progress
   - Smooth transitions when numbers update

4. **Results table & filters overhaul**
   - Redesign filter chips with better active states, counts inside each chip, and subtle transitions
   - Improve the search input with a search icon and clear button
   - Restyle the table: add alternating row shading, better hover states, larger touch targets
   - Make the domain name column more prominent (larger font, accent color for available domains)
   - Improve the score visualization — wider bar with gradient and numeric label
   - Better status badges with icons instead of dots
   - Improve action buttons (Copy/Register) with clearer hover states and better iconography
   - Add a polished empty/initial state with an illustration or icon and call-to-action text

5. **Multiselect & dropdown polish**
   - Add smooth open/close animation to the dropdown
   - Better visual separation between selected tags and search input
   - Improve option hover/highlight states with smoother transitions
   - Add a subtle backdrop blur or shadow to the dropdown

6. **Micro-interactions & finishing touches**
   - Add smooth CSS transitions on all interactive elements (buttons, chips, tags)
   - Add a subtle loading skeleton or shimmer effect while waiting for results
   - Improve the "copied" feedback with a toast notification instead of inline text swap
   - Add keyboard focus-visible styles for accessibility
   - Improve scrollbar styling to match the dark theme
   - Add a subtle footer with credit/version info

# Risks / Open questions
- **Performance**: Adding too many CSS animations or effects to a table with potentially thousands of rows could cause jank. The table rendering is already throttled via `requestAnimationFrame`, but heavy CSS effects on `<tr>` elements should be kept minimal.
- **Font loading**: The app uses Google Fonts (Inter, JetBrains Mono) which adds a network dependency. Consider adding `font-display: swap` if not already present.
- **Single-file constraint**: All changes go into one ~1000-line HTML file. This is manageable but the CSS section is already ~290 lines and will grow. Consider organizing CSS with clear section comments.
- **Scope creep**: "Improve design" is open-ended. The plan focuses on visual polish without changing functionality, layouts, or adding new features. If the user wants specific areas prioritized, that should be clarified.
