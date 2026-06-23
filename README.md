# Audience Activation Spec

A reusable skill for turning a country + audience input into an evidence-aware activation plan across mainstream reach channels.

## What this does

Input:

```yaml
country: Hungary
audience: people interested in cycling
```

Output:

- country-specific mainstream channel map
- research signal / HTE / consumer insight to platform-signal mapping
- evidence labels and calibration limits
- paid media campaign settings
- organic and operational channel actions
- creator, community, retail, CRM, and partnership options
- measurement and experiment design
- prioritized launch plan
- quality checks for AI / synthetic research misuse

## Primary file

Read [`SKILL.md`](./SKILL.md) for the full skill definition.

## Supporting files

- [`references/research-signal-contract.md`](./references/research-signal-contract.md): evidence labels, allowed claims, prohibited claims, and examples
- [`schemas/research-signal.schema.json`](./schemas/research-signal.schema.json): minimal machine-readable schema for research signals
- [`schemas/activation-plan.schema.json`](./schemas/activation-plan.schema.json): minimal machine-readable schema for activation plans
- [`templates/output-template.md`](./templates/output-template.md): reusable evidence-aware output format
- [`examples/hungary-cycling.md`](./examples/hungary-cycling.md): sample output for Hungary + cycling-interest audience
- [`scripts/validate_activation_spec.py`](./scripts/validate_activation_spec.py): stdlib-only markdown validator

## Core idea

The skill treats audience activation as a translation problem:

```text
research signal
→ evidence label
→ activation-safe audience interpretation
→ platform-recognizable proxy signal
→ campaign or operations setup
→ validation experiment
```

It avoids treating synthetic consumers, LLM interviews, or stated preferences as directly purchasable audience inventory. These signals can generate hypotheses and creative angles. They need platform proxies and validation before scale.

## AI / synthetic research safety model

This repository supports modern AI research signals, including synthetic panels and LLM interviews, but it separates them from observed behavior and causal evidence.

Default rules:

- A synthetic panel is a hypothesis source, not real consumer behavior.
- An LLM interview is a hypothesis source, not a deterministic audience list.
- A survey can show stated preference or descriptive segment differences, but not purchase behavior unless linked to behavior.
- Sales, click, and conversion data can show observed behavioral lift, but not causal treatment effects without a valid design.
- `causal_hte` requires experiment, treatment/control, randomized test, holdout, or credible quasi-experiment evidence.
- Platform targeting should be described as proxy-based unless the user supplies consented first-party data that the platform can use directly.

The safe posture is:

```text
synthetic / LLM / survey insight
→ hypothesis
→ platform proxy
→ small-budget validation
→ evidence label update
→ scale only if behavior supports it
```

## Minimal prompt

```text
Use the Audience Activation Spec skill.
Country: Hungary
Audience: people interested in cycling
Goal: purchase
Product: bicycle accessories ecommerce store
```

## Recommended prompt

```yaml
country: Hungary
audience: people interested in cycling
business_context:
  product_or_offer: bicycle accessories ecommerce store
  conversion_goal: purchase
  funnel_stage: conversion
  budget_level: medium
  target_city_or_region: Budapest plus national delivery
  languages: Hungarian, English
  first_party_data: website_visitors
  research_signals:
    - signal_id: syn_hu_cycling_001
      source_type: synthetic_panel
      audience_description: Hungarian urban cycling-interested consumers
      finding: Synthetic respondents who described themselves as urban commuters preferred messages about time saving, theft prevention, and night visibility.
      evidence_label: preference_heterogeneity
      calibration_level: uncalibrated
      limitations:
        - Synthetic respondents are not observed buyers.
        - The result may reflect prompt design and model priors.
      recommended_use: Generate creative hypotheses for commuter cycling ads and validate with small-budget channel tests.
```

## Validation

Run the valid fixture:

```bash
python scripts/validate_activation_spec.py evals/valid-hungary-cycling.md
```

Expected: pass.

Run negative fixtures with `--expect-fail`:

```bash
python scripts/validate_activation_spec.py evals/invalid-deterministic-targeting.md --expect-fail
python scripts/validate_activation_spec.py evals/invalid-causal-hte.md --expect-fail
```

Expected: pass because the validator catches the intended misuse.

## Design scope for v1

This v1 stays lightweight:

- Markdown-first skill definition
- JSON schemas as documentation and future validation targets
- one Python validator using only the standard library
- no package manager
- no CI workflow
- no country packs yet
- no full activation-plan generator yet
