# Lessons learned

Mistakes and discoveries from building the theme. Read before each step. Add an entry whenever something costs us a test round.

| # | Situation | Cause | Rule |
|---|---|---|---|
| 1 | `RadioButton` raised "group must be a RadioGroup object" | The `group` property takes a group object, not a name. | Put `RadioButton` components inside a `RadioGroupPanel`. Never pass `group`. |
| 2 | A tooltip typed in the Anvil editor changed every radio button | The editor was open on the theme's own `RadioButton` component, not on `Form1`, and wrote the change into the base file. | Never edit files under `_Components`, `Layouts`, `_utils` or `theme` in the Anvil editor. Theme changes are made in the repo files and committed. |
| 3 | The editor commits to `master` on its own | The editor follows `master` only. | All work is committed to `master`. `gcp` pulls before it pushes. |
| 4 | A dropdown showed no list | The test was clicked in the design panel. Dropdown and menu lists are hidden in the design view by design. | Test menus and dropdowns in the running panel (right side of the split view). |
| 5 | A dropdown had one long item | The Items box takes one item per line, not commas. | Type each item on its own line. |
| 6 | The same dropdown looked taller or wider in two places | A column panel stretches its content across the full width. A flow panel sizes it to its content. | Use a flow panel for compact components. |
| 7 | Property mistakes reached the editor | Names were checked but not value types. | Every file is checked for property names, option values and value types before it is handed over. The check cannot run Anvil itself. |
| 8 | `material-3-theme-master.zip` differs from v1.2.6 | The zip is a newer copy of upstream's main branch. | Use the git tag `upstream-v1.2.6` as the reference, never the zip. |
| 9 | `Form1` cannot be edited in the design view | It is built in code. | `Form1` is changed only by file. |
| 10 | A file was handed over without a destination | Process slip. | Every hand-off names the file and the exact folder. |
| 11 | Dark mode and palettes could not reach part of the theme | `theme.css` used `%color:...%` tokens directly in 55 places, bypassing the colour variables. | Theme CSS uses `var(--anvil-m3-...)` for every colour. A `%color:` token is allowed only inside the `:root` block. |
| 12 | A regex replace missed names containing digits | The pattern for colour names had no digits, so `Primary Overlay 2` was skipped. | After any bulk replace, count what is left and list it. Never assume the replace was complete. |
| 13 | An Excel lock file (`~$...xlsx`) was committed to the library repo | Excel creates it while the file is open, and `git add -A` picked it up. | The library repo ignores `~$*`. Close Excel before committing. |
| 14 | The colour library's default scheme did not match the base theme | It follows a newer Material specification. | Pass `spec_version="2021"`, and always compare generated colours with the known values before trusting them. |
| 15 | The Anvil editor rewrote the Dialog's `form_template.yaml` | When a component is placed in the design view, the editor saves its `form_template.yaml` in its own layout (the `html` on one line, in single quotes). The content was unchanged. | Write every new `form_template.yaml` in the editor's layout: `properties: {html: '...'}` on one line. |
| 16 | A test list could not be followed | Steps were written as short labels ("Basic: click Basic. Pass: ..."), so it was unclear what was a place, a control, an action or a result. | Every test step is a full sentence. Each step names where to look (section and heading), the exact control, the action, and what must be seen. Steps that check a result start with "Check that". One action per step, numbered in order. |
| 17 | Chip shadows were cut off and the filter chip row was cut off at the top | Anvil's FlowPanel and ColumnPanel set `overflow-x: hidden`, which also makes them cut off and scroll vertically. The chip's 48 px touch target and its shadow reached outside the chip, so the row became scrollable and scrolled when a chip was clicked. | Every component whose shadow, focus ring or touch target reaches outside its box gets the outer margin tokens (rule 5.5). Demo samples with deep shadows get padding around them. |
