---
name: refine-frontend
description: Refine an existing, working React or Next.js product interface into a more coherent, polished, responsive, and accessible UI while preserving behavior and minimizing code changes. Use for visual refactoring, UI polish, design QA with fixes, inconsistent Tailwind or shadcn interfaces, weak hierarchy or spacing, pre-release frontend finishing, and follow-up refinement that should remember accepted or rejected design decisions. Do not use to create a new site from scratch, redesign a brand, reproduce a Figma file, or change product behavior.
---

# Refine Frontend

Improve a working product UI without turning the task into a redesign. Build a durable visual contract, fix the highest-impact visual debt, verify behavior and responsive states, and persist human feedback for the next pass.

## Core contract

Optimize for **maximum perceived-quality gain per reasonable code delta**.

Preserve these invariants unless the user explicitly changes scope:

- business logic, data flow, APIs, routing, and permissions;
- factual copy, field names, and information architecture;
- semantic HTML and existing accessibility behavior;
- supported states, breakpoints, tests, and public component APIs;
- dependencies, build tooling, and brand assets.

Do not replace the product with a template, impose an aesthetic preset, add decorative effects by default, or describe an unverified result as "premium", "pixel-perfect", or accessible.

## Choose the mode

- **Refine**: inspect, plan, edit, and verify one named surface. Use by default.
- **Audit**: inspect and produce the contract and prioritized findings, but do not edit product code.
- **Continue**: load an existing `.visual-refactor/` directory, honor its feedback, and refine the next surface or iteration.

Keep v0.1 work to existing product UI—dashboards, tools, SaaS screens, forms, settings, tables, onboarding, and operational software. Do not expand into promotional sites or greenfield interface generation.

## Workflow

### 1. Establish scope and baseline

Identify one surface, its primary task, the densest realistic state, and the smallest supported viewport. Inspect the repository before proposing visual changes.

Run the project's existing build, tests, lint, or typecheck in proportion to the change. Capture baseline screenshots at desktop and mobile; add tablet only when layout behavior materially changes there.

If `.visual-refactor/` exists, read `visual-contract.json`, `visual-feedback.json`, and `change-ledger.md` before making decisions. Do not repeat a rejected rule unless new evidence or a changed constraint justifies it.

### 2. Freeze invariants

Write concrete invariants, not broad promises. Include important controls and states. Examples:

- `Submitting the form still calls saveProfile with the same payload.`
- `The table retains all columns and keyboard-accessible sorting.`
- `No new runtime dependency.`
- `The 320 CSS px view does not require page-level horizontal scrolling.`

Stop and request direction if the visual improvement would require changing product behavior, content hierarchy, brand, or a public API.

### 3. Classify the surface

Assign and justify:

```yaml
interaction_load: high | medium | low
information_density: high | medium | low
brand_expression_need: high | medium | low
refinement_depth: foundations | surface | system
```

High interaction load or information density lowers the expression budget. Favor familiar patterns, stable geometry, legibility, and state clarity. Low-load surfaces may support one stronger expressive decision.

### 4. Initialize or update the visual contract

Run:

```bash
python3 <skill-dir>/scripts/refine_workspace.py init \
  --project <project-root> \
  --surface "<surface-name>"
```

Then complete `.visual-refactor/visual-contract.json`. Use [visual-contract.md](references/visual-contract.md) for the schema and decision rules.

The contract has two layers:

1. **Foundation** — hierarchy, typography, composition, spacing, semantic color, surfaces, shape, responsive behavior, and states.
2. **Signature** — at most one expressive channel: typography, composition, color, motion, or imagery.

Foundation is mandatory. Signature is optional and must never compensate for weak structure.

### 5. Diagnose before editing

Read [research-and-rules.md](references/research-and-rules.md). Distinguish three kinds of evidence:

- **Observed defect**: visible or measurable in this product.
- **Standard violation**: traceable to a relevant standard such as WCAG.
- **Design hypothesis**: contextual judgment that requires visual comparison and human acceptance.

Rank findings by user impact, recurrence, and confidence. Limit the first pass to three to five coherent changes. Prefer root fixes in tokens or shared components when the inconsistency recurs; prefer local fixes when the issue is surface-specific.

### 6. Refactor in impact order

Work in this order:

1. typography and information hierarchy;
2. container geometry and composition;
3. spacing and rhythm;
4. semantic color and surface separation;
5. component morphology and consistency;
6. interaction states and responsive behavior;
7. one optional signature move.

Keep the diff narrow. Reuse the existing component system and tokens. Consolidate repeated arbitrary values only when doing so reduces real inconsistency; do not perform unrelated cleanup.

For each change, record:

- the observed problem;
- why this change addresses it;
- the affected files;
- the invariant and verification checks;
- whether the choice is foundation or signature.

### 7. Prove the result

Verification has three independent gates:

**Functional gate**

- Exercise primary controls with normal input.
- Confirm build, tests, lint, and typecheck relevant to the change.
- Verify loading, empty, error, disabled, selected, and dense states when they exist.

**Technical visual gate**

- Inspect desktop and mobile screenshots; use the densest realistic state.
- Check page-level overflow, clipping, overlap, text wrapping, image distortion, layering, and layout shift.
- Check keyboard focus, contrast, target size/spacing, reduced motion, and 320 CSS px reflow where applicable.
- Treat numeric checks as supporting evidence, not a replacement for screenshot inspection.

**Design gate**

- Compare before and after at the same viewport and state.
- Confirm clearer hierarchy, more coherent rhythm, contextual fit, and no brand drift.
- Ask whether every added visual element has a job.
- Reject a prettier screenshot if usability or behavior regressed.

See [verification.md](references/verification.md) for the sign-off protocol.

### 8. Persist decisions and feedback

Append accepted implementation decisions to `.visual-refactor/change-ledger.md`. Record user responses with:

```bash
python3 <skill-dir>/scripts/refine_workspace.py feedback \
  --project <project-root> \
  --id VR-TYPE-001 \
  --status accepted \
  --note "Keep the stronger heading contrast."
```

Allowed statuses are `accepted`, `modified`, `rejected`, and `reverted`. Feedback is project evidence, not a universal design rule.

Validate the workspace before sign-off:

```bash
python3 <skill-dir>/scripts/refine_workspace.py validate --project <project-root>
```

## Final response

Lead with what improved. Report:

- surface and files changed;
- three to five material decisions;
- functional and viewport checks performed;
- any unresolved risk or intentional exclusion;
- paths to the before/after evidence and visual contract.

Use calibrated language. Say what was observed and verified; do not convert aesthetic judgment into a fake objective score.
