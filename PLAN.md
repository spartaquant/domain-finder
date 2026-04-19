# Goal
Improve the visual design and UX polish of the Domain Finder app — better hierarchy, spacing, micro-interactions, and overall feel — without changing any backend logic.

---

# Approach

The entire UI lives in a single file: `static/index.html` with inline `<style>` and `<script>`. We'll keep this architecture but significantly upgrade the CSS and add small HTML/JS tweaks for better UX.

**Key design pillars:** (1) Clearer visual hierarchy with better section spacing and typography, (2) Subtle glassmorphism and depth via layered backgrounds, (3) Smooth micro-interactions (transitions, hover states, skeleton loading), (4) Collapsible keyword section so the 100+ tags don't dominate the page, (5) Improved table readability with alternating row tints and sticky header, (6) Better mobile layout.

> No backend changes. No new dependencies. Everything stays in the single HTML file.

---

# Architecture

```diagram
static/index.html (single file)
├── <style>
│   ├── CSS custom properties (updated palette + new vars)
│   ├── Layout & typography (refined)
│   ├── Glassmorphism card styles
│   ├── Keyword section (collapsible + scroll)
│   ├── Progress bar (animated gradient)
│   ├── Table (sticky header, zebra rows, better density)
│   ├── Filter bar (unified row, cleaner chips)
│   ├── Animations (@keyframes for transitions)
│   └── Responsive breakpoints (improved)
├── <body> HTML (minor structural tweaks)
└── <script> JS (toggle logic for collapsible keywords, no functional changes)
```

---

# Tasks

### Phase 1: Color palette, typography, and base styles
- Refine CSS custom properties: add `--surface3` for deeper layering, soften `--border` slightly, add `--glow` for accent shadows
- Add subtle body background gradient or noise texture (CSS only, no images)
- Increase base font size slightly for readability; tighten heading weights
- Add smooth `transition` defaults to interactive elements
- **Complexity:** Low

### Phase 2: Header and branding upgrade
- Make the logo icon larger with a subtle box-shadow glow
- Add a thin gradient accent line below the header
- Add a brief subtitle/tagline ("Generate .com combinations and check availability")
- **Complexity:** Low

### Phase 3: Keyword section — collapsible and scrollable
- Add a collapse/expand toggle button to the keywords card (default collapsed, showing count badge)
- When expanded, limit keyword area to `max-height: 200px` with `overflow-y: auto` and a fade-out mask at the bottom
- Add a subtle entrance animation for keyword tags
- Style the input row with an integrated "Add" button (input group pattern)
- **Complexity:** Medium

### Phase 4: Action bar and progress redesign
- Group the "Generate & Check" button more prominently — larger, with a glow effect on hover
- Restyle the progress bar: taller track, animated shimmer on the fill, pulse animation while active
- Add a summary stats row below progress with icon badges (checkmark for available, X for registered)
- **Complexity:** Medium

### Phase 5: Filter bar consolidation and results table polish
- Combine status filters, search input, and keyword filter into a single well-organized toolbar with clear visual grouping
- Add sticky `thead` so column headers stay visible when scrolling
- Add alternating row backgrounds (`nth-child` zebra striping)
- Improve status badges with slightly larger pills and subtle left-border color accent on rows
- Widen the score bar visualization; add a numeric label inside the bar when space allows
- Make "Copy" and register action buttons slightly larger touch targets
- **Complexity:** Medium

### Phase 6: Animations, transitions, and final polish
- Add `@keyframes` for: progress bar shimmer, card fade-in on results load, row entrance stagger
- Add `backdrop-filter: blur()` to the card backgrounds for glassmorphism depth (with fallback)
- Add a scroll-to-top button when table is long
- Improve empty state with a simple SVG illustration or larger icon
- Test and fix mobile layout (stacked filters, full-width table scroll, touch-friendly tap targets)
- Add `<meta name="theme-color">` for mobile browser chrome
- **Complexity:** Medium

---

# Risks / Open questions
- **Risk:** `backdrop-filter` (glassmorphism) has spotty support on older browsers — will include a solid-color fallback
- **Risk:** Collapsing keywords by default might confuse users who expect to see them — mitigated by showing keyword count badge and obvious expand button
- **Open question:** Should the keyword section default to collapsed or expanded? Plan assumes collapsed since 100+ tags are overwhelming, but can adjust

---

# Non-goals
- No backend or WebSocket protocol changes
- No splitting the file into separate CSS/JS files
- No adding external libraries (Tailwind, React, etc.)
- No changes to domain scoring logic or RDAP checking behavior
