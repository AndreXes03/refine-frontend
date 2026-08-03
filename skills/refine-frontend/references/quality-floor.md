# Readability and usability quality floor

Use this reference to prevent a visually polished result from shipping with weak reading, interaction, or recovery behavior. Apply it to the changed surface and the shared primitives it touches. It is a release floor, not a style preset and not a claim of WCAG conformance.

## Contents

1. Evidence levels
2. Structure and comprehension
3. Typography and reading
4. Contrast and use of color
5. Keyboard, focus, and control naming
6. Targets, states, and feedback
7. Forms, errors, and recovery
8. Responsive fit and spatial hierarchy
9. Density, grouping, and data display
10. Quality-floor record

## Evidence levels

Classify every finding before acting:

- **Standard** — traceable to an applicable WCAG 2.2 requirement. Treat an observed failure as a blocker unless the user explicitly changes the supported scope.
- **System rule** — already established by the product's design system, platform, or accepted feedback. Preserve it unless there is evidence that the rule itself causes harm.
- **Heuristic** — likely to improve comprehension or efficiency but dependent on content, language, task, and audience. Verify it visually and functionally.
- **Preference** — explicitly requested or accepted by the user. Never relabel preference as research.

Do not turn the numeric values below into a universal aesthetic recipe. Measure the actual rendered surface, preserve product-specific density, and prefer existing tokens when they satisfy the intent.

## 1. Structure and comprehension

- Give the surface one clear purpose and make the next meaningful action discoverable without scanning every region.
- Keep headings, landmarks, lists, tables, labels, and groups semantically aligned with their visible relationships. Do not use size or position as the only source of structure.
- Keep heading text descriptive and ordered by content hierarchy; do not select heading levels for visual size.
- Use the user's domain language. Keep internal implementation terms, unexplained abbreviations, and raw status codes out of primary UI copy.
- Prefer recognition over recall: keep essential choices, constraints, current values, and consequences visible at the decision point.
- Remove information only when it is irrelevant to the current task. Minimalism that hides controls, status, or context increases interaction cost.

Evidence: inspect the rendered hierarchy, semantic tree or markup, and the primary task path. Record the route and state checked.

## 2. Typography and reading

- Use at least an effective 16 CSS px for most running body text unless the existing product and audience justify another tested value. Reserve smaller text for short, secondary material rather than core instructions or actions.
- Keep long-form text predominantly left aligned in left-to-right languages. Avoid justified text and long centered passages.
- Keep most running-text lines within roughly 45–90 characters; target about 66 characters for sustained reading. Treat short alerts, captions, code, tables, and compact tool UI as contextual exceptions.
- Use a line height of at least 1.5 for sustained prose as a strong default. Short headings and compact controls may be tighter when letters and lines remain unambiguous.
- Keep uppercase, italics, bold, condensed faces, and aggressive letter spacing to short emphasis or labels. Do not set paragraphs or essential instructions in all caps.
- Connect headings to the content they introduce with less space below than above. Use proximity before adding borders or containers.
- Confirm that 200% text zoom does not remove content or functionality.
- Confirm that user-applied text spacing—line height 1.5×, paragraph spacing 2×, letter spacing 0.12×, and word spacing 0.16×—does not clip, overlap, or hide content.

Evidence: capture the densest realistic text state, computed type values for critical text, and the 200% or text-spacing check when affected.

Sources: [USWDS typography guidance](https://designsystem.digital.gov/components/typography/), [WCAG 2.2 resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), and [WCAG 2.2 text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## 3. Contrast and use of color

- Maintain at least 4.5:1 contrast for normal text and 3:1 for large text under WCAG 2.2 AA, including text inside interactive states.
- Maintain at least 3:1 contrast for essential component boundaries, state indicators, icons that convey meaning, and focus indicators against adjacent colors where WCAG non-text contrast applies.
- Do not communicate error, success, selection, priority, or status through color alone. Add text, shape, position, iconography, or another perceivable cue.
- Measure computed foreground and background colors in the actual state. Do not approve contrast from token names, a screenshot estimate, or the default state alone.
- Disabled controls may be exempt from some contrast criteria, but they must remain distinguishable and must not be the only way to explain why an action is unavailable.

Evidence: record the tested color pairs and ratios for primary text, muted essential text, key controls, focus, error, and selected states.

Sources: [WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), and [use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## 4. Keyboard, focus, and control naming

- Make every interactive function operable with a keyboard. Start with native HTML behavior and use ARIA patterns only when the component truly needs them.
- Keep DOM, reading, and focus order logical and aligned with the visible task sequence. Do not use positive `tabindex` values to repair a visually reordered layout.
- Keep focus visible, visually distinct from selected state, and unobscured by sticky headers, drawers, cookie banners, or overlays.
- Restore focus predictably after closing a modal, menu, or other temporary layer. Do not strand focus in removed content.
- Give every control a concise accessible name. Prefer persistent visible labels and ensure the visible label is included in the accessible name.
- Apply established keyboard conventions to tabs, menus, grids, comboboxes, and other composite widgets. Do not invent bindings without a product-specific need and documentation.

Evidence: record the keyboard path through the primary task, the focused element before and after overlays, and at least one focus-visible capture.

Sources: [WAI-ARIA APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) and [accessible names and descriptions](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).

## 5. Targets, states, and feedback

- Make pointer targets at least 24×24 CSS px or satisfy the WCAG 2.2 spacing exception. Aim larger for primary touch actions and high-frequency controls when density allows.
- Provide distinguishable default, hover, focus, active, selected, disabled, loading, error, and success states when those states exist. Never rely on hover to reveal essential actions on a touch-capable surface.
- Acknowledge user actions promptly. Keep long-running operations visibly in progress and prevent duplicate destructive or financial submissions.
- Keep system status close to the affected object or action. Use programmatic status messages when updates occur without moving focus.
- Preserve user control: provide cancel, back, close, undo, or confirmation according to consequence and reversibility. Do not add confirmation to every harmless action.

Evidence: record target dimensions or spacing for the smallest repeated controls and exercise all states introduced or changed.

Sources: [WCAG 2.2 target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), and [Nielsen Norman Group usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).

## 6. Forms, errors, and recovery

- Use persistent visible labels; do not use placeholders as labels. Connect hints and errors programmatically to the relevant field or group.
- Group related choices with appropriate semantics. Put constraints and formatting help before input when knowing them changes the answer.
- Prevent errors where reasonable, but do not block valid real-world input with unnecessarily strict formatting.
- On failure, identify the specific problem and explain how to fix it in plain language. Keep the message next to the affected field; add a linked summary for long or multi-error forms when appropriate.
- Preserve the user's entered values after validation. Move focus only when it improves recovery and does not destroy context.
- Distinguish validation errors, permission limits, empty results, and service failures; they require different explanations and next steps.

Evidence: exercise one invalid, incomplete, or failed state relevant to the surface and record recovery behavior. Use `not-applicable` only when the surface has no editable, fallible, or asynchronous flow.

Source: [GOV.UK error message guidance](https://design-system.service.gov.uk/components/error-message/) and [validation pattern](https://design-system.service.gov.uk/patterns/validation/).

## 7. Responsive fit and spatial hierarchy

- Support reflow at 320 CSS px without page-level horizontal scrolling or loss of information or functionality, except for genuinely two-dimensional regions such as a data table. Keep any exception local and keyboard reachable.
- Transform the composition around task priority; do not merely stack every desktop region. Keep the primary action, current status, and necessary context reachable in a logical order.
- Test realistic long labels, localization expansion, dense data, empty states, open menus, validation messages, and software keyboard pressure when relevant.
- Prevent fixed or sticky UI from covering the current focus, page title, anchor target, error summary, or terminal content.
- Reserve space for media and async regions to prevent disruptive layout shifts.

Evidence: capture the minimum supported viewport and one dense or long-content state; record page and scoped overflow behavior.

Sources: [WCAG 2.2 reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) and [focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html).

## 8. Density, grouping, and data display

- Preserve useful density in operational interfaces. Improve scan paths, alignment, grouping, and progressive disclosure before adding empty space.
- Let proximity, alignment, headings, and surface changes express relationships. Do not wrap every region in an equal card or repeat the same label at multiple hierarchy levels.
- Align comparable values consistently. Use tabular numerals when available for changing or columnar numbers; align numeric columns according to the product's reading task.
- Keep table headers, row identity, sort state, units, and empty values unambiguous. Use a scoped horizontal scroller or alternate narrow representation rather than clipping columns.
- Keep destructive, primary, and high-frequency actions distinct by consequence and task priority, not by arbitrary visual novelty.
- Make charts and status visuals understandable without relying on color alone and expose the underlying value or equivalent text.

Evidence: inspect the densest realistic state and explain the intended scan path. Treat these rules as contextual unless they map to a standard violation.

## Quality-floor record

Complete `qualityFloor.checks` in the visual contract before strict validation. Use only:

- `pass` — inspected and supported by recorded evidence;
- `not-applicable` — outside the changed surface, with a concrete reason in `evidence`.

Required check IDs:

1. `structureAndComprehension`
2. `typographyAndZoom`
3. `contrastAndColor`
4. `keyboardAndFocus`
5. `targetsStatesAndFeedback`
6. `formsErrorsAndRecovery`
7. `responsiveAndOverflow`
8. `densityGroupingAndData`

Do not use `not-applicable` because a check was inconvenient or a tool was unavailable. Record an unresolved risk and stop sign-off instead. Automated scans can support this record, but rendered inspection and normal user input remain required.
