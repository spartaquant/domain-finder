# Goal
Add a magenta theme to the Domain Finder app alongside the existing dark and light themes, with a three-way theme toggle.

---

# Approach

The app uses CSS custom properties scoped to `data-theme` attributes on `<html>`. Currently there are two themes: **dark** (`:root` defaults) and **light** (`[data-theme="light"]`). The toggle button cycles between them with sun/moon SVG icons.

**Add a `[data-theme="magenta"]` CSS variable block** with a deep magenta-tinted dark palette: dark plum/purple backgrounds, magenta/fuchsia accents, and pink-tinted UI elements. This gives the theme a distinct identity rather than just recoloring the accent.

**Update the toggle to cycle through three themes** (dark → light → magenta → dark). Replace the two-icon toggle with a three-state cycle, showing an appropriate icon for each theme — sun for dark (click to go light), moon for light (click to go magenta), and a sparkle/star icon for magenta (click to go dark).

> All changes are confined to `static/index.html` — no backend changes needed.

---

# Architecture

```diagram
static/index.html
├── <style>
│   ├── :root { ... }              ← dark theme (existing)
│   ├── [data-theme="light"] { }   ← light theme (existing)
│   └── [data-theme="magenta"] { } ← NEW magenta theme
│
├── <header>
│   └── theme-toggle button        ← UPDATE: 3-icon cycle
│
└── <script>
    ├── toggleTheme()              ← UPDATE: dark→light→magenta→dark
    ├── updateThemeIcon()          ← UPDATE: show correct icon for 3 states
    └── IIFE theme loader          ← UPDATE: handle 'magenta' value
```

---

# Tasks

### Phase 1: Add magenta CSS theme variables
- Add `[data-theme="magenta"]` CSS block after the light theme block (~line 66 in `index.html`)
- Color palette: deep plum backgrounds (`#1a0a1e`, `#240e2a`, `#2e1436`), magenta borders (`#4a1942`), magenta accent (`#e040a0`, `#f472b6`), keep green/red/yellow status colors readable against the dark background
- Define all the same CSS variables as the other themes: `--bg`, `--surface`, `--surface2`, `--border`, `--text`, `--muted`, `--accent`, `--accent-glow`, `--green`, `--green-bg`, `--red`, `--red-bg`, `--yellow`, `--yellow-bg`, `--row-border`, `--row-hover`, `--dropdown-shadow`, `--ms-tag-bg`, `--ms-tag-border`, `--ms-highlight`, `--kw-match-bg`, `--kw-match-shadow`, `--register-bg`, `--register-border`, `--register-hover-bg`
- Update the logo and progress bar gradients: currently `linear-gradient(135deg, var(--accent), #a855f7)` — this works naturally since we change `--accent`, but consider whether the purple endpoint should also adapt via a CSS variable
- **Complexity:** Low

### Phase 2: Add third SVG icon for magenta theme
- Add a new SVG icon (sparkle/diamond shape) with `id="themeIconMagenta"` alongside the existing sun and moon icons in the header button (~line 364)
- Initially hidden via `style="display:none"`, same pattern as the moon icon
- **Complexity:** Low

### Phase 3: Update JavaScript theme cycling logic
- Update `toggleTheme()` (~line 984) to cycle: `dark → light → magenta → dark`
- Update `updateThemeIcon()` (~line 978) to show the correct icon for the current theme:
  - Dark: show sun icon (click to go to light)
  - Light: show moon icon (click to go to magenta)
  - Magenta: show sparkle icon (click to go to dark)
- Update the theme tooltip on the button to reflect the next theme
- Update the inline IIFE at line 351 to accept `'magenta'` as a valid stored value
- **Complexity:** Low

---

# Risks / Open questions
- **Risk:** The magenta palette may clash with the fixed status colors (green for available, red for registered, yellow for unknown). These should be tested visually to ensure sufficient contrast on the magenta backgrounds.
- **Open question:** The exact magenta shade — a deeper plum-based dark theme vs. a brighter hot-pink theme. Plan assumes a dark-base with magenta accents for best readability.

---

# Non-goals
- Not adding a theme picker dropdown or settings panel — keeping the single toggle button
- Not refactoring CSS into separate files or adding a CSS preprocessor
- Not changing the backend or adding any new endpoints
- Not adding theme transition animations beyond what already exists
