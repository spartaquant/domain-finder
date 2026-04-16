# Goal
Improve the visual design and UX polish of the Domain Finder web app while keeping the vanilla HTML/CSS/JS stack.

# Approach
The current app has a solid dark-theme foundation but feels utilitarian. The improvements focus on visual hierarchy, micro-interactions, layout refinement, and modern polish — without changing the tech stack or backend. All changes are in `static/index.html`.

Key design decisions:
- Keep the single-file approach (all CSS/JS inline) for simplicity
- Add subtle glassmorphism effects to cards for depth
- Improve the header with a gradient text treatment and tagline
- Add stat summary cards above the results table for quick scanning
- Polish animations and transitions throughout
- Make the keyword section collapsible to reduce visual clutter once domains are generated
- Improve the table with row hover effects, better spacing, and alternating subtle backgrounds
- Add a smooth scroll-to-results behavior when generation starts
- Better empty/loading states with illustrations (CSS-only)
- Improve mobile responsiveness

# Tasks

1. **Header & branding polish**
   - Gradient text effect on "Domain Finder" title
   - Animated logo icon with hover effect
   - Add subtle tagline styling with a separator dot
   - Add a global CSS backdrop blur and noise texture overlay for depth

2. **Card & layout system upgrade**
   - Add glassmorphism effect to cards (subtle backdrop-filter blur, translucent bg)
   - Improve card shadows and border treatments with subtle glow on hover
   - Add collapsible keyword section with a toggle chevron (collapse after generation starts)
   - Better spacing rhythm between sections (consistent gap system)

3. **Stats dashboard cards**
   - Add a row of 4 mini stat cards above results (Total, Available, Registered, Unknown)
   - Each card gets an icon, count, and label with color-coded accents
   - Animate count numbers on update
   - Replace the inline progress stats with these cards

4. **Table & results polish**
   - Subtle alternating row backgrounds for readability
   - Improved hover state with left accent border
   - Better status badges with subtle pulse animation on "likely available"
   - Score bar gets a gradient that changes based on score value (green for high, orange for mid, red for low)
   - Domain name column gets a subtle hover underline linking to the domain
   - Smoother copy button feedback animation
   - Add pagination or virtual scroll hint for large result sets (show count + "showing first N")

5. **Filter & search bar improvements**
   - Group all filters into a single cohesive toolbar with a frosted-glass background
   - Search input gets a search icon prefix
   - Filter chips get count badges (e.g., "Available (42)")
   - Active filter chip gets a subtle glow effect
   - Keyword multiselect gets better tag styling with colored borders matching keyword importance

6. **Animations & micro-interactions**
   - Smooth entry animation for table rows as results stream in (fade + slide)
   - Progress bar gets a shimmer/pulse effect while active
   - Button press states with scale transform
   - Keyword tags get a pop-in animation when added
   - Smooth transitions when toggling filters (table re-renders with fade)
   - Add a CSS-only loading spinner for the initial generation state

7. **Empty states & responsive polish**
   - Better empty state with a CSS-illustrated magnifying glass or globe icon
   - "Getting started" hints in the empty state
   - Improve mobile layout: stack filters vertically, full-width cards, collapsible sections
   - Add a sticky header on scroll with compact mode
   - Ensure touch-friendly tap targets (min 44px) on mobile

# Risks / Open questions
- **Performance**: CSS animations on many table rows could lag with 5000+ results — may need to limit animations to the first visible batch or use `will-change` hints
- **Browser support**: `backdrop-filter` (glassmorphism) is not supported in older Firefox versions — need a solid fallback background color
- **Scope**: "Improve design" is broad — this plan focuses on visual polish and UX. If the user wants functional changes (new features, different layout paradigm, framework migration), that's a different scope
- **Font loading**: Currently using Google Fonts CDN — adding more weights or fonts could slow initial load
