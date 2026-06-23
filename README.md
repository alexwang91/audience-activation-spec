# Audience Activation Spec

A reusable skill for turning a country + audience input into an executable activation plan across mainstream reach channels.

## What this does

Input:

```yaml
country: Hungary
audience: people interested in cycling
```

Output:

- country-specific mainstream channel map
- HTE / consumer insight to platform-signal mapping
- paid media campaign settings
- organic and operational channel actions
- creator, community, retail, CRM, and partnership options
- measurement and experiment design
- prioritized launch plan

## Primary file

Read [`SKILL.md`](./SKILL.md) for the full skill definition.

## Templates and examples

- [`templates/output-template.md`](./templates/output-template.md): reusable output format
- [`examples/hungary-cycling.md`](./examples/hungary-cycling.md): sample output for Hungary + cycling-interest audience

## Core idea

The skill treats audience activation as a translation problem:

```text
consumer insight / HTE result
→ platform-recognizable proxy signal
→ campaign or operations setup
→ creative angle
→ measurement
→ validation experiment
```

It avoids pretending that a platform can perfectly identify every person in a behavioral group. Instead, it builds a set of high-signal proxies and validates them through experiments.

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
  hte_findings:
    - urban commuters respond to convenience
    - e-bike users respond to time saving and lower effort
    - safety-conscious buyers respond to helmets and lights bundles
```
