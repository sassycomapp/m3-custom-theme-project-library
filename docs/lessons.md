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
