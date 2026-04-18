# Goal
Redesign the Domain Finder UI with a clean, modern light theme and improved visual design throughout.

---

# Approach

The entire UI lives in a single file (`static/index.html`) with inline `<style>`. The current dark theme is defined via CSS custom properties in `:root`, which makes switching to light straightforward — **swap the color palette in `:root`** and adjust any hardcoded `rgba()` values scattered through the styles.

Beyond the palette swap, we'll **refine spacing, shadows, typography, and component polish** to make the light theme feel intentional rather than just "inverted dark." Light themes need subtle shadows and borders for depth (dark themes rely on luminance differences). We'll add soft box-shadows to cards, refine the progress bar gradient, and give status badges and filter chips crisper contrast.

> All changes are confined to `static/index.html` — no backend changes needed.

---

# Architecture

```diagram
static/index.html
├── <style> ── :root variables (palette swap here)
│   ├── Cards, buttons, badges
│   ├── Table styles
│   ├── Multiselect / filters
│   └── Responsive breakpoints
├── <body> ── HTML structure (unchanged)
└── <script> ── JS logic (unchanged)
```

---

# Tasks

### Phase 1: Light color palette
- Replace all `:root` CSS custom properties with light-theme values:
  - `--bg`: white/off-white (`#f8fafc`)
  - `--surface`: white (`#ffffff`)
  - `--surface2`: light gray (`#f1f5f9`)
  - `--border`: soft gray (`#e2e8f0`)
  - `--text`: dark slate (`#1e293b`)
  - `--muted`: medium gray (`#64748b`)
  - `--accent` / `--accent-glow`: keep indigo but adjust for light bg contrast
  - Status colors (green/red/yellow): darken slightly for readability on white, adjust `*-bg` opacity values
- **Complexity:** Low

### Phase 2: Card and layout refinements
- Add `box-shadow` to `.card` for subtle elevation (e.g. `0 1px 3px rgba(0,0,0,.08)`)
- Update header logo gradient to work well on light background
- Adjust `.app` max-width and padding if needed for better visual balance
- Update `body` background to a very subtle warm/cool off-white
- Fix any hardcoded `rgba()` colors in the styles that assumed a dark background (e.g. `tbody tr` hover, border colors)
- **Complexity:** Low

### Phase 3: Component polish — buttons, badges, chips
- Restyle `.btn-primary` for crisp contrast on light bg
- Update `.btn-secondary` border/background for light theme
- Adjust `.filter-chip` colors: inactive should be light gray, active stays accent-colored
- Refine `.status-badge` backgrounds — use slightly more saturated tints so they pop on white
- Update `.kw-tag` and `.kw-tag.kw-match` styles for light theme visibility
- Update `.icon-btn` and `.icon-btn.primary` for light context
- **Complexity:** Medium

### Phase 4: Table and data display
- Update table header (`thead th`) styling — subtle bottom border, muted text that reads well on white
- Fix `tbody tr:hover` background to a light indigo wash
- Adjust `.score-bar .bar` track color for light theme
- Ensure `.domain-name` monospace text has good contrast
- Update `.word-chip` background for light surfaces
- Fix `.ms-dropdown` shadow and background for light theme (currently uses dark shadow)
- **Complexity:** Low

### Phase 5: Input fields and multiselect
- Update all `input` backgrounds from dark surface to white/light gray with visible borders
- Adjust `.ms-trigger`, `.ms-tag`, `.ms-dropdown`, `.ms-option` for light palette
- Ensure focus states (border-color transitions) are visible on light background
- Update placeholder text color for readability
- **Complexity:** Low

### Phase 6: Progress bar and empty states
- Adjust progress bar track color for light bg
- Keep gradient fill (indigo → purple) — works on both themes
- Update `.empty-state` text color
- Update `.progress-stats` text colors
- Review `.copied-flash` green color for light bg contrast
- **Complexity:** Low

---

# Risks / Open questions
- **Risk:** Some status badge background colors (especially yellow/unknown) may be hard to read on white — will need manual contrast tuning
- **Risk:** The multiselect dropdown shadow (`rgba(0,0,0,.5)`) is very dark for a light theme — needs to be softened
- **Open question:** Should we keep a dark mode toggle for users who prefer dark, or fully commit to light-only? (Plan assumes light-only per request)

---

# Non-goals
- No backend (`app.py`) changes
- No JavaScript logic changes — only CSS/styling
- No dark/light theme toggle or system preference detection
- No layout restructuring or new UI components
