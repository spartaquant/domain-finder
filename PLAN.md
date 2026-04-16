# Goal

Modernize and polish the Domain Finder UI — improve visual hierarchy, add micro-interactions, refine spacing/typography, and make the overall experience feel more premium while keeping the existing dark theme and vanilla HTML/CSS/JS stack.

# Approach

The app is a single `static/index.html` file with inline CSS and JS. All changes will be contained to this file. The design improvements focus on high-impact visual changes: better header with branding, glassmorphism-style cards, smoother animations, improved table readability, a proper stats dashboard, and polished interactive states. No structural changes to the backend or WebSocket logic.

Key design decisions:
- **Keep it vanilla** — no frameworks, no build step. All CSS stays inline.
- **Dark theme stays** — refine the palette with slightly richer tones and more contrast layers.
- **Progressive enhancement** — animations use CSS transitions/keyframes so the app works fine without them.
- **Mobile-first polish** — improve responsive breakpoints and touch targets.

# Tasks

1. **Revamp header and branding**
   - Animated gradient logo with subtle pulse
   - Better typography hierarchy for the title and subtitle
   - Add a thin accent border/glow line below the header for visual separation

2. **Upgrade card and layout system**
   - Add glassmorphism effect to cards (subtle backdrop-blur, softer borders)
   - Improve spacing rhythm (consistent padding/margins using a 4px/8px grid)
   - Add subtle card entrance animations (fade-in on load)
   - Add a faint background pattern or gradient mesh to the body for depth

3. **Polish interactive elements (buttons, inputs, chips, tags)**
   - Add hover/active scale micro-interactions to buttons
   - Improve focus ring styles for accessibility
   - Add transition animations to filter chips (smooth background/color changes)
   - Better keyword tag design with smoother remove animation
   - Style the multiselect dropdown with better shadows and option hover states
   - Improve registrar selector pill appearance

4. **Redesign the progress section**
   - Wider, more visible progress bar with animated gradient shimmer while active
   - Add a pulsing dot or spinner next to "Checked X / Y" while scanning
   - Animate the counter numbers (smooth counting transitions via CSS)
   - Show an estimated time or speed indicator (domains/sec)

5. **Improve results table design**
   - Alternating row tinting for readability
   - Better status badges with subtle icon animations (pulse on "likely available")
   - Improve score bar visual — add gradient coloring based on score value (green for high, dimmer for low)
   - Sticky table header when scrolling
   - Add row entrance animation for newly arriving results
   - Better action button hover states with tooltip-style labels

6. **Add summary stats dashboard**
   - Replace the plain counter line with a row of styled stat cards above the table (total, available, registered, unknown)
   - Each stat card gets an icon, a large number, and a label
   - Color-code each card to match its status color

7. **Refine typography, colors, and responsive layout**
   - Tighten the color palette — add a secondary accent color for variety
   - Improve font size scale for better hierarchy
   - Add a footer with subtle branding
   - Improve mobile layout: stack filters vertically, full-width buttons, collapsible keyword area
   - Add smooth scroll behavior and better overflow handling on the table

# Risks / Open questions

- **Font loading** — the app loads Inter and JetBrains Mono from Google Fonts. Adding more weights or a new font could slow initial render. We'll keep the same fonts and just use existing weights more effectively.
- **Performance with large tables** — CSS animations on table rows could cause jank with 5000+ rows. We'll limit entrance animations to the first visible batch and use `will-change` sparingly.
- **Backdrop-filter support** — `backdrop-filter: blur()` for glassmorphism isn't supported in all browsers. We'll add a solid fallback background.
