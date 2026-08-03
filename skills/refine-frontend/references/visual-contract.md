# Visual contract

The contract is a project-local decision record, not a design-system replacement. Keep it small enough to read before every refinement pass.

## Required structure

```json
{
  "schemaVersion": 1,
  "surface": {
    "name": "Settings / Profile",
    "primaryTask": "Update account identity",
    "routes": ["/settings/profile"],
    "states": ["default", "saving", "error", "success"]
  },
  "classification": {
    "interactionLoad": "medium",
    "informationDensity": "medium",
    "brandExpressionNeed": "low",
    "refinementDepth": "surface",
    "rationale": "Frequent operational form; clarity outranks novelty."
  },
  "patternSelection": {
    "taskTopology": "configure",
    "dominantArtifact": "workspace configuration",
    "nativePattern": "focused settings form",
    "navigationModel": "product shell with local settings navigation",
    "compositionModel": "single reading column with progressive sections",
    "existingPrimitives": ["settings-nav", "field-group", "save-bar"],
    "productSpecificSignals": ["workspace identity preview", "persistent save state"],
    "alternativePattern": "two-pane settings inspector",
    "rejectedDefaults": ["dashboard metric grid", "generic card mosaic"],
    "mobileTransformation": "keep one form sequence and pin save status after edits",
    "convergenceRisk": "medium",
    "rationale": "The task is sequential configuration, not monitoring or triage."
  },
  "invariants": [],
  "constraints": {
    "framework": "Next.js",
    "styling": "Tailwind",
    "newDependencies": false,
    "maxChangedFiles": null
  },
  "foundations": {
    "typography": {},
    "spacing": {},
    "colorRoles": {},
    "surfaces": {},
    "shape": {},
    "layout": {},
    "states": {},
    "responsive": {}
  },
  "signature": {
    "enabled": false,
    "channel": null,
    "rule": null,
    "exclusions": []
  },
  "verification": {
    "viewports": [
      {"name": "mobile", "width": 390, "height": 844},
      {"name": "desktop", "width": 1440, "height": 900}
    ],
    "commands": [],
    "scenarios": []
  }
}
```

## Decision rules

- Record only rules that affect the named surface or a shared primitive it uses.
- Derive `patternSelection` from the primary task, dominant artifact, information flow, and existing product system before choosing visual treatments.
- Name at least one rejected default. A rejected default is a plausible but insufficiently contextual pattern, not a banned component.
- Record at least two `productSpecificSignals` that should remain recognizable without relying on the product name or accent color.
- Use `alternativePattern` to show that selection was deliberate rather than the first available default.
- Describe `mobileTransformation` as a task-preserving behavior, not only a column change.
- Treat palette, radius, shadow, and spacing changes as polish rather than pattern differentiation.
- Do not force novelty. Reuse a familiar pattern when it is the clearest match for the task, but document why it fits.
- Prefer semantic roles (`action-primary`, `text-muted`) over raw values when the project already has or needs reusable tokens.
- Preserve established brand values unless the user authorizes brand work.
- Set `signature.enabled` only after foundation defects are resolved.
- Use one signature channel. A channel can contain several coordinated properties, but it must express one idea.
- Add explicit exclusions when a likely but unsuitable treatment should not recur, such as nested cards, decorative gradients, or always-on motion.
- Use `maxChangedFiles` as a guardrail only when the user or project imposes it. Do not game the metric by creating oversized files.

## Feedback precedence

When rules conflict, use this order:

1. explicit current user instruction;
2. functional and accessibility invariants;
3. accepted/rejected project feedback;
4. existing brand and design-system rules;
5. the visual contract;
6. contextual heuristics;
7. agent preference.

Rejected feedback blocks automatic reuse of the same rule. It does not prevent a materially different solution to the same underlying problem.
