# Motion

Tokens in `theme/assets/m3x/tokens.css`; generator `tools/spring_to_linear.py`; Python helper `client_code/_utils/m3x_motion.py`. Step 8.

## 1. What it is

M3 Expressive motion is spring-based: a movement accelerates and settles like a spring, and lively springs overshoot their target a little before settling. The theme reproduces the M3 springs in CSS and Python from the spring tokens.

## 2. The springs

Two schemes, each with six springs (stiffness, damping ratio; mass 1). Spatial springs move, resize and reshape; effects springs change colour and opacity.

| Spring | Expressive (default) | Standard |
|---|---|---|
| Spatial fast | 800, 0.6: 360 ms, about 9 % overshoot | 1400, 0.9: 224 ms |
| Spatial default | 380, 0.8: 435 ms | 700, 0.9: 317 ms |
| Spatial slow | 200, 0.8: 600 ms | 300, 0.9: 484 ms |
| Effects fast | 3800, 1.0: 150 ms | 3800, 1.0: 150 ms |
| Effects default | 1600, 1.0: 231 ms | 1600, 1.0: 231 ms |
| Effects slow | 800, 1.0: 327 ms | 800, 1.0: 327 ms |

Durations are the settling time: when the spring stays within 0.1 % of its target.

## 3. How it works

- `tools/spring_to_linear.py` (run as `python tools/spring_to_linear.py ../m3-custom-theme` from the library root) solves each spring and writes its CSS `linear()` easing (32 points) and its settling time into the generated block of `tokens.css`. That block is never edited by hand.
- Components use the alias tokens `--m3x-motion-{spatial,effects}-{fast,default,slow}-{easing,duration}`. In browsers without `linear()` they fall back to the M3 cubic-bezier easings and durations.
- Where springs are used: the shape changes of Expressive buttons, icon buttons, button groups, split buttons and menu items (spatial fast); the FAB menu, carousel items, toolbar hiding, the bottom sheet's entrance and the Expressive rail (spatial default); their colour changes (effects default). Hover state layers and fades keep the short standard timings.
- Every animated m3x rule has a `prefers-reduced-motion: reduce` rule that removes the motion.

## 4. API (`m3x_motion`)

| Name | Meaning |
|---|---|
| `SCHEMES` | `("expressive", "standard")` |
| `SPRINGS` | `("spatial-fast", "spatial-default", "spatial-slow", "effects-fast", "effects-default", "effects-slow")` |
| `set_scheme(scheme)`, `get_scheme()` | Choose or read the motion scheme for the whole app. |
| `reduced_motion()` | True if the device asks for reduced motion. |
| `spring(name)` | The (easing, duration in ms) of a spring, as the page uses them. |
| `animate(node, keyframes, name="spatial-default", **options)` | Run a Web Animations API animation with a spring; it jumps to the end with reduced motion. |
