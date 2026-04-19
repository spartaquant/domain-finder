# Goal
Add a light theme to the Domain Finder app with a toggle to switch between dark and light modes, persisting the user's preference.

---

# Approach
The app already uses CSS custom properties (`:root` variables) for all colors — `--bg`, `--surface`, `--border`, `--text`, `--muted`, etc. This is the ideal setup for theming.

**Strategy:** Define a `[data-theme="light"]` attribute selector that overrides every CSS variable with light-mode equivalents. Add a theme toggle button in the header. Persist the choice in `localStorage` and respect the user's OS preference (`prefers-color-scheme`) as the default.

All changes are confined to `static/index.html` — no backend changes needed. The toggle will be a small sun/moon icon button in the header area.

---

# Architecture

```diagram
static/index.html
├── <style>
│   ├── :root { --bg: #0b0f1a; ... }          (existing dark vars)
│   └── [data-theme="light"] { --bg: #f8f9fb; ... }  (NEW light vars)
├── <header>
│   └── [Theme Toggle Button]                  (NEW)
└── <script>
    └── Theme init + toggle logic              (NEW)
        ├── Read localStorage / prefers-color-scheme
        ├── Set data-theme on <html>
        └── Persist choice to localStorage
```

---

# Tasks

### Phase 1: Light theme CSS variables and toggle
- Add `[data-theme="light"]` CSS block overriding all color variables with a clean light palette:
  - `--bg: #f8f9fb` (near-white background)
  - `--surface: #ffffff` (white cards)
  - `--surface2: #f0f2f5` (subtle gray for inputs/chips)
  - `--border: #d1d5db` (light gray borders)
  - `--text: #1a1a2e` (near-black text)
  - `--muted: #6b7280` (medium gray for secondary text)
  - `--accent: #4f46e5` (slightly deeper indigo for contrast on white)
  - `--accent-glow: #6366f1`
  - Adjust status color backgrounds for better contrast on white (`--green-bg`, `--red-bg`, `--yellow-bg` with higher opacity)
- Fix any hardcoded colors that bypass CSS variables:
  - `tbody tr` hover uses hardcoded `rgba(99,102,241,.05)` — make it use a variable or keep it (works on both themes)
  - `tbody tr` border uses hardcoded `rgba(30,45,69,.5)` — adjust for light theme
  - `.ms-dropdown` shadow uses `rgba(0,0,0,.5)` — reduce for light theme
  - `.ms-tag` uses hardcoded `rgba(99,102,241,.15)` — keep as-is (works on both)
- Add a theme toggle button (sun/moon SVG icon) in the header, styled to match the existing UI
- Add JS logic: read `localStorage.getItem("theme")`, fall back to `prefers-color-scheme: dark`, set `document.documentElement.dataset.theme`, toggle on click, persist to `localStorage`
- Update the toggle icon to reflect current state (sun for dark mode, moon for light mode)
- **Complexity:** Medium

---

# Risks / Open questions
- **Risk:** Some hardcoded `rgba()` values in hover states and shadows may look wrong on the light background — these will need manual adjustment in the light variable block or via additional selectors.
- **Open question:** The logo gradient (`linear-gradient(135deg, var(--accent), #a855f7)`) and progress bar gradient use a hardcoded purple — these work fine on both themes but could be adjusted if desired.

---

# Non-goals
- No changes to the Python backend — theming is purely client-side
- No separate CSS file — keeping the single-file architecture
- No auto-switching based on time of day — only OS preference and manual toggle
- No theme customization beyond dark/light (no custom color picker)
