# Fork and extend Anvil’s theme to create A full, general-purpose M3/M3 Expressive theme

## Resources:

- https://github.com/anvil-works/material-3-theme

- https://github.com/material-foundation/material-tokens

- https://github.com/material-foundation/material-theme-builder

- [https://m3.material.io/](https://m3.material.io/)

Use **m3.material.io** as the primary specification for components, variants, motion, adaptive layouts, and M3 Expressive.

## Workflow

1. **Fork and import the theme**  
   Fork `anvil-works/material-3-theme`, then import it into Anvil as your working M3 theme app.
2. **Study its structure**  
   Review its components, layouts, Roles, `theme.css`, colour schemes, and dependency setup.
3. **Create a development branch/version**  
   Keep the original working version intact; develop M3 Expressive additions separately.
4. **Build the token layer**  
   Use `material-tokens` and Material Theme Builder to define light/dark colour, typography, shape, elevation, state, and motion tokens; map them into Anvil Roles and `theme.css`.
5. **Extend foundations**  
   Add expressive typography, expanded shapes, surface-container levels, state layers, and motion tokens.
6. **Complete missing M3 components**  
   Add components missing from Anvil’s theme, using the relevant `m3.material.io` component spec.
7. **Add M3 Expressive components**  
   Start with buttons, FABs, cards, button groups, expressive lists, navigation, progress, and snackbars.
8. **Add motion**  
   Implement hover, press, focus, selection, loading, and shape-morph transitions.
9. **Add adaptive layouts**  
   Extend or create layouts for compact, medium, and expanded screen sizes.
10. **Test each component**  
    Check light/dark themes, states, accessibility, responsiveness, and Python event handling.
11. **Publish versions**  
    Tag stable releases, then use the published version in your apps.
12. **Maintain against upstream**  
    Periodically compare with Anvil’s official theme and merge useful updates.

## Rules and Critical Guidelines

### Design rules

- Follow `m3.material.io` as the source of truth for component anatomy, variants, states, and behaviour.
- Use M3 tokens rather than hardcoded colours, sizes, radii, fonts, shadows, or animation values.
- Support both light and dark themes from the start.
- Use semantic roles—such as `primary`, `on-primary`, `surface`, and `outline`—not raw hex values.
- Keep one clear primary action per screen or component group.
- Use expressive styling sparingly: one dominant expressive element per screen.
- Preserve clear visual hierarchy: headline, supporting text, action, supporting content.
- Do not sacrifice readability or contrast for decoration.

### Component rules

- Build each component against its official M3 spec page.
- Implement all normal states: default, hover, focus, pressed, selected, disabled, loading, and error where applicable.
- Keep component APIs simple and predictable.
- Use consistent property names across related components.
- Prefer composition over deeply nested custom components.
- Do not modify existing Anvil M3 components unless necessary; extend or create variants instead.
- Keep every component usable without custom CSS.
- Make optional features optional through properties, not separate duplicate components.

### Code rules

- Keep theme CSS in `theme.css`.
- Use Anvil Roles for reusable styling.
- Prefix all new Roles and CSS classes, for example `x-` or `m3x-`, to avoid collisions.
- Use Anvil colour tokens such as `%color:Primary%` wherever possible.
- Keep Python client code modular: separate helpers for motion, loading, snackbars, and theming.
- Avoid global CSS that unintentionally affects existing Anvil components.
- Test CSS in both light and dark schemes.
- Avoid `!important` unless overriding a specific existing Anvil style.
- Keep custom JavaScript minimal and isolated.

### Motion rules

- Use motion to communicate state, hierarchy, and cause-and-effect—not decoration.
- Keep durations short: roughly 150–300 ms for most interactions.
- Use consistent easing curves across similar interactions.
- Animate only transform, opacity, colour, and shadow where possible.
- Respect reduced-motion preferences.
- Ensure animations do not block clicks or make the UI feel slow.
- Use shape morphing only where it clarifies a state change.

### Layout rules

- Design for compact, medium, and expanded widths.
- Use Anvil’s M3 navigation layouts as the base where possible.
- Preserve adequate touch-target sizes.
- Maintain consistent spacing and alignment.
- Avoid fixed pixel widths for main content.
- Ensure layouts work on small laptops, tablets, and phones.
- Keep navigation predictable across pages.

### Accessibility rules

- Maintain sufficient colour contrast for text and icons.
- Ensure visible keyboard focus states.
- Keep interactive elements reachable by keyboard.
- Use meaningful labels for icons and icon-only buttons.
- Do not rely on colour alone to communicate status.
- Test with screen readers where practical.
- Ensure disabled components are clearly distinguishable.

### Dependency rules

- Keep the theme app’s package name stable.
- Use semantic versioning: `v1.0.0`, `v1.1.0`, `v2.0.0`.
- Publish stable versions before using the theme in production apps.
- Do not make breaking changes to existing component APIs without a major version bump.
- Document every new Role, component, property, event, and CSS class.
- Keep a changelog.
- Periodically compare your fork with Anvil’s upstream theme and merge useful fixes.

### Testing rules

- Test every new component in isolation first.
- Then test it inside a real Anvil page.
- Test light mode, dark mode, mobile widths, and keyboard navigation.
- Test all interactive states.
- Test Python event handlers and loading states.
- Create a demo page containing every component and variant.
- Do not publish a version until the demo page passes your checks.
