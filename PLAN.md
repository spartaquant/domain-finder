# Goal
Improve the existing light theme so it feels intentionally designed rather than a mechanical variable swap — better contrast, refined depth/shadows, polished component styles, and visual consistency across all UI elements.

---

# Approach

The current light theme (lines 40–66 of `static/index.html`) overrides CSS custom properties but leaves several areas under-polished: the progress bar and logo gradients are tuned for dark backgrounds, cards lack shadow-based depth, inputs and table rows feel flat, and some text/color combinations have weak contrast.

**Strategy: enhance the `[data-theme="light"]` block and add targeted light-mode overrides** — no structural HTML changes, no new files. We'll add a few new CSS variables for light-specific shadows and gradients, and add `[data-theme="light"]` selector rules for components that need more than a variable swap (cards, buttons, inputs, table header, progress bar, logo).

> Key constraint: all changes stay within `<style>` in `static/index.html`. No backend changes needed.

---

# Architecture

```diagram
static/index.html
├── <style>
│   ├── :root (dark vars)          ← unchanged
│   ├── [data-theme="light"]       ← ENHANCE: refine colors, add shadow vars
│   ├── Component rules            ← ADD: [data-theme="light"] overrides for
│   │   ├── .card                     cards, inputs, buttons, table, progress,
│   │   ├── .btn-primary              logo, filter chips, status badges,
│   │   ├── table thead               multiselect dropdown
│   │   ├── .progress-bar-fill
│   │   ├── .logo
│   │   └── ...
│   └── @media responsive          ← unchanged
└── <script>                       ← unchanged
```

---

# Tasks

### Phase 1: Refine light theme color variables
- Adjust `--bg` to a warmer/softer off-white (e.g. `#f8f9fb`) for less harshness
- Improve `--surface2` contrast — current `#edf0f5` is close to `--bg`, make it more distinct
- Darken `--muted` slightly for better readability against light backgrounds
- Add new variables: `--card-shadow`, `--input-focus-ring`, `--header-border` for light-specific depth cues
- Adjust `--accent` and `--accent-glow` to have better contrast on white (WCAG AA target)
- Tweak status colors (`--green`, `--red`, `--yellow`) for better legibility on light backgrounds
- **Complexity:** Low

### Phase 2: Cards, inputs, and surface depth
- Add subtle `box-shadow` to `.card` in light mode instead of relying solely on border for depth
- Give inputs (`.kw-input-row input`, `.search-row input`, `.ms-trigger`) a light inset shadow and slightly stronger border
- Add a subtle focus ring (box-shadow) on input focus for better affordance
- Refine `.ms-dropdown` shadow to be softer/larger for light mode (current `--dropdown-shadow` is very subtle at 0.12 opacity)
- **Complexity:** Low

### Phase 3: Header, logo, and progress bar
- Adjust `.logo` gradient to use deeper accent tones that pop on light backgrounds
- Add a bottom border or subtle shadow to `header` for visual separation in light mode
- Change `.progress-bar-fill` gradient to use richer accent colors that stand out on `--surface2` track
- Ensure `.score-bar .bar-fill` gradient also looks vivid on light backgrounds
- **Complexity:** Low

### Phase 4: Buttons, filter chips, and table
- Give `.btn-primary` a subtle shadow in light mode for depth
- Improve `.btn-secondary` hover state — add slight background tint instead of just border change
- Make `.filter-chip.active` background slightly deeper/more saturated
- Add a light background tint to `thead` row for visual table header separation
- Improve `tbody tr:hover` to be more visible in light mode
- Refine `.status-badge` background opacities — bump up slightly so badges are more visible against white
- **Complexity:** Low

### Phase 5: Keyword tags, multiselect, and misc polish
- Improve `.kw-tag` styling: slightly stronger border and background in light mode
- Make `.kw-tag.kw-match` yellow highlight more visible on light backgrounds
- Refine `.ms-tag` colors for better contrast on light surfaces
- Ensure `.icon-btn.primary` (register button) has sufficient contrast
- Polish `.theme-toggle` button appearance in light mode
- Add smooth `transition` on `background-color` to `body` for theme switch animation
- **Complexity:** Low

---

# Risks / Open questions
- **Risk:** Adjusting accent color for light mode contrast could make it look different from the dark theme brand — will keep changes subtle (darken slightly, not change hue)
- **Risk:** Adding shadows to cards in light mode could feel heavy on mobile — will use very subtle shadows (1-2px blur)
- **Open question:** Should the light theme `--bg` be pure white (`#fff`) or stay off-white? Plan defaults to a soft off-white for reduced eye strain

---

# Non-goals
- No changes to the dark theme
- No HTML structure changes
- No backend/Python changes
- No new external dependencies or fonts
