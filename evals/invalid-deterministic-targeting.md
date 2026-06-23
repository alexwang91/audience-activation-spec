# Invalid Fixture: Deterministic Targeting Misuse

## 1. Activation brief

| Field | Value |
|---|---|
| Country | Hungary |
| Audience | People interested in cycling |
| Business goal | Ecommerce purchase |
| Funnel stage | Conversion |
| Primary activation thesis | Use platform audiences to deterministically reach all users who are interested in cycling. |
| Evidence handling | Synthetic signals are mentioned but not validated. |
| Main assumptions | Hungary only. |

## 2. Market and channel assumptions

| Assumption | Working view | Confidence | Validation needed |
|---|---|---|---|
| Primary language(s) | Hungarian | Medium | Validate later |
| Main regions / cities | Hungary | Medium | Validate later |
| Dominant digital behaviors | Search and social | Medium | Validate later |
| Purchase journey | Search then buy | Medium | Validate later |
| Evidence availability | Synthetic only | Low | Validate later |
| Compliance / policy constraints | Not considered | Low | Validate later |

## 3. Mainstream reach-channel map

| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |
|---|---|---|---|---|
| Google | Conversion | It can perfectly identify cycling people | Cycling audience | High |

## 4. Research-signal-to-platform mapping

| Research signal | Evidence label | Consumer meaning | Platform proxy | Channels where usable | Required validation | Caveats |
|---|---|---|---|---|---|---|
| Synthetic cycling persona | preference_heterogeneity | Likes cycling | Google cycling audience | Google | None | Assumes platform precision |

## 5. Channel execution specs

### Channel: Google

```yaml
role: conversion
objective: purchases
setup:
  geography: Hungary
  language: Hungarian
  audience:
    included:
      - cycling audience
    excluded: []
  inventory_or_placement:
    - all inventory
  bid_or_budget: scale immediately
  creative:
    angles:
      - cycling
    formats:
      - static
  landing_or_destination: homepage
  measurement:
    primary_kpi: purchases
    secondary_kpis:
      - CTR
    tracking:
      - UTM
evidence_basis:
  strongest_signal: synthetic persona
  evidence_label: preference_heterogeneity
  activation_safety: hypothesis
risks:
  - none
validation_test: none
```

## 6. Experiment matrix

| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |
|---|---|---|---|---|---|---|
| A | Google | Cycling audience | Cycling | Purchase | Any purchase | Scale |

## 7. Measurement and instrumentation

### Conversion events

| Event | Definition | Source | Required setup |
|---|---|---|---|
| Purchase | Order | Website | UTM |

## 8. Prioritized launch plan

| Phase | Timing | Actions | Exit criteria |
|---|---|---|---|
| Phase 0 | Now | Launch | Spend |

## 9. Quality checks

- [ ] The plan is country-specific.
- [ ] The audience has been translated into executable platform proxy signals.
- [ ] Each paid channel includes geography, language, audience, creative, bid/budget, landing, and measurement.
- [ ] Platform feature claims are current or labeled as assumptions.
- [ ] Compliance-sensitive targeting is conservative.
