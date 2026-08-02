# Research and operational rules

Use this reference to justify the method, not to force every interface into one style. Research findings are population- and task-dependent; translate them into hypotheses and guardrails, then verify the actual product.

## Evidence model

### Reduce accidental complexity; preserve useful familiarity

Tuch et al. tested first impressions of website screenshots and found that visual complexity and prototypicality affected aesthetic ratings at very short exposures. In their experiments, low-complexity, high-prototypicality websites were rated most positively.

Operational translation:

- remove redundant borders, nested cards, competing accents, and repeated labels before adding decoration;
- preserve familiar product patterns when interaction load is high;
- make novelty local and legible rather than changing every convention;
- do not infer that all dense interfaces are poor—operational products can require real density.

Source: Alexandre N. Tuch et al., *The role of visual complexity and prototypicality regarding first impression of websites* (2012): https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/

### Separate foundation from expression

Lavie and Tractinsky found two distinguishable dimensions in perceived website aesthetics: classical aesthetics, associated with order and clarity, and expressive aesthetics, associated with creativity and originality.

Operational translation:

- make the foundation layer complete before adding a signature;
- allow one primary expressive channel per surface;
- lower the expression budget as interaction load and information density rise;
- do not use decorative novelty to hide weak hierarchy or spacing.

Source: Talia Lavie and Noam Tractinsky, *Assessing dimensions of perceived visual aesthetics of web sites* (2004): https://cris.bgu.ac.il/en/publications/assessing-dimensions-of-perceived-visual-aesthetics-of-web-sites-2/

### Treat aesthetics and usability as related but independent gates

Tractinsky, Katz, and Ikar reported a strong relationship between perceived aesthetics and perceived usability in an ATM experiment. Later work by Tuch et al. found conditions where usability affected post-use aesthetics while aesthetics did not improve perceived usability. The evidence does not support treating beauty as proof of usability.

Operational translation:

- evaluate visual quality and functional usability separately;
- never accept a visually stronger result that breaks interaction or accessibility;
- describe aesthetic improvement as a contextual judgment, not an objective usability gain;
- retain before/after evidence and human feedback.

Sources:

- N. Tractinsky, A. S. Katz, and D. Ikar, *What is beautiful is usable* (2000): https://cris.bgu.ac.il/en/publications/what-is-beautiful-is-usable-2/
- Alexandre N. Tuch et al., *Is beautiful really usable?* (2012): https://edoc.unibas.ch/entities/publication/ebcfa3de-1a92-4195-b6fd-ab67d80af2aa

## Standards-backed technical rules

These checks can identify likely failures, but this skill does not certify WCAG conformance.

- **Contrast**: preserve WCAG 2.2 text and non-text contrast requirements. Validate actual computed colors and states, including disabled and focus states where applicable. https://www.w3.org/TR/WCAG22/
- **Focus**: every keyboard-operable control must expose a visible focus indicator; do not remove the browser outline without an adequate replacement. https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
- **Reflow**: non-exempt content should work at a width equivalent to 320 CSS px without loss of information/functionality or two-dimensional scrolling. Tables and other genuinely two-dimensional content can be scoped exceptions, not excuses for page-level overflow. https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
- **Target size**: WCAG 2.2 AA requires targets to be at least 24×24 CSS px or meet an exception such as adequate spacing. A 44×44 target is the enhanced AAA criterion, not the AA minimum. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- **Layout stability**: reserve space for late-loading media and dynamic regions. A good Core Web Vitals CLS target is 0.1 or less at the 75th percentile, but a local visual pass cannot establish field performance. https://web.dev/articles/optimize-cls

## Contextual heuristics

Treat these as design hypotheses, not standards:

- Establish one clear primary action per task region; subordinate secondary actions visually.
- Use typographic contrast before adding containers or decoration.
- Prefer a small set of repeated spacing relationships over many arbitrary gaps.
- Use surface changes only when they communicate grouping, elevation, selection, or state.
- Keep repeated components morphologically consistent: height, radius, padding, icon sizing, label alignment, and state treatment.
- Make dense interfaces orderly rather than artificially spacious. Density is not clutter when grouping and hierarchy are clear.
- Add motion only when it explains state change, continuity, causality, or hierarchy. Respect `prefers-reduced-motion`.
- Keep a signature move specific enough to be remembered and restrained enough not to compete with the primary task.

## Claim discipline

Use these labels in findings:

- `observed`: visible or measurable in the inspected state;
- `standard`: traceable to an applicable requirement;
- `hypothesis`: expected to improve contextual visual quality and requiring comparison/feedback;
- `preference`: explicitly requested or accepted by the user.

Do not invent percentages, universal scores, or research claims for spacing scales, font pairings, radius values, or aesthetic styles.
