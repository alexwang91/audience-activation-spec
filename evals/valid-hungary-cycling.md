# Valid Fixture: Hungary + Cycling Interest

## Input

```yaml
country: Hungary
audience: people interested in cycling
business_context:
  product_or_offer: bicycle accessories ecommerce store
  conversion_goal: purchase
  first_party_data: website_visitors
  research_signals:
    - signal_id: syn_hu_cycling_001
      source_type: synthetic_panel
      evidence_label: preference_heterogeneity
      calibration_level: uncalibrated
```

## 1. Activation brief

| Field | Value |
|---|---|
| Country | Hungary |
| Audience | People interested in cycling |
| Business goal | Ecommerce purchase |
| Funnel stage | Conversion with consideration support |
| Primary activation thesis | Capture high-intent cycling demand through Search and retargeting, then validate interest, contextual, creator, and publisher proxies before scaling. |
| Evidence handling | Synthetic and expert signals are treated as hypotheses until validated against observed behavior or a controlled test. |
| Main assumptions | Hungarian creative is primary. Budapest receives separate reporting. |

## 2. Market and channel assumptions

| Assumption | Working view | Confidence | Validation needed |
|---|---|---|---|
| Primary language(s) | Hungarian first, English as a limited test | Medium | Check conversion rate by landing-page language |
| Main regions / cities | National delivery, Budapest split for reporting | Medium | Check order density and shipping margin |
| Dominant digital behaviors | Search, social video, marketplace comparison, specialist cycling content | Medium | Validate with analytics and search-term reports |
| Purchase journey | Users search for gear, compare safety, price, reviews, and delivery | Medium | Confirm through post-purchase survey and funnel data |
| Evidence availability | Synthetic panel hypothesis plus website visitor behavior | Medium | Validate synthetic-derived angles through small-budget tests |
| Compliance / policy constraints | Use consented first-party lists and platform proxy signals conservatively | High | Review current platform policy before launch |

## 3. Mainstream reach-channel map

| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |
|---|---|---|---|---|
| Google Search | Conversion | Captures active demand for bikes, e-bikes, helmets, locks, lights, and accessories | Hungarian keywords, match types, negatives, shopping feed if available | High |
| Google YouTube / Demand Gen / Display | Awareness and consideration | Reaches users consuming cycling, outdoor, and urban mobility content | Custom segments, contextual topics, managed placements, remarketing | High |
| Performance Max | Conversion scaling | Can scale feed and asset groups after tracking works | Audience signals, search themes, product feed, conversion value bidding | High |
| Meta: Facebook and Instagram | Awareness and retargeting | Strong visual formats for commuting, safety, and product bundles | Broad targeting, interest proxies, catalog ads, engagement retargeting | High |
| TikTok | Discovery | Short-form demos can test commuting and safety hooks | Interest proxies, creator content, video engagement retargeting | Medium |
| Local cycling publishers | Consideration | Specialist readers have category interest and trust niche media | Sponsored guides, newsletter placement, native ads | Medium |
| Influencers / creators | Trust | Local cycling creators can demonstrate gear in context | Creator briefs, affiliate links, paid amplification rights | Medium |
| SEO / content | Durable intent | Hungarian guides can capture research and comparison demand | Buying guides, comparison pages, local cycling content | Medium |
| CRM / retargeting | Conversion and retention | Website visitors and cart abandoners are higher-intent first-party audiences | Email, dynamic retargeting, suppression rules, lifecycle triggers | High |
| Partnerships / offline | Trust and reach | Clubs, repair shops, and events aggregate cycling-interested users | Affiliate codes, event booths, shop collaborations | Medium |

## 4. Research-signal-to-platform mapping

| Research signal | Evidence label | Consumer meaning | Platform proxy | Channels where usable | Required validation | Caveats |
|---|---|---|---|---|---|---|
| syn_hu_cycling_001: synthetic panel suggests urban commuters prefer convenience and safety messages | preference_heterogeneity | Commuter cyclists may respond to time saving, locks, lights, and visibility | Budapest cycling keywords, commuter creative, lock/light category pages, cycling creator briefs | Search, Meta, TikTok, YouTube, SEO, creators | Test commuter vs generic cycling creative on qualified visit rate and add-to-cart rate | Synthetic panel is hypothesis-generating and uncalibrated |
| Website visitors who viewed helmet and light pages | behavioral_lift | Safety gear browsing indicates near-term category interest | Retargeting pools, CRM segments, product bundles, dynamic catalog ads | Google, Meta, CRM, email | Use holdout or capped retargeting test to estimate incremental recovered revenue | Observed behavior can be confounded by baseline purchase intent |
| Team assumption: e-bike users want longer-distance comfort | preference_heterogeneity | E-bike riders may value comfort and range support | e-bike accessory keywords, e-bike publisher placements, e-bike creator demos | Search, YouTube, Display, creators, SEO | Test e-bike accessory landing page against generic accessories page | Internal assumption needs behavioral validation |

## 5. Channel execution specs

### Channel: Google Search

```yaml
role: conversion
objective: purchases
setup:
  geography: Hungary with Budapest reporting split
  language: Hungarian primary
  audience:
    included:
      - kerékpár sisak
      - bicikli lámpa
      - kerékpár zár
      - elektromos kerékpár kiegészítők
    excluded:
      - free
      - jobs
      - used-only intents if not served
  inventory_or_placement:
    - search results
  bid_or_budget: use controlled budget until purchase tracking is stable
  creative:
    angles:
      - safe city cycling
      - commuter convenience
    formats:
      - responsive search ads
  landing_or_destination: Hungarian safety and commuter accessory pages
  measurement:
    primary_kpi: purchase CPA
    secondary_kpis:
      - add-to-cart rate
      - search-term quality
    tracking:
      - purchase event
      - UTM by keyword theme
  operating_cadence:
    daily:
      - check spend and tracking
    weekly:
      - review search terms and negatives
evidence_basis:
  strongest_signal: helmet and light page visitors
  evidence_label: behavioral_lift
  activation_safety: observed_behavior
risks:
  - Broad cycling terms may pull low-intent traffic.
validation_test: Compare safety keywords against generic cycling keywords on CPA and add-to-cart rate.
```

### Channel: Meta and Instagram

```yaml
role: awareness and retargeting
objective: purchases and add-to-cart events
setup:
  geography: Hungary
  language: Hungarian
  audience:
    included:
      - broad Hungary audience with cycling creative
      - cycling interest proxies where available
      - website visitor retargeting
    excluded:
      - recent purchasers unless cross-sell is intended
  inventory_or_placement:
    - Reels
    - Stories
    - Feed
  bid_or_budget: separate cold prospecting and retargeting budgets
  creative:
    angles:
      - commuter safety setup
      - night visibility kit
    formats:
      - UGC-style short video
      - carousel
  landing_or_destination: safety bundle and commuter accessory pages
  measurement:
    primary_kpi: add-to-cart CPA
    secondary_kpis:
      - CTR
      - purchase CPA
    tracking:
      - pixel
      - UTM by creative angle
  operating_cadence:
    daily:
      - monitor budget and creative fatigue
    weekly:
      - rotate weak hooks
evidence_basis:
  strongest_signal: syn_hu_cycling_001
  evidence_label: preference_heterogeneity
  activation_safety: hypothesis
risks:
  - Interest proxies may be broad.
validation_test: Compare broad audience with cycling creative against interest-proxy audience and retargeting pools.
```

## 6. Experiment matrix

| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |
|---|---|---|---|---|---|---|
| A | Google Search | Safety accessory keywords | Safe city cycling | Purchase CPA | CPA at or below target | Expand exact and phrase terms |
| B | Meta | Broad Hungary audience | Commuter safety setup | Add-to-cart CPA | Beats interest proxy at equal spend | Scale broad creative variants |
| C | YouTube / Display | Cycling contextual placements | Night visibility kit | Qualified visit rate | Beats generic outdoor placements by 20 percent | Add publisher-specific placements |
| D | Creator | Hungarian cycling micro-creators | Real commute setup | Creator-attributed sales | One creator clears target CPA | Whitelist best creator asset |
| E | CRM | Cart abandoners | Complete your setup | Incremental recovered revenue | Positive holdout-adjusted revenue | Scale lifecycle sequence |

## 7. Measurement and instrumentation

### Conversion events

| Event | Definition | Source | Required setup |
|---|---|---|---|
| Purchase | Completed ecommerce order | Website | Purchase event, value, currency, order id |
| Add to cart | Product added to cart | Website | Pixel and analytics event |
| Qualified visit | Product view or high-engagement session | Analytics | UTM and event tracking |

### Evidence update rules

| Current evidence label | Upgrade condition | Downgrade / caution condition |
|---|---|---|
| preference_heterogeneity | Repeated behavioral lift in channel tests | No lift or contradictory behavior |
| behavioral_lift | Treatment/control or credible quasi-experiment | Selection bias or weak instrumentation |
| causal_hte | Replicated experiment or external validity test | Fails outside tested population |

### UTM structure

```text
utm_source=google|meta|tiktok|publisher|creator|email
utm_medium=paid_search|paid_social|video|display|creator|community|crm|affiliate
utm_campaign=hu_cycling_purchase
utm_content=<creative_angle>_<format>
utm_term=<keyword_or_segment>
```

### Reporting cadence

| Cadence | Tasks |
|---|---|
| Daily | Check spend, tracking, disapprovals, and stock issues |
| Weekly | Review search terms, creative fatigue, proxy performance, and placement quality |
| Monthly | Update evidence labels, HTE interpretation, and budget allocation |

### Feedback loop into HTE / segmentation

```text
campaign result
→ observed response by proxy signal
→ compare with research signal and evidence label
→ update segment definitions, creative angles, media weights, and validation priority
```

## 8. Prioritized launch plan

| Phase | Timing | Actions | Exit criteria |
|---|---|---|---|
| Phase 0: foundation | Week 0 | Tracking, landing pages, consent, evidence audit, baseline | Events fire correctly |
| Phase 1: intent capture | Weeks 1-2 | Google Search and retargeting | Stable search-term quality |
| Phase 2: audience expansion | Weeks 2-4 | Meta, YouTube, Display, TikTok tests | Two proxy plus creative combinations clear thresholds |
| Phase 3: trust channels | Weeks 3-6 | Creators and publishers | One creator or publisher proves qualified traffic |
| Phase 4: scale and retention | Week 6+ | CRM, lookalikes, incrementality tests | Incremental revenue supports budget increase |

## 9. Quality checks

- [x] The plan is country-specific.
- [x] The audience has been translated into executable platform proxy signals.
- [x] Each paid channel includes geography, language, audience, creative, bid/budget, landing, and measurement.
- [x] Each operational channel includes owner actions, cadence, format, and KPI.
- [x] Platform feature claims are current or labeled as assumptions.
- [x] The answer avoids deterministic targeting claims unless first-party data exists.
- [x] Compliance-sensitive targeting is conservative.
- [x] Synthetic / LLM / survey / expert signals are visibly separated from observed behavior and causal evidence.
- [x] causal_hte appears only with experiment, treatment/control, randomized test, or quasi-experiment evidence.
- [x] Every research-derived targeting idea has a validation experiment before scale.
