# m3-custom-theme: reference

## 1. What the theme is

m3-custom-theme is a full Material 3 (M3) and M3 Expressive theme for Anvil, built on Anvil's official M3 theme (`anvil-works/material-3-theme`, version v1.2.6). The theme:

- keeps everything Anvil's theme does;
- adds the M3 components Anvil's theme is missing;
- adds M3 Expressive components, shapes, typography and motion;
- has eight colour palettes, each in light and dark;
- is an Anvil dependency app that other apps (for example `mb-3-cs-app1`) depend on.

This document says how the theme is built and maintained. How an app uses the theme is in `docs/usage-guide.md`. Each component's specification is in `docs/components/`.

The theme lives in two repos: `m3-custom-theme` (the Anvil app) and `m3-custom-theme-project-library` (this document, the usage guide, the component specifications, the record of edits to base files and the build tools).

## 2. Resources

| Resource | Used for |
|---|---|
| https://github.com/anvil-works/material-3-theme | The base. Source of components, layouts, `theme.css` and the colour scheme. MIT licensed. Tags up to v1.2.6 exist. |
| https://github.com/androidx/androidx/tree/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens | Token values. Google's Jetpack Compose Material 3 token files, the code form of the M3 specification: `TypeScaleTokens`, `TypefaceTokens`, `ShapeTokens`, `StateTokens`, `MotionTokens`, `StandardMotionTokens`, `ExpressiveMotionTokens`, `ColorLightTokens`, `ColorDarkTokens`. |
| https://github.com/material-foundation/material-theme-builder | The tool and documentation for generating light and dark colour schemes from a source colour and exporting them. |
| https://m3.material.io/ | The specification for component anatomy, variants, states, motion, adaptive layout and M3 Expressive. The source of truth. |

## 3. Fixed decisions

1. **Package name stays `m3`.** Apps switch from Anvil's theme to ours by changing the dependency, with no code changes. The theme replaces Anvil's theme in an app. It is never used alongside it.
2. **New code uses the prefix `m3x`**: CSS classes `m3x-*`, CSS variables `--m3x-*`, Roles `m3x-*`, Python helper modules `m3x_*`. Inherited `anvil-m3-*` names are left as they are.
3. **Upstream is tracked through a git remote named `upstream`**, with tag fetching switched off after the baseline is set. This stops upstream tags from colliding with the theme's tags.
4. **One version, `v2.0.0`.** The tag `v2.0.0` sits on the released commit, a version line clearly separate from upstream's `v1.x`. Every release moves the tag to the new commit, so every app that depends on `v2.0.0` has the current theme.
5. **Branches**: `master` is the working branch and is always releasable, because the Anvil editor reads and commits to `master` only. All work is committed to `master`. Only upstream merges use their own branch, `upstream-sync`. After any edit made in the Anvil editor, run `git pull` before the next commit.
6. **Licence**: keep Anvil's MIT notice in `LICENSE` and add the theme's own copyright line beneath it.
7. **JavaScript policy.** Anvil supports JavaScript (script tags in `head_html`, files in theme assets, and the `anvil.js` bridge from Python), and the base already ships a JavaScript library this way (floating-ui). It is used only where CSS and Python cannot do the job. Any JavaScript file is vendored into `theme/assets/m3x/js/`, version-pinned, and loaded through `head_html` in `anvil.yaml`. No JavaScript is loaded from a CDN at runtime. The base theme loads its fonts from Google Fonts, and that stays as it is until a separate decision is made. The theme never loads or replaces the jQuery or Bootstrap that Anvil already provides.
8. **Springs are reproduced with the CSS `linear()` easing.** `tools/spring_to_linear.py` solves each spring token (mass 1, stiffness and damping ratio) and writes its curve, 32 points, and its settling time (within 0.1 % of the target) into a generated block in `tokens.css`. Components use six alias tokens (`--m3x-motion-spatial-*` and `--m3x-motion-effects-*`, each fast, default or slow), which point at the expressive springs by default, at the standard springs when `m3x_motion.set_scheme("standard")` is called, and at the standard cubic-bezier easings in browsers without `linear()`. Python animations use the same springs through `m3x_motion.animate`.

## 4. Colours

- **Eight palettes**: `default`, `professional_blue`, `warm_coral`, `calm_teal`, `sophisticated_purple`, `sky_blue`, `forest_green` and `desert_rose`. Each has a light and a dark scheme, 16 in all. `default` keeps the base theme's own colours; its dark scheme is the published M3 baseline dark scheme. Each of the other seven is the Material 3 Content scheme built from three source colours (main, second and accent). The Content scheme keeps the main source colour as Primary Container and gives every colour family strong colour, so these palettes stay vivid; only the backgrounds are near-neutral. Material's colour algorithm sets every light and dark shade from the source colours. The palette colours are fixed.
- **`tools/build_palettes.py`** (library repo) holds the source colours and writes three files in the app repo: `theme/assets/m3x/palettes.css` (the colours of every palette, light and dark), `theme/parameters.yaml` (Anvil's colour list and the 16 colour presets in Anvil's Theme editor, one per palette and mode) and `client_code/_utils/m3x_presets.py` (which preset belongs to which palette and mode). Anvil's colour list holds `professional_blue` light, so a new app starts on that palette. The build checks every text and control colour against every background to the WCAG AA minimum (4.5:1 for text, 3:1 for outlines) and stops on any failure. The three files are never edited by hand.
- Every colour in the theme's CSS goes through a variable (`--anvil-m3-*` for the base colours, `--m3x-color-*` for the colour roles the base lacks), so palette and mode can change while the app runs.
- **Two attributes on the page's root element** choose the colours: `data-m3x-palette` (a palette name; absent means the colours of the preset chosen in Anvil's Theme editor) and `data-m3x-theme` (`light`, `dark` or `system`; absent means light). Following the device's dark setting is opt-in (`system`), so an app never changes appearance unexpectedly.
- **`client_code/_utils/m3x_theming.py`** sets and remembers them from Python (`set_palette`, `set_mode`, `get_palette`, `get_mode`, `is_dark`, `editor_preset`, `apply_saved`). The preset chosen in Anvil's Theme editor is the app's starting palette and mode. A choice made through `set_palette` or `set_mode` is remembered in the browser and wins over the preset. Setting a mode always sets a palette too, because the dark colours belong to a palette. A multi-client app sets them once at start-up from the client's own setting.
- All other token values (typography, shape, elevation, state layers, motion and spacing) are in `theme/assets/m3x/tokens.css`, taken from the Jetpack Compose Material 3 token files.

## 5. Maintenance

The demo form `Form1` shows every component in every variant and state, with Palette and Mode controls at the top for all 16 combinations. It is built in code from one data table (`SECTIONS` in `client_code/Form1/__init__.py`), so it is changed only by file, never in the Anvil design view. Every check below runs in `Form1`.

### 5.1 Adding a component

1. Read the component's page on m3.material.io. Record its anatomy, variants and states in `docs/components/<ComponentName>.md`.
2. Define the API: property names, defaults, events. Use the same names that related components use.
3. Create `client_code/_Components/<ComponentName>/` with `__init__.py` and `form_template.yaml`, following the pattern of an existing component such as `Button`.
4. Create `theme/assets/m3x/<componentname>.css` and import it from `theme/assets/m3x/components.css`. Component tokens (`--m3x-<componentname>-*`) go in `tokens.css`.
5. Export the component in `client_code/components/__init__.py`.
6. Add a toolbox entry in `anvil.yaml` and its icons in `theme/assets/designer_icons/`.
7. Add the component, in every variant and state, to the demo form.
8. Run the Section 6.9 checks. Fix every failure.
9. Commit to `master`.

### 5.2 Upstream releases

At each upstream release, fetch the `upstream` remote, merge into `upstream-sync`, resolve conflicts using the record in `docs/upstream-edits.md`, run the demo form, then merge into `master`.

### 5.3 Lessons

`docs/lessons.md` lists the problems met while building the theme, their causes and the rule each one produced. Read it before any change to the theme.

## 6. Rules

### 6.1 Specification

- m3.material.io is the source of truth for anatomy, variants, states and behaviour.
- Where Anvil's base differs from the M3 spec, the spec wins for new components. Existing components are not changed for this reason alone (see 6.3).
- Every component gets its own `docs/components/<ComponentName>.md` before code is written.
- m3.material.io is rendered by JavaScript and cannot be read automatically. Component specs are taken from pasted text of the site's pages and from the per-component docs in `docs/components/` of `github.com/material-components/material-components-android`, which follow the same spec.

### 6.2 Tokens

- Every colour, size, radius, font, shadow and animation value in new CSS comes from a `--m3x-*` variable. Hardcoded values are not allowed in component CSS.
- Tokens are semantic (`primary`, `on-primary`, `surface`, `outline`), never raw hex values, outside `tokens.css` and the dark block.
- Light and dark values are defined together for every palette. A token with only one scheme is incomplete.
- Colour values come from `tools/build_palettes.py`. All other token values come from the Jetpack Compose Material 3 token files (Section 2). `tokens.css` records each source file, its version and the date it was read.

### 6.3 Upstream files

- The base files stay as they are unless a change is needed. Prefer extending or adding a variant in a new file.
- Every edit to a base file is marked in the file with a `/* m3x: reason */` comment (or `# m3x: reason` in Python) and logged in `docs/upstream-edits.md` with the file name and the reason. This is what makes upstream merges manageable (Section 5.2).
- Do not reformat or reorder base files. Formatting changes create merge conflicts.
- Never edit the theme's own files through the Anvil editor. That means everything under `_Components`, `Layouts`, `_utils` and `theme`. The editor commits straight to `master` and writes the change into the base file (this happened once with a tooltip on `RadioButton`). Theme files are changed only in the repo files, by commit. The editor is used to run and look at `Form1`.

### 6.4 Component construction

- One folder per component under `client_code/_Components/`, named in PascalCase.
- Build properties with the helpers in `client_code/_utils/properties.py` rather than writing new property code.
- Every component exposes designer support: properties in the Anvil designer, a toolbox entry, and light and dark toolbox icons.
- Related components use the same property names (`enabled`, `role`, `icon`, `text`, `align`, and so on) and the same event names.
- Optional features are properties on one component, not separate duplicate components.
- Prefer composition over deep nesting of custom components.
- Every component works with no custom CSS from the consuming app.
- Implement every state that applies: default, hover, focus, pressed, selected, disabled, loading, error.
- A disabled component must not raise events.

### 6.5 CSS

- Each component's CSS lives in its own file under `theme/assets/m3x/`. `theme.css` contains only `@import` lines, the variable blocks and the page-level base styles.
- Every selector begins with `.m3x-`, or with `.anvil-role-m3x-` where an m3x Role styles an Anvil element (Anvil names a Role's class `anvil-role-<role>`). No bare element selectors and no selectors that match existing Anvil classes alone.
- Avoid `!important`. If an existing Anvil rule can only be beaten with `!important`, add a comment saying which rule and why.
- Do not add global rules that change how existing components look.
- Do not use fixed pixel widths for layout. Use relative units and the width classes in 6.7.
- A component whose shadow, focus ring or touch target reaches outside its box has the outer margin `var(--m3x-component-outer-margin-block) var(--m3x-component-outer-margin-inline)` (8 px above and below, 4 px at the sides). A component with a shadow of level 3 or higher uses `var(--m3x-component-outer-margin-elevated)` (16 px) instead. Anvil's containers (FlowPanel, ColumnPanel) cut off anything outside a component's margin box, and content that reaches outside makes the container scroll.
- Use Anvil's `%color:...%` tokens where Anvil needs them, and `--m3x-*` variables everywhere else.
- Test the CSS in light and dark before merging.

### 6.6 Motion

- Motion communicates state, hierarchy or cause and effect. It is not decoration.
- All durations, easings and springs come from the motion tokens in `tokens.css`. Standard transitions are roughly 150–300 ms. Expressive transitions follow the spring tokens, and their settling time is set by the spec, not by that range.
- Animate only `transform`, `opacity`, colour and shadow where possible.
- Honour `@media (prefers-reduced-motion: reduce)` in every animated rule.
- Animation must never block clicks or delay events.
- Shape morphing is used only where it clarifies a state change.
- Motion code lives in `m3x_motion.py` and CSS. JavaScript follows decision 7 in Section 3.

### 6.7 Layout

- Design for the three M3 width classes: compact, medium and expanded.
- Build on the existing navigation layouts. Do not rewrite them.
- Touch targets meet the M3 minimum size.
- Spacing and alignment follow the spacing tokens.
- Layouts must work on small laptops, tablets and phones.

### 6.8 Python

- The Python code follows the base's `.ruff.toml`: `E`, `F` and `I001` checks, import order with `anvil` as third-party, and quote style preserved.
- Modular helpers, one purpose per file: `m3x_motion.py`, `m3x_loading.py`, `m3x_snackbar.py`, `m3x_theming.py`.
- Components do not import each other's internals. Shared code goes in `client_code/_utils/`.

### 6.9 Testing (before every commit to `master`)

1. The component appears in the demo form in every variant and state.
2. It looks correct in light and dark.
3. It works at compact, medium and expanded widths.
4. It is usable by keyboard, with a visible focus state.
5. Contrast is sufficient for text and icons. Colour is not the only status signal.
6. Icon-only controls have labels.
7. Python events fire correctly, including loading and error states.
8. The component works inside a real Anvil page, not only in the demo form.
9. Existing components in the demo form are unchanged (regression check).

### 6.10 Documentation and release

- Every new Role, component, property, event and CSS class is documented before merge.
- Keep `CHANGELOG.md` in the same format as the base's, with an entry per release.
- Versioning is semantic: `v2.0.0`, `v2.1.0`, `v3.0.0`. A breaking change to a component's API requires a major version bump.
- The release checklist: every demo-form check passes, `CHANGELOG.md` is updated, `docs/upstream-edits.md` is current, the version is published in Anvil and the same commit is tagged in git.
- No version is published until the demo form passes every check in 5.9.
