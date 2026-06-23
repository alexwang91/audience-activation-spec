# Invalid Fixture: Synthetic Signal Misused as Causal HTE

## 1. Activation brief

| Field | Value |
|---|---|
| Country | Hungary |
| Audience | People interested in cycling |
| Business goal | Ecommerce purchase |
| Funnel stage | Conversion |
| Primary activation thesis | Scale the synthetic causal HTE segment immediately through Google and Meta. |
| Evidence handling | Synthetic panel output is treated as a targeting label. |
| Main assumptions | Hungary only. |

## 2. Market and channel assumptions

| Assumption | Working view | Confidence | Validation needed |
|---|---|---|---|
| Primary language(s) | Hungarian | Medium | Validate later |
| Main regions / cities | Hungary | Medium | Validate later |
| Dominant digital behaviors | Search and social | Medium | Validate later |
| Purchase journey | Search then buy | Medium | Validate later |
| Evidence availability | Synthetic panel only | Low | None planned |
| Compliance / policy constraints | Not considered | Low | Validate later |

## 3. Mainstream reach-channel map

| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |
|---|---|---|---|---|
| Google Search | Conversion | Cycling users search for accessories | Keywords | High |
| Meta | Awareness | Cycling users use social feeds | Interest proxies | High |

## 4. Research-signal-to-platform mapping

| Research signal | Evidence label | Consumer meaning | Platform proxy | Channels where usable | Required validation | Caveats |
|---|---|---|---|---|---|---|
| synthetic_panel row says commuters buy more safety gear | causal_hte | Urban commuters have a proven treatment effect for safety ads | Cycling and commuter interest targeting | Google, Meta | None | Synthetic output treated as proof |

## 5. Channel execution specs

### Channel: Meta

```yaml
role: conversion
objective: purchases
setup:
  geography: Hungary
  language: Hungarian
  audience:
    included:
      - commuter and cycling interest proxies
    excluded: []
  inventory_or_placement:
    - Reels
  bid_or_budget: scale immediately
  creative:
    angles:
      - safety
    formats:
      - short video
  landing_or_destination: safety bundle page
  measurement:
    primary_kpi: purchases
    secondary_kpis:
      - add to cart
    tracking:
      - pixel
evidence_basis:
  strongest_signal: synthetic_panel row
  evidence_label: causal_hte
  activation_safety: causal_evidence
risks:
  - none
validation_test: none
```

## 6. Experiment matrix

| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |
|---|---|---|---|---|---|---|
| A | Meta | Cycling interest | Safety | Purchase CPA | Any sale | Scale |

## 7. Measurement and instrumentation

### Conversion events

| Event | Definition | Source | Required setup |
|---|---|---|---|
| Purchase | Order | Website | Pixel |

## 8. Prioritized launch plan

| Phase | Timing | Actions | Exit criteria |
|---|---|---|---|
| Phase 0 | Now | Launch and scale | Spend |

## 9. Quality checks

- [ ] The plan is country-specific.
- [ ] The audience has been translated into executable platform proxy signals.
- [ ] Each paid channel includes geography, language, audience, creative, bid/budget, landing, and measurement.
- [ ] Platform feature claims are current or labeled as assumptions.
- [ ] Compliance-sensitive targeting is conservative.
