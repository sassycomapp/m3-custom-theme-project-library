# Edits to base (upstream v1.2.6) files

Every change to a file that came from Anvil's theme is listed here, so upstream merges (Step 11) can be resolved. Format: file, change, reason, step.

| File | Change | Reason | Step |
|---|---|---|---|
| `anvil.yaml` | `name` set to `m3-custom-theme`. The startup module `_TestForms.ButtonMenuFUI`, which does not exist in the public repo, was replaced by `startup_form: Form1`. The editor also reformatted one line. | Make the app run. | 1 |
| `.gitignore` | Added `/.anvil/`. | Anvil's local folder. | 1 |
| `.anvil_editor.yaml` | Added ids for `Form1`, `m3x/palettes.css` and `_utils.m3x_theming`. | New files. | 1, 4 |
| `theme/assets/theme.css` | (a) Added `@import '_/theme/m3x/palettes.css';` after the base imports. (b) Added the variable `--anvil-m3-on-background` to the `:root` block. (c) Replaced 55 direct `%color:...%` tokens after the `:root` block with the matching `var(--anvil-m3-...)`. Each replaced token has the identical value in light mode. | Palettes and dark mode must reach the whole theme, including the page background, navigation, modal and data grid. | 4 |

## Known upstream issues, not changed

| Where | Issue | Why left |
|---|---|---|
| `theme/assets/theme.css`, `a.anvil-inlinable` | The rule reads `color: %color:Primary%%;` with a stray `%`, so the colour is invalid and ignored. | Fixing it changes the appearance of inline links in light mode. Decide with the link component in Step 6. |
| `theme/assets/theme.css`, `@property --PrimaryOverlay2` | Registered with a fixed colour but used nowhere. | Dead code. Harmless. |
