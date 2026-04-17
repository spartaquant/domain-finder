# Goal
Polish the Domain Finder UI with a stronger visual hierarchy, tighter components, smoother feedback, and better information density on the results table — without rewriting the app structure.

# Approach
The existing dark theme works: indigo/purple accent, slate surfaces, Inter + JetBrains Mono. The problems are density, flatness, and lack of hierarchy. Everything looks like it has the same weight — the primary CTA doesn't pop, the results table is cramped, filters blend into each other, and there's no streaming feedback motion.

The plan is **refinement, not a redesign**. All edits live in `static/index.html` (styles + markup + a small amount of JS for new micro-interactions). No backend changes. No new dependencies beyond what already loads from Google Fonts.

Key moves:
- **Palette & depth:** subtle radial gradient background, softer surface colors, tuned shadows to give cards actual elevation instead of just borders. Replace the flat indigo with a slightly warmer gradient accent.
- **Hero:** replace the tiny letter-"D" logo with an SVG mark, move the keyword management + primary CTA into a single prominent hero card so the first screen has a clear focal point.
- **Results table:** status-colored left border per row, bigger score bar with numeric overlay, zebra-free but tighter row rhythm, row-in fade+slide animation as results stream. Sticky header. Monospace domain column bumped in weight/size.
- **Toolbar:** fuse the status filter, search, keyword multiselect, position filter, and registrar picker into a cohesive toolbar with inline counts on chips (e.g. "Likely Available · 42"). Registrar becomes a compact segmented control.
- **Progress:** add rate (domains/sec) + ETA next to the bar, animate the fill with a shimmer while active.
- **Micro-interactions:** toast-style copy confirmation (absolute-positioned, fades), button hover lift, chip press state, focus rings that match the accent.
- **Responsive:** below 720px the table collapses into stacked cards so the key fields stay legible on mobile.

Non-goals: no framework migration, no new routes, no auth, no theming toggle (staying dark — the palette is what it needs to be).

# Tasks

1. **Palette, typography, and global polish**
   - Tune CSS custom properties: warmer accent gradient, softer muted tones, layered surface colors (`--surface-1`, `--surface-2`, `--surface-raised`).
   - Add a subtle radial gradient body background and a hairline noise / vignette for depth.
   - Increase base font size to 15px, tighten heading weights, ensure consistent letter-spacing on labels.
   - Standardize focus ring (`:focus-visible`) across inputs, buttons, chips.

2. **Header + hero card**
   - Replace the letter-"D" div with an inline SVG logo mark (simple geometric "domain node" icon).
   - Upgrade the `<h1>` lockup with a proper subtitle and a subtle gradient on the wordmark.
   - Merge Keywords card and Actions row into one "hero" card with the primary CTA visually dominant (larger button, gradient fill, animated glow on hover).
   - Move "Recheck unknowns" into a secondary/ghost position beside it.

3. **Results toolbar redesign**
   - Combine search, status filters, keyword multiselect, and position filter into a two-row toolbar with consistent spacing.
   - Add inline counts to each status chip (re-use existing `resultCounters` data).
   - Replace the chip-style registrar picker with a compact segmented control (icons + label), persist selection to localStorage (already done).
   - Keep the toolbar sticky-ish (sticky to top of results card) when the user scrolls the table.

4. **Results table enhancements**
   - Add a 3px status-colored left accent on each row (green / red / amber).
   - Bump domain column typography; shrink non-essential columns.
   - Redesign score cell: wider bar, gradient fill proportional to score, numeric value right-aligned inside the bar lane.
   - Add row-in animation (`opacity` + 4px `translateY`) staggered by a few ms when new items append — cheap CSS keyframe, guarded so re-renders don't re-animate existing rows.
   - Make the full row subtly clickable (hover lift) while keeping actions as distinct buttons.

5. **Progress and feedback micro-interactions**
   - Add rate (items/sec, rolling window) and ETA to the progress stats line.
   - Add a moving shimmer gradient to `.progress-bar-fill` while active; stop when done.
   - Replace inline "✓ Copied" text swap with a small floating toast near the button (fades out in ~1s).
   - Add a "press" transform to chips and buttons for tactile feedback.

6. **Responsive + empty states**
   - Below ~720px, render results as stacked cards (domain + status + score + actions) instead of a horizontally scrolling table.
   - Style the initial "no results yet" state (before first run) with an illustration-lite placeholder inside the hero card.
   - Tighten the empty-filter-results state.

# Risks / Open questions
- **Direction is subjective.** If the user wanted a fundamentally different look (light mode, glassmorphic, brutalist, etc.) this plan won't hit that — it's a polish pass on the current dark/indigo aesthetic. Happy to redo as a light theme, a glass/blurred variant, or a more minimal/monochrome look if asked.
- **Sticky toolbar** can feel heavy if the page is short; will only activate when table exceeds ~8 rows.
- **Row-in animation** must not replay on every throttled re-render. Will track a `_rendered` flag per result row (client-side only, not persisted) so only newly-appended rows animate.
- **Mobile card layout** adds markup but doesn't change backend shape; safe to do in pure CSS + a small template branch.
