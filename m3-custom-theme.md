# Build a full, general-purpose M3 / M3 Expressive theme for Anvil

## 1. Objective

Build a custom Material 3 theme for Anvil, based on Anvil's official M3 theme (`anvil-works/material-3-theme`, version v1.2.6). The theme:

- keeps everything Anvil's theme already does;
- adds the M3 components Anvil's theme is missing;
- adds M3 Expressive components, shapes, typography and motion;
- supports light and dark schemes;
- is published as an Anvil dependency app that our own apps (for example `mb-3-cs-app1`) depend on.

This document covers **how the theme is built**: the workflow (Section 4) and the rules we follow while building it (Section 5). How apps use the finished theme is documented separately, after release.

## 2. Resources and what each is used for

| Resource | Used for |
|---|---|
| https://github.com/anvil-works/material-3-theme | The base. Source of components, layouts, `theme.css` and the colour scheme. MIT licensed. Tags up to v1.2.6 exist. |
| https://github.com/androidx/androidx/tree/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens | Token values. Google's Jetpack Compose Material 3 token files, the code form of the M3 specification: `TypeScaleTokens`, `TypefaceTokens`, `ShapeTokens`, `StateTokens`, `MotionTokens`, `StandardMotionTokens`, `ExpressiveMotionTokens`, `ColorLightTokens`, `ColorDarkTokens`. |
| https://github.com/material-foundation/material-theme-builder | The tool and documentation for generating light and dark colour schemes from a source colour and exporting them. |
| https://m3.material.io/ | The specification for component anatomy, variants, states, motion, adaptive layout and M3 Expressive. The source of truth. |

Local reference copies are in the `m3-custom-theme-project-library` repo: `material-3-theme-master.zip`, `material-theme-builder-main.zip`, and a saved copy of the M3 site page. The two zip files are snapshots of each repo's main branch. `material-3-theme-master.zip` is newer than v1.2.6 and differs from it (for example, it contains a `virtualize` module).

## 3. Starting point and fixed decisions

### 3.1 What exists today (checked 2 Nov 2026)

- The `m3-custom-theme` repo is a **plain Anvil app that depends on Anvil's M3 theme v1.2.6**. It is not yet a fork. Its `theme/assets/theme.css` is empty and it holds one placeholder form, `Form1`.
- Anvil's M3 theme has this structure:
  - `client_code/_Components/` for components (a Python `__init__.py` plus a `form_template.yaml` per component);
  - `client_code/Layouts/` for `NavigationDrawerLayout` and `NavigationRailLayout`;
  - `client_code/_utils/properties.py` for shared property helpers;
  - `client_code/components/__init__.py`, which exports every component for `import m3.components as m3`;
  - `client_code/InitModule.py`, which registers M3 replacements for the standard Anvil components;
  - `theme/assets/theme.css`, which imports the per-component CSS files in `theme/assets/anvil-m3/`;
  - `theme/parameters.yaml`, which holds the colour scheme (about 45 named colours) and the Roles;
  - `anvil.yaml`, which holds the package name `m3`, the toolbox sections, and the font and floating-ui `head_html`.
- Colours reach the CSS as `%color:Primary%`-style tokens, assigned in `theme.css` to variables named `--anvil-m3-*`.
- Gaps we know about: the base has **one colour scheme and no dark-mode mechanism**, it uses `!important` in places, and its component set is smaller than the full M3 list.

### 3.2 Fixed decisions

Change these only by editing this section.

1. **Package name stays `m3`.** Our apps then switch from Anvil's theme to ours by changing the dependency, with no code changes. Our theme replaces Anvil's theme in an app. It is never used alongside it.
2. **New code uses the prefix `m3x`**: CSS classes `m3x-*`, CSS variables `--m3x-*`, Roles `m3x-*`, Python helper modules `m3x_*`. Inherited `anvil-m3-*` names are left as they are.
3. **Upstream is tracked through a git remote named `upstream`**, with tag fetching switched off after the baseline is set. This stops upstream tags from colliding with ours.
4. **Our release tags start at `v2.0.0`**, a version line clearly separate from upstream's `v1.x`. The first release also confirms that Anvil lists our tags as selectable dependency versions.
5. **Branches**: `master` is the working branch and is always releasable, because the Anvil editor reads and commits to `master` only. All work is committed to `master`. Only upstream merges use their own branch, `upstream-sync`. After any edit made in the Anvil editor, run `git pull` before the next commit.
6. **Licence**: keep Anvil's MIT notice in `LICENSE` and add our own copyright line beneath it.
7. **JavaScript policy.** Anvil supports JavaScript (script tags in `head_html`, files in theme assets, and the `anvil.js` bridge from Python), and the base already ships a JavaScript library this way (floating-ui). We use it only where CSS and Python cannot do the job. Any JavaScript file is vendored into `theme/assets/m3x/js/`, version-pinned, and loaded through `head_html` in `anvil.yaml`. No JavaScript is loaded from a CDN at runtime. The base theme loads its fonts from Google Fonts, and that stays as it is until a separate decision is made. We never load or replace the jQuery or Bootstrap that Anvil already provides.

## 4. Build workflow

Each step has an exit check. Do not start the next step until the check passes.

**Step 1. Establish the base.**
Bring upstream v1.2.6 into the `m3-custom-theme` repo on a branch named `step1-base`:
- add the `upstream` remote and fetch the v1.2.6 tag under the local name `upstream-v1.2.6`;
- record it as a merge base with an empty "ours" merge, so later upstream merges have a common ancestor;
- replace the working tree with the v1.2.6 tree;
- remove `LICENSE.txt` (upstream's file is `LICENSE`);
- set `name: m3-custom-theme` in `anvil.yaml`;
- replace the startup module `_TestForms.ButtonMenuFUI`, which does not exist in the public repo, with `startup_form: Form1`;
- keep the placeholder `Form1` as the startup form, and keep its entry in `.anvil_editor.yaml`; Step 3 turns it into the demo form;
- keep `/.anvil/` in `.gitignore`.

The `m3` dependency disappears from `anvil.yaml` by itself, because the app now *is* the `m3` package. The README is upstream's until we rewrite it at Step 10.
*Exit check:* the staged tree differs from the `upstream-v1.2.6` tree in exactly five files (`.anvil_editor.yaml`, `.gitignore`, `anvil.yaml`, `client_code/Form1/__init__.py`, `client_code/Form1/form_template.html`). The app opens in the Anvil editor, `Form1` runs, and the toolbox shows the same components as upstream v1.2.6. Tag the commit `base-v1.2.6`.

**Step 2. Inventory the base.**
Write `docs/base-inventory.md` in the project library repo. Inventory the v1.2.6 tree (tag `upstream-v1.2.6`), not the zip file, which is newer. It lists every component with its properties and events, every layout, every CSS file in `theme/assets/anvil-m3/`, the colour names in `parameters.yaml`, the Roles, and the helpers in `_utils/properties.py`. Then write `docs/gap-list.md`, comparing the inventory against the full component list on m3.material.io. Each gap gets a priority.
*Exit check:* both files exist and every component in the base appears in the inventory.

**Step 3. Build the demo and test app.**
Turn `Form1` into the demo form. It is already the startup form. It shows every existing component in each variant and state, built in Python from one data table (`SECTIONS` in `client_code/Form1/__init__.py`), so adding a component later means adding one entry. Every property name and option value in the table is checked against the component's `form_template.yaml` before the file is delivered.
Step 3 is done in two passes, both now written. Pass 3a covers the components that sit in a simple row: buttons, icon buttons, toggle icon buttons, checkbox, radio buttons (inside a `RadioGroupPanel`), switch, text box, text area, slider, avatar, link, headings, text, cards, progress indicators and dividers. Pass 3b adds `ButtonMenu`, `IconButtonMenu`, `AvatarMenu`, `MenuItem`, `DropdownMenu`, `FileLoader` and `NavigationLink`. The two navigation layouts and `SidesheetContent` cannot sit inside a form, so they get their own demo forms in Step 9, where we change them anyway.
Form1 is only changed by file, never in the Anvil design view. The demo form is built in code, so the design view cannot edit it.
*Exit check:* Form1 runs in the Anvil editor, every section appears, and the console shows no errors. After Step 4 the same form also shows the light/dark switch.

**Step 4. Prove palettes and dark mode.**
Findings from the base files: every component colour already goes through the `--anvil-m3-*` variables, but `theme.css` used `%color:...%` tokens directly in 55 places (navigation, modal, text, data grid, page background). Those could not change at runtime, so each was replaced by the matching variable. The result in light mode is identical. The edit is marked in the file and logged in `docs/upstream-edits.md`.

What was built:
- **Four palettes** (`professional_blue`, `warm_coral`, `calm_teal`, `sophisticated_purple`) from `docs/Anvil-M3 color mapping 4 palette.xlsx`, plus the base theme's own colours as `default`. Each has a light and a dark scheme. The dark schemes are generated with Material's colour algorithm from each palette's key colour. Every light colour in the spreadsheet matched that algorithm within 2 steps, which is why the dark partners can be trusted. The base theme's own dark scheme is the published M3 baseline dark scheme, checked colour by colour against the expected Material tones.
- **`tools/build_palettes.py`** (library repo) reads the spreadsheet and writes three files in the app repo: `theme/assets/m3x/palettes.css` (the colours of every palette, light and dark), `theme/parameters.yaml` (Anvil's colour list and the ten colour presets in Anvil's Theme editor, one per palette and mode) and `client_code/_utils/m3x_presets.py` (which preset belongs to which palette and mode). These files are never edited by hand. To change a colour, change the spreadsheet and rebuild. Corrections made to the spreadsheet's values are listed in `docs/palette-corrections.md`.
- **Two attributes on the page's root element** choose the colours: `data-m3x-palette` (a palette name; absent means the colours of the preset chosen in Anvil's Theme editor) and `data-m3x-theme` (`light`, `dark` or `system`; absent means light). Following the device's dark setting is opt-in (`system`), so an existing app never changes appearance unexpectedly.
- **`client_code/_utils/m3x_theming.py`** sets and remembers them from Python (`set_palette`, `set_mode`, `get_palette`, `get_mode`, `is_dark`, `editor_preset`, `apply_saved`). The preset chosen in Anvil's Theme editor is the app's starting palette and mode. A choice made through `set_palette` or `set_mode` is remembered in the browser and wins over the preset. Setting a mode always sets a palette too, because the dark colours belong to a palette. A multi-client app sets them once at start-up from the client's own setting.
- **`Form1`** has Palette and Mode dropdowns at the top, so every component can be inspected in all 10 combinations (5 palettes, light and dark).

*Exit check:* in each of the 10 combinations, every section of `Form1` is readable and nothing keeps its old colour (page background, text, buttons, text boxes, cards, menus, dropdown lists, progress indicators). Hover and pressed states are visibly correct on filled, tonal and elevated buttons. If a combination fails, the cause is recorded in `docs/lessons.md` before Step 5.

**Step 5. Build the token layer.**
Create `theme/assets/m3x/tokens.css` and import it from `theme.css`. The colour schemes are the palettes from Step 4. The token layer adds every M3 colour role the base lacks (Error Container, Inverse Primary, Surface Tint, Surface Dim, Surface Bright, Surface Container Lowest, Scrim, Shadow, and the Fixed and Fixed Dim roles for primary, secondary and tertiary) to every palette in light and dark, through `tools/build_palettes.py`. Take typography, shape, state-layer, motion and spacing values from the Jetpack Compose Material 3 token files (Section 2). Shadows use the M3 shadow values the base components already use. Spacing follows the M3 4 px grid. The type scale includes the expressive (emphasised) styles, and the shape scale includes the full expanded set of corner sizes. Motion tokens cover both the standard duration-and-easing set and the Expressive spring set (stiffness and damping ratio, with separate spatial and effects specs). The Expressive spatial springs are fast 800 / 0.6, default 380 / 0.8 and slow 200 / 0.8. The effects springs are fast 3800 / 1.0, default 1600 / 1.0 and slow 800 / 1.0. These values agree across the Flutter `motor` package, react-native-paper and other implementations. They are confirmed against Google's Jetpack Compose source before they are frozen.
*Exit check:* every token category has variables, and a token reference page in the demo form shows them all in light and dark and passes the Section 5.9 checks.

**Step 6. Build the missing M3 components.**
Take the gaps from `docs/gap-list.md` in priority order. Use the Component Build Loop (4.1) for each one.

**Step 7. Build the M3 Expressive components.**
Start with buttons and button groups, FABs, cards, expressive lists, navigation, progress indicators and snackbars. Use the Component Build Loop (4.1) for each one.

**Step 8. Add motion.**
Implement hover, press, focus, selection, loading and shape-morph transitions through the motion tokens from Step 5, in the helper module `client_code/_utils/m3x_motion.py` and in CSS. M3 Expressive motion is spring-based, not fixed-duration. The first task is to prove how springs are reproduced, trying these approaches in order and stopping at the first that works in the browsers we target: (1) a CSS `linear()` easing, generated by a small Python script (`tools/spring_to_linear.py` in the library repo) from the closed-form spring equation (mass 1, with stiffness and damping ratio from the tokens), with the animation duration set to the spring's settling time; (2) the Web Animations API, called from `m3x_motion.py` through `anvil.js`; (3) a small vendored JavaScript motion library (decision 7). The chosen approach is recorded in Section 3.2 before the rest of this step. Precedents: the Flutter `motor` package (`MaterialSpringMotion`), react-native-paper's motion tokens, and the web library `tankrap/m3x`, which drives its components with a spring solver of about 1 KB fed by the same tokens.
*Exit check:* the motion rules in Section 5.6 pass, including reduced-motion behaviour.

**Step 9. Add adaptive layouts.**
Extend the existing navigation layouts and add new ones for compact, medium and expanded widths, following the M3 adaptive layout specification.
*Exit check:* each layout works at the three width classes in the demo form.

**Step 10. Release.**
Complete the release checklist in Section 5.10, update `CHANGELOG.md`, publish the version in Anvil and tag the same commit.
*Exit check:* a test app (not a production app) switches its dependency to the new version and works unchanged.

**Step 11. Maintain against upstream.**
At each upstream release, fetch the `upstream` remote, merge into `upstream-sync`, resolve conflicts using the log in `docs/upstream-edits.md`, run the demo form, then merge into `master`.

### 4.1 Component Build Loop (used in Steps 6 and 7)

1. Read the component's page on m3.material.io. Record its anatomy, variants and states in `docs/components/<ComponentName>.md`.
2. Define the API: property names, defaults, events. Use the same names that related components use.
3. Create `client_code/_Components/<ComponentName>/` with `__init__.py` and `form_template.yaml`, following the pattern of an existing component such as `Button`.
4. Create `theme/assets/m3x/<componentname>.css` and import it from `theme/assets/m3x/components.css`. Component tokens (`--m3x-<componentname>-*`) go in `tokens.css`.
5. Export the component in `client_code/components/__init__.py`.
6. Add a toolbox entry in `anvil.yaml` and its icons in `theme/assets/designer_icons/`.
7. Add the component, in every variant and state, to the demo form.
8. Run the Section 5.9 checks. Fix every failure.
9. Commit to `master`.

## 5. Rules for building the theme

### 5.1 Specification

- m3.material.io is the source of truth for anatomy, variants, states and behaviour.
- Where Anvil's base differs from the M3 spec, the spec wins for new components. Existing components are not changed for this reason alone (see 5.3).
- Every component gets its own `docs/components/<ComponentName>.md` before code is written.
- m3.material.io is rendered by JavaScript and cannot be read automatically. Component specs are taken from the saved site pages, from text you paste in, and from the per-component docs in `docs/components/` of `github.com/material-components/material-components-android`, which follow the same spec.

### 5.2 Tokens

- Every colour, size, radius, font, shadow and animation value in new CSS comes from a `--m3x-*` variable. Hardcoded values are not allowed in component CSS.
- Tokens are semantic (`primary`, `on-primary`, `surface`, `outline`), never raw hex values, outside `tokens.css` and the dark block.
- Light and dark values are defined together for every palette. A token with only one scheme is incomplete.
- Colour values come from `tools/build_palettes.py`. All other token values come from the Jetpack Compose Material 3 token files (Section 2). `tokens.css` records each source file, its version and the date it was read.

### 5.3 Upstream files

- The base files stay as they are unless a change is needed. Prefer extending or adding a variant in a new file.
- Every edit to a base file is marked in the file with a `/* m3x: reason */` comment (or `# m3x: reason` in Python) and logged in `docs/upstream-edits.md` with the file name and the reason. This is what makes Step 11 merges manageable.
- Do not reformat or reorder base files. Formatting changes create merge conflicts.
- Never edit the theme's own files through the Anvil editor. That means everything under `_Components`, `Layouts`, `_utils` and `theme`. The editor commits straight to `master` and writes the change into the base file (this happened once with a tooltip on `RadioButton`). Theme files are changed only in the repo files, by commit. The editor is used to run and look at `Form1`.

### 5.4 Component construction

- One folder per component under `client_code/_Components/`, named in PascalCase.
- Build properties with the helpers in `client_code/_utils/properties.py` rather than writing new property code.
- Every component exposes designer support: properties in the Anvil designer, a toolbox entry, and light and dark toolbox icons.
- Related components use the same property names (`enabled`, `role`, `icon`, `text`, `align`, and so on) and the same event names.
- Optional features are properties on one component, not separate duplicate components.
- Prefer composition over deep nesting of custom components.
- Every component works with no custom CSS from the consuming app.
- Implement every state that applies: default, hover, focus, pressed, selected, disabled, loading, error.
- A disabled component must not raise events.

### 5.5 CSS

- Each component's CSS lives in its own file under `theme/assets/m3x/`. `theme.css` contains only `@import` lines, the variable blocks and the page-level base styles.
- Every selector begins with `.m3x-`, or with `.anvil-role-m3x-` where an m3x Role styles an Anvil element (Anvil names a Role's class `anvil-role-<role>`). No bare element selectors and no selectors that match existing Anvil classes alone.
- Avoid `!important`. If an existing Anvil rule can only be beaten with `!important`, add a comment saying which rule and why.
- Do not add global rules that change how existing components look.
- Do not use fixed pixel widths for layout. Use relative units and the width classes in 5.7.
- Use Anvil's `%color:...%` tokens where Anvil needs them, and `--m3x-*` variables everywhere else.
- Test the CSS in light and dark before merging.

### 5.6 Motion

- Motion communicates state, hierarchy or cause and effect. It is not decoration.
- All durations, easings and springs come from the motion tokens (Step 5). Standard transitions are roughly 150–300 ms. Expressive transitions follow the spring tokens, and their settling time is set by the spec, not by that range.
- Animate only `transform`, `opacity`, colour and shadow where possible.
- Honour `@media (prefers-reduced-motion: reduce)` in every animated rule.
- Animation must never block clicks or delay events.
- Shape morphing is used only where it clarifies a state change.
- Motion code lives in `m3x_motion.py` and CSS. JavaScript follows decision 7 in Section 3.2.

### 5.7 Layout

- Design for the three M3 width classes: compact, medium and expanded.
- Build on the existing navigation layouts. Do not rewrite them.
- Touch targets meet the M3 minimum size.
- Spacing and alignment follow the spacing tokens.
- Layouts must work on small laptops, tablets and phones.

### 5.8 Python

- The Python code follows the base's `.ruff.toml`: `E`, `F` and `I001` checks, import order with `anvil` as third-party, and quote style preserved.
- Modular helpers, one purpose per file: `m3x_motion.py`, `m3x_loading.py`, `m3x_snackbar.py`, `m3x_theming.py`.
- Components do not import each other's internals. Shared code goes in `client_code/_utils/`.

### 5.9 Testing (before every commit to `master`)

1. The component appears in the demo form in every variant and state.
2. It looks correct in light and dark.
3. It works at compact, medium and expanded widths.
4. It is usable by keyboard, with a visible focus state.
5. Contrast is sufficient for text and icons. Colour is not the only status signal.
6. Icon-only controls have labels.
7. Python events fire correctly, including loading and error states.
8. The component works inside a real Anvil page, not only in the demo form.
9. Existing components in the demo form are unchanged (regression check).

### 5.10 Documentation, versioning and release

- Every new Role, component, property, event and CSS class is documented before merge.
- Keep `CHANGELOG.md` in the same format as the base's, with an entry per release.
- Versioning is semantic: `v2.0.0`, `v2.1.0`, `v3.0.0`. A breaking change to a component's API requires a major version bump.
- The release checklist: every demo-form check passes, `CHANGELOG.md` is updated, `docs/upstream-edits.md` is current, the version is published in Anvil and the same commit is tagged in git.
- No version is published until the demo form passes every check in 5.9.
