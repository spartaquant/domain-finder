# Goal

Modernize the visual design of the Domain Finder single-page app — keep the dark theme and single-file architecture, but elevate the overall polish and feel.

# Approach

The current UI is solid functionally but looks like a typical "developer dark theme." The goal is to make it feel more like a polished product — think Linear, Vercel Dashboard, or Raycast. We'll stay in the single `index.html` file and focus on CSS + minor HTML tweaks (no structural/JS logic changes).

Key design moves:
- **Subtler, richer color palette** — shift from the flat navy/indigo to deeper, slightly warmer tones with more nuanced surface layering (3-4 surface levels instead of 2). Reduce border reliance in favor of elevation via subtle shadows and background contrast.
- **Better typography hierarchy** — increase heading weight contrast, use slightly larger domain names in the table, tighten line-heights for data-dense areas, add font-feature-settings for the monospace font.
- **Refined components** — softer filter chips with better active/hover states, keyword tags with more breathing room, smoother transitions, and a more polished progress bar (animated gradient shimmer while active).
- **Table glow-up** — alternating row tints (very subtle), better column spacing, sticky header, improved status badges with subtle glow effects, and a cleaner score bar visualization.
- **Micro-interactions** — smooth hover lifts on cards, button press states, subtle focus rings, and a fade-in for new table rows during streaming.
- **Header & branding** — a more distinctive logo treatment with a subtle animated gradient, better subtitle styling.

All changes are CSS-only or minor HTML class/attribute tweaks. No JavaScript logic changes. No file splitting.

# Tasks

1. **Color system & CSS custom properties overhaul**
   - Redesign the `:root` variable palette with richer surface tones (4 levels: bg, surface, surface-raised, surface-overlay)
   - Add subtle warm undertones to the grays (e.g., slate instead of pure blue-gray)
   - Introduce `--shadow-sm`, `--shadow-md`, `--shadow-lg` tokens for elevation
   - Add `--transition-fast` and `--transition-normal` timing tokens
   - Refine accent, green, red, yellow colors to be slightly more vibrant/modern

2. **Typography & base element refinements**
   - Tighten body line-height for data-dense UI (1.4 instead of 1.5)
   - Improve header: animated gradient on logo, better visual weight on title, styled subtitle as a muted pill/badge
   - Refine `.card-title` with a left accent bar instead of just uppercase text
   - Add `font-feature-settings: "ss01", "cv01"` to Inter for modern alternates
   - Better `::selection` styling

3. **Component polish: keywords, buttons, inputs**
   - Keyword tags: slightly larger padding, softer border radius, subtle inner shadow, smoother hover-to-delete transition
   - Buttons: add subtle gradient to primary, press-down transform on `:active`, better disabled state (not just opacity)
   - Inputs: inner glow on focus instead of just border color change, slightly taller for better touch targets
   - Filter chips: pill shape with subtle background shift on hover, active state with accent glow/shadow

4. **Progress bar & loading states**
   - Animated gradient shimmer on the progress bar fill (CSS `@keyframes` moving gradient)
   - Subtle pulse animation on the stats numbers while checking is active
   - Smoother width transition on the bar fill

5. **Results table modernization**
   - Very subtle alternating row backgrounds (every other row slightly lighter)
   - Sticky `thead` with a backdrop-blur effect and bottom shadow
   - Status badges: add subtle `box-shadow` glow matching their color
   - Score bar: slightly taller, rounded ends, gradient that shifts with value
   - Domain name column: subtle hover highlight effect
   - Action buttons: better icon alignment, hover lift with shadow
   - Fade-in animation for rows as they appear during streaming (CSS `@keyframes fadeIn` applied via class)

6. **Multiselect dropdown & filter row polish**
   - Dropdown: add backdrop-blur, softer shadow, smooth open/close with max-height transition
   - Selected tags: refined pill style matching the accent palette
   - Options: smoother highlight transition, add checkmark icon for selected items
   - Better visual grouping of the filter row (keyword filter + position filter) with subtle separator or background section

# Risks / Open questions

- **Font loading**: We rely on Google Fonts for Inter and JetBrains Mono. If the user is offline, the fallback system fonts will look different. No change planned here — just noting it.
- **Browser compat**: `backdrop-filter: blur()` doesn't work in older Firefox versions. We'll use it as progressive enhancement with a solid fallback background.
- **Performance**: CSS animations on the table during streaming could cause jank with thousands of rows. We'll keep animations lightweight (opacity/transform only, avoid layout-triggering properties) and limit fade-in to the initial appearance only.
