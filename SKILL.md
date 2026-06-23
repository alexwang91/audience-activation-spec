# Audience Activation Spec Skill

## Purpose

Generate a country-specific audience activation plan from a simple input such as:

```text
Country: Hungary
Audience: people interested in cycling
```

The skill converts a research or HTE audience insight into an executable media and operations plan. The output should explain which mainstream channels matter in the target country and how to configure each channel so the team can reach the audience through paid media, organic operations, partnerships, and owned channels.

## When to use this skill

Use this skill when the user asks how to reach, activate, advertise to, operate for, or acquire a specific audience in a specific country or market.

Typical prompts:

- "Country: Hungary. Audience: cycling enthusiasts. Give me the activation spec."
- "How do I reach Gen Z skincare buyers in Indonesia?"
- "Turn this HTE segment into a media plan for Brazil."
- "For Germany + vegan parents, give me all major channels and settings."

## Required input

Ask for missing required input only when the country or audience is absent. Otherwise proceed with reasonable assumptions and label them.

```yaml
country: <required>
audience: <required>
```

## Optional input

Use optional fields when provided. Do not block the task when they are missing.

```yaml
business_context:
  product_or_offer: <optional>
  industry: <optional>
  conversion_goal: purchase | lead | signup | app_install | store_visit | awareness | other
  funnel_stage: awareness | consideration | conversion | retention
  budget_level: low | medium | high | unknown
  target_city_or_region: <optional>
  languages: <optional>
  existing_assets: <optional>
  first_party_data: none | website_visitors | CRM | app_users | purchasers | unknown
  excluded_channels: <optional>
  must_include_channels: <optional>
  compliance_constraints: <optional>
  hte_findings: <optional, structured or free text>
```

## Core principle

HTE or consumer research usually identifies high-response people and message preferences. Ad platforms usually require executable proxy signals. The central task is to build a mapping layer:

```text
HTE insight / consumer trait
→ platform-recognizable proxy signal
→ campaign setting
→ creative angle
→ measurement plan
→ experiment cell
```

Never claim that a platform can deterministically reach every person in a behavioral group unless the user supplies a deterministic first-party audience list. Use language such as "proxy", "signal", "segment", "approximation", "contextual placement", and "validation experiment".

## Output contract

Return the answer in this structure.

### 1. Activation brief

Summarize the country, audience, goal, main assumptions, and the activation thesis.

### 2. Market and channel assumptions

State the assumptions used for:

- primary languages
- major cities or regions
- platform availability
- ecommerce or offline behavior
- likely purchase journey
- known regulatory or platform policy constraints

When facts may have changed, verify them with current sources and cite them. Use official platform documentation for channel features whenever possible.

### 3. Mainstream reach-channel map

Create a table of mainstream channels for the country. Include both paid and operational channels.

Required columns:

| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |
|---|---|---|---|---|

Cover these channel families unless clearly irrelevant or unavailable:

1. Search engines
2. Paid social
3. Video platforms
4. Display / programmatic / contextual media
5. Retail media and ecommerce marketplaces
6. Local publishers and vertical communities
7. Influencers / creators / KOLs
8. Messaging apps and community operations
9. SEO and content operations
10. CRM, email, SMS, app push, and retargeting
11. Partnerships, affiliates, events, and offline touchpoints

For each country, adapt the concrete platforms. Examples:

- Google Search, YouTube, Google Display, Performance Max
- Meta: Facebook, Instagram, WhatsApp surfaces where relevant
- TikTok
- LinkedIn for B2B or professional audiences
- Reddit, Pinterest, Snapchat, X only when audience-country fit is plausible
- Amazon, Mercado Libre, Allegro, Shopee, Lazada, Flipkart, Coupang, Rakuten, Trendyol, Bol, Tokopedia, eMAG, or local marketplaces where relevant
- LINE, KakaoTalk, WeChat, Telegram, WhatsApp, Messenger, Discord, Viber, or local forums where relevant
- Local search or media platforms such as Baidu, Naver, Yandex, Seznam, Yahoo Japan, Zalo, VK, or country-specific publishers where relevant

### 4. HTE-to-platform mapping

Build a mapping table.

Required columns:

| HTE / audience signal | Consumer meaning | Platform proxy | Channels where usable | Caveats |
|---|---|---|---|---|

Examples of platform proxy signals:

- country, region, city, radius, location presence settings
- language
- age, gender, household, parental status, income proxies where legal and available
- interests and affinity segments
- in-market or purchase-intent segments
- search keywords and match types
- custom intent / custom segments built from keywords, URLs, apps, competitors, creators, or content categories
- contextual topics
- managed placements
- creator or publisher lists
- first-party lists, remarketing pools, lookalikes, similar segments, customer match, consented CRM audiences
- device, operating system, carrier, connection, dayparting, and location context
- feed attributes for retail or shopping campaigns

### 5. Channel execution specs

For each selected high-priority channel, provide an execution spec with the following fields.

```yaml
channel: <platform or channel>
role: <awareness | consideration | conversion | retention>
objective: <campaign objective or operational objective>
setup:
  geography: <country / city / radius / location option>
  language: <language setting and creative language>
  audience:
    included: <segments, keywords, topics, placements, communities>
    excluded: <negative audiences, irrelevant intents, non-service regions>
  inventory_or_placement: <search, feed, reels, shorts, display, creator posts, marketplace ads, etc.>
  bid_or_budget: <bidding method, budget split, pacing>
  creative: <message angles, formats, hooks, localized copy needs>
  landing_or_destination: <landing page, app page, marketplace PDP, lead form, community, store>
  measurement: <primary KPI, secondary KPI, pixel / conversion / UTM requirements>
  operating_cadence: <daily / weekly tasks>
risks:
  - <risk or limitation>
validation_test: <experiment that proves or rejects the setup>
```

### 6. Experiment matrix

Create a test matrix. Each row should isolate one hypothesis.

Required columns:

| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |
|---|---|---|---|---|---|---|

Include at least:

- one intent-based test
- one interest-based test
- one contextual or placement-based test
- one creator / community / publisher test when relevant
- one retargeting or first-party data test when possible

### 7. Measurement and instrumentation

Specify:

- conversion events
- attribution assumptions
- UTM structure
- pixel / SDK / offline conversion requirements
- landing page segmentation
- holdout or incrementality test where feasible
- reporting cadence
- how results should feed back into HTE or segmentation

Recommended UTM schema:

```text
utm_source=<platform>
utm_medium=<paid_social|paid_search|video|display|creator|community|crm|affiliate>
utm_campaign=<country>_<audience>_<objective>
utm_content=<creative_angle>_<format>
utm_term=<keyword_or_segment>
```

### 8. Prioritized launch plan

Provide a phased plan.

```text
Phase 0: tracking, landing page, consent, baseline
Phase 1: highest-intent channels
Phase 2: interest and contextual expansion
Phase 3: creators, communities, partnerships
Phase 4: retargeting, CRM, lookalikes, scaling
```

### 9. Quality checks

Before finalizing, check:

- The plan is country-specific, not a generic global media plan.
- Every channel has an executable audience mechanism.
- Every paid channel includes geography, language, audience, creative, bidding, landing, and measurement.
- Every operational channel includes owner actions, cadence, content format, and KPI.
- Claims about platform availability or targeting features are current or labeled as assumptions.
- The output does not imply deterministic access to behavioral audiences unless first-party data exists.
- Compliance-sensitive targeting is handled conservatively.

## Channel-specific guidance

### Google Search

Use for active intent. Translate the audience into local-language keywords, match types, negative keywords, ad groups, landing pages, and bidding.

Include:

- exact, phrase, and broad match strategy
- negative keyword themes
- local-language terms and English spillover terms where relevant
- city or region campaigns when local behavior differs
- conversion bidding only when tracking is reliable

### Google Display, YouTube, Demand Gen, and Performance Max

Use for interest, intent expansion, video education, remarketing, and scaled conversion.

Include:

- custom segments from keywords, URLs, apps, competitors, creators, and publishers
- contextual topics
- managed placements when high-signal content exists
- audience signals for automated campaigns
- separate remarketing pools
- creative variants by motivation, not just demographics

### Meta: Facebook, Instagram, Messenger, WhatsApp surfaces

Use for broad social reach, interest proxies, lookalikes, community retargeting, and creator-style creative.

Include:

- campaign objective
- location and language
- broad vs interest vs lookalike structure
- Advantage+ or automated setup where appropriate
- excluded purchasers or irrelevant regions
- Reels, Stories, Feed, and click-to-message variants when relevant
- community or group operations if organic presence matters

### TikTok

Use for discovery, creator-led education, trend participation, and lower-friction acquisition.

Include:

- interest and behavior proxies
- creator whitelisting / Spark Ads where applicable
- short-form hooks
- local-language captions
- landing or in-app conversion flow
- rapid creative testing cadence

### Retail media and marketplaces

Use when the product can be discovered or bought in marketplaces.

Include:

- relevant local marketplaces
- sponsored product / sponsored brand / display formats
- category keywords
- product feed quality
- ratings, reviews, price, delivery, and promotion levers
- search rank and retail conversion metrics

### Influencers, creators, and KOLs

Use when the audience has trusted creator niches or when platforms under-represent the segment.

Include:

- creator discovery criteria
- country, language, niche, engagement quality, audience geography
- brief structure
- content rights and paid amplification rights
- coupon, affiliate link, UTM, or post-purchase survey measurement

### Messaging and community operations

Use when the country has strong messaging-app or group behavior.

Include:

- relevant apps and communities
- opt-in mechanism
- moderation and response cadence
- content calendar
- rules for promotions vs support vs education
- referral or ambassador mechanics

### SEO and content

Use for durable intent capture and education.

Include:

- local-language keyword clusters
- comparison, guide, review, and local intent pages
- schema, internal links, and content refresh cadence
- country-specific SERP features

### CRM and retargeting

Use when first-party data exists.

Include:

- consent basis
- segmentation logic
- lifecycle triggers
- suppression rules
- frequency and fatigue controls
- winback and cross-sell paths

## Response style

Be concrete. Prefer parameter tables, setup blocks, experiment matrices, and country-specific examples. Avoid generic statements such as "use social media" without specifying the platform, setup, audience proxy, creative, and measurement.
