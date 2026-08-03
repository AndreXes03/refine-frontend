# Demonstration protocol

Use this protocol when publishing or handing off before/after evidence. The goal is an auditable comparison, not a persuasive mockup.

## Lock the comparison

- Capture the same route, data, state, viewport, browser and zoom.
- Preserve factual copy, controls, behavior and content density.
- Capture the baseline before editing product code.
- Do not hide difficult states, crop defects, or change content to flatter the result.
- Label synthetic fixtures as synthetic. Never imply client work or production metrics.

## Record an evidence manifest

For every pair, record:

- a stable identifier and surface name;
- classification: `real-product`, `public-reproduction`, or `synthetic-benchmark`;
- viewport width and height;
- frozen functional and content invariants;
- changed visual foundations or signature choice;
- checks actually completed;
- paths to before and after captures.

## Prevent benchmark-set convergence

When publishing more than one demonstration, evaluate the set as well as each pair.

- Give every case a task-specific shell. Share reset, accessibility, and evidence-label utilities; do not share one complete composition stylesheet across unrelated surfaces.
- Record the primary task topology, navigation model, composition model, density model, visual grammar, and rejected defaults for each case.
- Require meaningful difference in at least three of these five dimensions: navigation topology, dominant content structure, action placement, density or scan flow, and surface morphology.
- Do not count palette, brand name, copy, icon, radius, or accent-color changes as structural diversity.
- Preserve the same content, behavior, state, and viewport within each before/after pair. Diversity across the set never permits a dishonest comparison inside a pair.
- Explain why each after-state fits its task. If the explanation could be pasted onto another case unchanged, the benchmark is not specific enough.

Reject the set when multiple cases collapse into the same sidebar, topbar, card grid, metric strip, generic table shell, or other reusable starter without a documented product reason.

## Sign-off rules

Accept the pair only when:

1. the content and behavior contracts match;
2. both captures use the declared viewport and state;
3. relevant functional checks still pass;
4. page-level horizontal overflow is absent at 320 CSS px, except intentional inner regions such as a data table;
5. the change ledger explains each material difference;
6. the result is described with observed changes, not an invented quality score.
7. for a multi-case set, the convergence checks above pass and each case has a distinct task-based rationale.

Reject and recapture if any invariant changed, a screenshot is selectively cropped, the after state introduces a functional, responsive or accessibility regression, or palette variation is being used to hide structural sameness.
