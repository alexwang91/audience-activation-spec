# Audience Activation Spec Output Template

## Input

```yaml
country: <country>
audience: <audience>
business_context:
  product_or_offer: <optional>
  conversion_goal: <optional>
  funnel_stage: <optional>
  budget_level: <optional>
  target_city_or_region: <optional>
  languages: <optional>
  first_party_data: <optional>
  hte_findings: <optional>
```

## 1. Activation brief

| Field | Value |
|---|---|
| Country |  |
| Audience |  |
| Business goal |  |
| Funnel stage |  |
| Primary activation thesis |  |
| Main assumptions |  |

## 2. Market and channel assumptions

| Assumption | Working view | Confidence | Validation needed |
|---|---|---|---|
| Primary language(s) |  |  |  |
| Main regions / cities |  |  |  |
| Dominant digital behaviors |  |  |  |
| Purchase journey |  |  |  |
| Compliance / policy constraints |  |  |  |

## 3. Mainstream reach-channel map

| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |
|---|---|---|---|---|
| Search engines |  |  | Keywords, shopping, local search |  |
| Paid social |  |  | Interests, broad targeting, lookalikes, creator-style creative |  |
| Video platforms |  |  | Video interests, custom segments, placements |  |
| Display / programmatic |  |  | Contextual topics, publisher lists, retargeting |  |
| Retail media / marketplaces |  |  | Marketplace search, sponsored products, category ads |  |
| Local publishers / vertical communities |  |  | Sponsorships, native ads, newsletter, forum presence |  |
| Influencers / creators |  |  | Niche creator audiences, affiliate links, whitelisting |  |
| Messaging / communities |  |  | Opt-in groups, support, referral, community drops |  |
| SEO / content |  |  | Local-language search demand, guides, comparison pages |  |
| CRM / retargeting |  |  | First-party lists, lifecycle triggers, abandoned cart |  |
| Partnerships / offline |  |  | Affiliates, clubs, events, retailers, associations |  |

## 4. HTE-to-platform mapping

| HTE / audience signal | Consumer meaning | Platform proxy | Channels where usable | Caveats |
|---|---|---|---|---|
|  |  |  |  |  |

## 5. Channel execution specs

### Channel: <name>

```yaml
role: <awareness | consideration | conversion | retention>
objective: <campaign objective or operational objective>
setup:
  geography: <country / city / radius / presence setting>
  language: <settings and creative language>
  audience:
    included:
      - <segments / keywords / topics / placements / communities>
    excluded:
      - <negative audiences / irrelevant intents / excluded regions>
  inventory_or_placement:
    - <feed / search / video / display / creator / community / marketplace>
  bid_or_budget: <bidding, budget split, pacing>
  creative:
    angles:
      - <angle>
    formats:
      - <format>
  landing_or_destination: <landing page / PDP / lead form / community / app page>
  measurement:
    primary_kpi: <KPI>
    secondary_kpis:
      - <KPI>
    tracking:
      - <pixel / SDK / UTM / offline conversion / coupon>
  operating_cadence:
    daily:
      - <task>
    weekly:
      - <task>
risks:
  - <risk>
validation_test: <test design>
```

Repeat for each high-priority channel.

## 6. Experiment matrix

| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |
|---|---|---|---|---|---|---|
| A |  |  |  |  |  |  |
| B |  |  |  |  |  |  |
| C |  |  |  |  |  |  |

## 7. Measurement and instrumentation

### Conversion events

| Event | Definition | Source | Required setup |
|---|---|---|---|
|  |  |  |  |

### UTM structure

```text
utm_source=<platform>
utm_medium=<paid_social|paid_search|video|display|creator|community|crm|affiliate>
utm_campaign=<country>_<audience>_<objective>
utm_content=<creative_angle>_<format>
utm_term=<keyword_or_segment>
```

### Reporting cadence

| Cadence | Tasks |
|---|---|
| Daily |  |
| Weekly |  |
| Monthly |  |

### Feedback loop into HTE

```text
campaign result
→ observed response by proxy signal
→ compare with HTE segment prediction
→ update segment definitions, creative angles, and media weights
```

## 8. Prioritized launch plan

| Phase | Timing | Actions | Exit criteria |
|---|---|---|---|
| Phase 0: foundation |  | Tracking, landing pages, consent, baseline |  |
| Phase 1: intent capture |  | Search, marketplace search, high-intent SEO |  |
| Phase 2: audience expansion |  | Paid social, video, display, contextual |  |
| Phase 3: trust channels |  | Creators, communities, partnerships |  |
| Phase 4: scale and retention |  | Retargeting, CRM, lookalikes, incrementality |  |

## 9. Quality checks

- [ ] The plan is country-specific.
- [ ] The audience has been translated into executable platform proxy signals.
- [ ] Each paid channel includes geography, language, audience, creative, bid/budget, landing, and measurement.
- [ ] Each operational channel includes owner actions, cadence, format, and KPI.
- [ ] Platform feature claims are current or labeled as assumptions.
- [ ] The answer avoids deterministic targeting claims unless first-party data exists.
- [ ] Compliance-sensitive targeting is conservative.
