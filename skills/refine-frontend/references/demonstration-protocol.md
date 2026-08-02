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

## Sign-off rules

Accept the pair only when:

1. the content and behavior contracts match;
2. both captures use the declared viewport and state;
3. relevant functional checks still pass;
4. page-level horizontal overflow is absent at 320 CSS px, except intentional inner regions such as a data table;
5. the change ledger explains each material difference;
6. the result is described with observed changes, not an invented quality score.

Reject and recapture if any invariant changed, a screenshot is selectively cropped, or the after state introduces a functional, responsive or accessibility regression.
