# Verification protocol

Use the same route, data, state, viewport, zoom, color mode, and motion preference for before/after comparisons.

## Coverage inventory

Before editing, list:

- the surface's user-visible claims;
- primary and secondary controls;
- meaningful states and transitions;
- densest realistic content state;
- minimum supported viewport;
- invariants that could regress.

Map each item to a functional check and a visual check. Do not infer visual success from passing tests.

Initialize the eight checks in `qualityFloor.checks` and identify the route, state, measurement, capture, or command that can prove each one. Use [quality-floor.md](quality-floor.md) for the rules and evidence expectations.

## Screenshot set

Capture viewport screenshots rather than relying only on full-page images:

- desktop initial and densest state;
- mobile initial and densest state;
- focus-visible state for an important control;
- open overlay, error, or expanded state when changed by the refinement;
- optional tablet only when the layout has a distinct intermediate behavior.

Store baseline and final evidence in `.visual-refactor/before/` and `.visual-refactor/after/` with matching names.

## Technical inspection

Check:

- `document.documentElement.scrollWidth <= document.documentElement.clientWidth` for page-level overflow, then visually inspect scoped scrollers;
- no clipped labels, controls, focus rings, menus, tooltips, or sticky regions;
- expected wrapping at long labels and realistic data lengths;
- clear hover, focus, active, selected, disabled, loading, error, and success states where present;
- keyboard traversal follows a meaningful order and keeps focus visible;
- reduced-motion preference does not hide essential state changes;
- contrast and target sizing with an appropriate checker or computed styles;
- media and dynamic regions reserve stable geometry.
- rendered text remains usable at 200% zoom and with WCAG text-spacing overrides when the changed surface can be affected;
- controls retain visible labels or accessible names, and status, selection, errors, and priority do not depend on color alone;
- the primary task exposes timely feedback and a recoverable relevant failure state.

Numeric checks can miss visibly obscured or awkward content. A screenshot failure remains a failure even when DOM metrics pass.

## Functional inspection

Use normal user input for primary flows. For reversible controls, test initial state, changed state, and return. Exercise at least two off-happy-path cases relevant to the surface, such as:

- long text or dense data;
- empty, loading, and error content;
- keyboard-only operation;
- narrow viewport with an open menu;
- slow media or delayed dynamic content.

Run the repository's existing verification commands. Do not add a new testing stack solely for this skill unless the user approves it.

## Sign-off

Pass only when all are true:

- primary behavior and relevant automated checks pass;
- invariants remain true;
- required viewports and states were inspected;
- no page-level overflow, clipping, overlap, or brand drift remains;
- accessibility was not knowingly degraded;
- before/after evidence shows a coherent improvement;
- every signature treatment supports the contract;
- at least two product-specific signals remain visible when brand names and accent color are ignored;
- the mobile result follows the recorded task-preserving transformation instead of mechanically stacking desktop regions;
- strict workspace validation passes with no placeholder decisions;
- every required quality-floor check is `pass` or concretely `not-applicable` and includes evidence;
- unresolved risks and exclusions are reported plainly.

Do not claim WCAG conformance from this protocol alone. Do not use an aesthetic score unless it comes from a named, reproducible human study.
