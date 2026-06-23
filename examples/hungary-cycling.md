# Example: Hungary + People Interested in Cycling

## Input

```yaml
country: Hungary
audience: people interested in cycling
business_context:
  product_or_offer: bicycle accessories ecommerce store
  conversion_goal: purchase
  funnel_stage: conversion
  budget_level: medium
  target_city_or_region: national delivery, with Budapest as a priority market
  languages: Hungarian primary, English secondary test
  first_party_data: website visitors and cart abandoners
  hte_findings:
    - urban commuters respond to convenience and time saving
    - e-bike users respond to lower effort and longer trip distance
    - sport cyclists respond to performance and durability
    - safety-conscious buyers respond to helmets, lights, and locks bundles
```

## 1. Activation brief

| Field | Value |
|---|---|
| Country | Hungary |
| Audience | People interested in cycling |
| Business goal | Ecommerce purchase |
| Funnel stage | Conversion with consideration support |
| Primary activation thesis | Use search and marketplace-like intent to capture active buyers, then use Google, Meta, TikTok, creators, publishers, and retargeting to expand to cycling-interest and urban-mobility audiences. |
| Main assumptions | Hungarian-language creative is the default. Budapest deserves separate budget control. Interest audiences are proxies and need validation. |

## 2. Market and channel assumptions

| Assumption | Working view | Confidence | Validation needed |
|---|---|---|---|
| Primary language | Hungarian first; English as a small test for expats, tourists, or international-brand search behavior | Medium | Check account search terms and landing-page conversion by language |
| Main region | National delivery with Budapest separated for optimization | Medium | Check order density and shipping economics |
| Purchase journey | Search for products, compare price and reviews, then buy online or visit a specialist store | Medium | Validate with analytics, search terms, and post-purchase survey |
| Compliance | Avoid sensitive personal targeting. Use behavior, intent, contextual, and first-party consented audiences | High | Confirm platform policy and local privacy requirements before launch |

## 3. Mainstream reach-channel map

| Channel | Role in funnel | Why it fits this audience | Reach mechanism | Execution priority |
|---|---|---|---|---|
| Google Search | Conversion | Captures users actively searching for bikes, e-bikes, helmets, locks, lights, and repair-related terms | Hungarian keywords, match types, negative keywords, Shopping/PMax if feed exists | High |
| Google YouTube / Demand Gen / Display | Awareness and consideration | Reaches cycling content viewers, e-bike researchers, urban commuters, and outdoor-interest users | Custom segments, topics, placements, video creative, remarketing | High |
| Performance Max | Conversion scaling | Uses feed, creative assets, and audience signals to scale across Google inventory | Audience signals, search themes, product feed, conversion bidding | High if tracking and feed are ready |
| Meta: Facebook and Instagram | Awareness, retargeting, social proof | Broad reach, visual product formats, cycling lifestyle content, retargeting | Broad, interest proxies, lookalikes, Reels, Stories, Feed, catalog ads | High |
| TikTok | Discovery | Works for short-form product demos, commuting hacks, safety tips, and creator-led education | Interest/behavior proxies, Spark Ads, creator briefs, short hooks | Medium |
| Local cycling publishers and forums | Consideration | Cycling enthusiasts trust specialist media and communities | Native ads, newsletters, sponsored articles, managed placements, forum participation | Medium |
| Influencers / creators | Trust and demand creation | Local cyclists, commuters, e-bike reviewers, and sports creators can demonstrate use cases | Creator posts, affiliate links, whitelisting, discount codes | Medium |
| Marketplaces / retail media | Conversion | Users compare price, reviews, delivery, and availability | Sponsored listings, category ads, product feed optimization | Medium, depending on distribution |
| SEO / content | Durable intent | Local-language guides can capture search demand without paid media dependency | Hungarian keyword clusters, comparison pages, buying guides, local cycling guides | Medium |
| CRM / retargeting | Conversion and retention | Website visitors and cart abandoners are higher-intent than cold audiences | Email, SMS, app push, Google/Meta/TikTok retargeting, cart recovery | High if consented data exists |
| Partnerships / offline | Trust and local access | Cycling clubs, repair shops, events, and commuter groups aggregate the audience | Affiliate partnerships, event booths, store collaborations, referral codes | Medium |

## 4. HTE-to-platform mapping

| HTE / audience signal | Consumer meaning | Platform proxy | Channels where usable | Caveats |
|---|---|---|---|---|
| Interested in cycling | General category affinity | Cycling keywords, cycling interests, cycling content topics, bicycle publisher URLs, cycling creator audiences | Google, Meta, TikTok, YouTube, Display, creators | Interest signals are probabilistic, not deterministic |
| Urban commuter | Uses bike for transport | Keywords around city bike, commuter bike, bike lock, bike lights, Budapest cycling; creative about faster city movement | Search, Meta, TikTok, SEO, creators | Platform may not expose exact commuter-cyclist segment |
| E-bike interest | Wants less effort and longer range | e-bike keywords, e-bike review placements, e-bike product categories, custom segments from e-bike URLs | Search, YouTube, Display, PMax, SEO | Distinguish e-bike buyers from general bike users |
| Safety-conscious buyer | Wants helmets, lights, locks | Product keywords, bundle landing page, safety guide, retargeting after product-page visits | Search, Shopping/PMax, Meta catalog, email | Message should avoid fear-based exaggeration |
| Sport cyclist | Cares about performance | road bike, gravel, MTB, lightweight accessories, performance creator placements | Search, YouTube, creators, publishers | Smaller but potentially higher AOV |
| Existing website visitor | Already aware | Retargeting audience, cart abandoner list, viewed category page list | Google, Meta, TikTok, CRM | Requires consent and correct tracking |

## 5. Channel execution specs

### Google Search

```yaml
role: conversion
objective: purchases
setup:
  geography: Hungary; separate Budapest campaign or ad group if volume allows
  language: Hungarian primary; English as a controlled test
  audience:
    included:
      - kerékpár
      - bicikli
      - bringa
      - elektromos kerékpár
      - e-bike
      - városi kerékpár
      - kerékpár sisak
      - bicikli lámpa
      - kerékpár zár
      - kerékpár szerviz Budapest
    excluded:
      - free, used-only, jobs, tutorial-only, irrelevant repair intents if not offered
  inventory_or_placement:
    - Search results
    - Shopping if a product feed exists
  bid_or_budget: start with maximize conversions if purchase tracking is stable; otherwise start with controlled CPC or maximize clicks until conversion data is reliable
  creative:
    angles:
      - safer city riding
      - commuter convenience
      - e-bike comfort
      - accessory bundles
      - fast national delivery
    formats:
      - responsive search ads
      - sitelinks to helmets, locks, lights, e-bike accessories
  landing_or_destination: Hungarian product category pages and bundle pages
  measurement:
    primary_kpi: purchase CPA or ROAS
    secondary_kpis:
      - conversion rate
      - search term quality
      - new customer rate
    tracking:
      - purchase conversion
      - enhanced conversions where available
      - UTM by ad group and keyword theme
  operating_cadence:
    daily:
      - check spend, disapprovals, and tracking anomalies
    weekly:
      - review search terms, add negatives, split high-performing themes
risks:
  - Generic cycling terms may attract low-intent traffic.
validation_test: Compare exact/phrase high-intent accessory terms against broader cycling terms on CPA and ROAS.
```

### Google YouTube / Demand Gen / Display

```yaml
role: awareness and consideration
objective: engaged sessions and assisted conversions
setup:
  geography: Hungary, with Budapest reporting split
  language: Hungarian creative
  audience:
    included:
      - custom segment keywords: kerékpár, bicikli, bringa, e-bike, gravel bike, mountain bike, kerékpárút, kerékpár sisak
      - custom segment URLs: local cycling publishers, bike shops, cycling associations, e-bike review sites
      - contextual topics: cycling, outdoor recreation, fitness, urban mobility where available
      - remarketing: product-page visitors and cart abandoners
    excluded:
      - purchasers from the last 30 to 90 days unless cross-sell is intended
      - kids content and low-quality placements
  inventory_or_placement:
    - YouTube in-stream / Shorts where appropriate
    - Demand Gen feed placements
    - Display contextual placements
  bid_or_budget: optimize to engaged sessions first if conversion volume is thin; use conversion bidding for remarketing and high-signal custom segments
  creative:
    angles:
      - commute faster in Budapest
      - ride safer after dark
      - e-bike accessories for longer trips
      - weekend cycling essentials
    formats:
      - 6 to 15 second video
      - short product demo
      - static bundle image
      - carousel where available
  landing_or_destination: segmented landing pages for commuter, safety, e-bike, and sport accessories
  measurement:
    primary_kpi: assisted conversion CPA or qualified visit rate
    secondary_kpis:
      - view rate
      - CTR
      - engaged sessions
      - remarketing pool growth
    tracking:
      - UTM content by creative angle
      - video engagement audiences
  operating_cadence:
    daily:
      - monitor spend and poor placements
    weekly:
      - refresh weak creatives and review placement reports
risks:
  - Interest segments can overreach into general sports traffic.
validation_test: Test custom keyword segment vs contextual cycling placements vs remarketing on qualified visit rate and assisted conversion rate.
```

### Performance Max

```yaml
role: conversion scaling
objective: purchases or ROAS
setup:
  geography: Hungary
  language: Hungarian
  audience:
    included:
      - audience signal: cycling custom segment
      - audience signal: product page visitors
      - search themes: kerékpár, bicikli, e-bike, kerékpár sisak, kerékpár zár, bicikli lámpa
    excluded:
      - unavailable product categories
      - non-service regions if delivery is limited
  inventory_or_placement:
    - Search, Shopping, YouTube, Display, Discover, Gmail depending on availability and setup
  bid_or_budget: maximize conversion value or target ROAS after purchase tracking and feed quality are stable
  creative:
    angles:
      - bundles
      - delivery
      - safety
      - commute convenience
    formats:
      - asset groups by commuter, safety, e-bike, sport
  landing_or_destination: product feed and category URLs; avoid sending all traffic to the homepage
  measurement:
    primary_kpi: ROAS
    secondary_kpis:
      - purchase volume
      - new customer value
      - category-level margin
    tracking:
      - purchase value
      - product feed diagnostics
      - campaign asset reporting
  operating_cadence:
    daily:
      - check feed errors and budget pacing
    weekly:
      - review asset group performance and search term insights where available
risks:
  - Audience signals guide the model but do not hard-restrict delivery.
validation_test: Compare PMax with cycling-specific asset groups against generic all-products PMax on ROAS and new-customer rate.
```

### Meta: Facebook and Instagram

```yaml
role: awareness, consideration, retargeting
objective: purchases or landing-page views depending on tracking maturity
setup:
  geography: Hungary; Budapest split if budget allows
  language: Hungarian
  audience:
    included:
      - broad Hungary audience with cycling creative
      - cycling and outdoor interest proxies where available
      - lookalikes from purchasers or high-quality visitors if data volume allows
      - retargeting: viewed product, added to cart, engaged with Instagram/Facebook
    excluded:
      - recent purchasers unless cross-sell campaign
      - low-value website visitors if enough data exists
  inventory_or_placement:
    - Reels
    - Stories
    - Feed
    - catalog ads if product feed exists
  bid_or_budget: start with broad + creative segmentation; allocate separate budget to retargeting if audience size supports it
  creative:
    angles:
      - before/after commute friction
      - helmet and light bundle
      - lock quality demonstration
      - weekend ride packing list
    formats:
      - UGC-style short video
      - carousel
      - product catalog
      - social proof image
  landing_or_destination: product category page, bundle page, or catalog shopping flow
  measurement:
    primary_kpi: purchase CPA or ROAS
    secondary_kpis:
      - thumb-stop rate
      - CTR
      - add-to-cart rate
    tracking:
      - pixel and conversion API where available
      - UTM by creative angle and placement
  operating_cadence:
    daily:
      - monitor spend and creative fatigue
    weekly:
      - rotate hooks and pause weak angles
risks:
  - Platform interest labels may be broad; creative and post-click behavior must validate fit.
validation_test: Broad audience with cycling creative vs interest-proxy audience vs retargeting on add-to-cart rate and CPA.
```

### TikTok

```yaml
role: discovery and demand creation
objective: engaged visits, add-to-cart, or purchases after signal volume improves
setup:
  geography: Hungary
  language: Hungarian captions and voiceover where possible
  audience:
    included:
      - cycling, fitness, outdoor, commuting, e-bike, gadget, and safety content proxies where available
      - engagement retargeting from video viewers
      - website retargeting if pixel is active
    excluded:
      - recent purchasers unless cross-sell campaign
  inventory_or_placement:
    - short-form in-feed video
    - creator posts or Spark Ads where available
  bid_or_budget: small creative-test budget first; scale only winning hooks
  creative:
    angles:
      - three things every Budapest cyclist needs
      - e-bike accessory checklist
      - night riding safety setup
      - bike lock test
    formats:
      - 9:16 UGC-style video
      - creator demonstration
      - product checklist
  landing_or_destination: mobile-first landing page or product page
  measurement:
    primary_kpi: qualified visit or add-to-cart CPA
    secondary_kpis:
      - hook rate
      - video completion
      - CTR
    tracking:
      - pixel
      - UTM by hook
      - creator code where applicable
  operating_cadence:
    daily:
      - review creative-level spend and early engagement
    weekly:
      - produce new hooks from comments and search terms
risks:
  - Discovery traffic may not convert immediately.
validation_test: Test creator demo vs product checklist vs commute-problem hook on add-to-cart rate.
```

### Local cycling publishers and communities

```yaml
role: consideration and trust
objective: qualified referral traffic and authority building
setup:
  geography: Hungary
  language: Hungarian
  audience:
    included:
      - readers of cycling media
      - members of cycling forums or Facebook groups
      - e-bike and commuter cycling communities
    excluded:
      - communities where commercial posting is prohibited
  inventory_or_placement:
    - sponsored article
    - newsletter placement
    - banner or native ad
    - buying guide contribution
    - forum participation under community rules
  bid_or_budget: fixed placement fees, sponsorship package, or affiliate commission
  creative:
    angles:
      - commuter gear guide
      - safety checklist
      - e-bike accessory guide
      - Budapest cycling essentials
    formats:
      - long-form article
      - checklist PDF
      - newsletter feature
      - community Q&A
  landing_or_destination: guide page with product modules and UTM tracking
  measurement:
    primary_kpi: qualified referral sessions and assisted revenue
    secondary_kpis:
      - newsletter clicks
      - guide engagement
      - coupon usage
    tracking:
      - UTM by publisher
      - exclusive coupon code
      - post-purchase survey
  operating_cadence:
    weekly:
      - review referral quality and negotiate content follow-ups
risks:
  - Publisher traffic can be small but high-quality.
validation_test: Compare sponsored guide vs newsletter placement vs banner/native ad on engaged session rate and assisted revenue.
```

### Influencers and creators

```yaml
role: trust, education, and demand creation
objective: creator-sourced purchases and reusable creative assets
setup:
  geography: Hungary
  language: Hungarian
  audience:
    included:
      - urban cycling creators
      - e-bike reviewers
      - MTB / road / gravel creators
      - commuter lifestyle creators
    excluded:
      - creators with weak Hungarian audience match
      - inflated engagement or poor comment quality
  inventory_or_placement:
    - Instagram Reels
    - TikTok videos
    - YouTube Shorts or reviews
    - blog reviews
    - whitelisted paid amplification where rights are granted
  bid_or_budget: fixed fee plus affiliate or coupon bonus; reserve usage-rights budget for paid amplification
  creative:
    angles:
      - real commute setup
      - night ride safety
      - lock stress test
      - e-bike trip essentials
    formats:
      - demo video
      - checklist
      - ride-along
      - product review
  landing_or_destination: creator landing page or product collection
  measurement:
    primary_kpi: creator CPA or assisted revenue
    secondary_kpis:
      - saves
      - comments with purchase intent
      - coupon use
      - paid amplification CPA
    tracking:
      - UTM link
      - creator code
      - affiliate link
      - post-purchase survey
  operating_cadence:
    weekly:
      - review creator pipeline, content approvals, and performance
risks:
  - Creator audience quality varies; require audience geography screenshots and comment review.
validation_test: Run 5 to 10 micro-creators by segment, then whitelist the top 2 creatives into paid social.
```

### CRM and retargeting

```yaml
role: conversion and retention
objective: recover high-intent visitors and increase repeat purchase
setup:
  geography: Hungary where consented
  language: Hungarian
  audience:
    included:
      - cart abandoners
      - product page viewers
      - past purchasers for cross-sell
      - email subscribers
    excluded:
      - refunded orders
      - unsubscribed users
      - recent purchasers from acquisition campaigns
  inventory_or_placement:
    - email
    - SMS if consented
    - app push if applicable
    - Google, Meta, TikTok retargeting
  bid_or_budget: separate remarketing budget with frequency control
  creative:
    angles:
      - complete your cycling setup
      - helmet + light bundle
      - free shipping threshold
      - seasonal maintenance checklist
    formats:
      - lifecycle email
      - dynamic catalog ad
      - abandoned-cart reminder
      - product recommendation
  landing_or_destination: cart, saved products, or personalized collection
  measurement:
    primary_kpi: recovered revenue
    secondary_kpis:
      - open rate
      - click rate
      - unsubscribe rate
      - frequency
    tracking:
      - email campaign IDs
      - pixel retargeting audiences
      - suppression lists
  operating_cadence:
    daily:
      - monitor deliverability and automation errors
    weekly:
      - review revenue per recipient and fatigue
risks:
  - Over-retargeting can create fatigue and inflated attribution.
validation_test: Add a holdout group for cart recovery and compare incremental recovered revenue.
```

## 6. Experiment matrix

| Test cell | Channel | Audience proxy | Creative angle | KPI | Success threshold | Next action |
|---|---|---|---|---|---|---|
| A | Google Search | Exact/phrase accessory keywords | Safety bundle | Purchase CPA | CPA at or below target | Expand terms and landing pages |
| B | Google Search | Broad cycling terms | Commuter convenience | Search-term quality and CPA | Search terms remain relevant and CPA within 20 percent of target | Keep only converting broad clusters |
| C | YouTube / Demand Gen | Custom cycling keyword + URL segment | Night riding safety | Qualified visit rate | Beats generic outdoor segment by 25 percent | Scale custom segment and test new videos |
| D | Meta | Broad Hungary audience | UGC commute setup | Add-to-cart CPA | Beats interest audience or has higher scale at similar CPA | Move budget to broad + best creatives |
| E | TikTok | Cycling / outdoor behavior proxy | Three essentials for Budapest cyclists | Hook rate and add-to-cart CPA | Best hook clears creative benchmark and adds to cart efficiently | Produce variants with same hook |
| F | Creator | Hungarian cycling micro-creators | Product demonstration | Creator-sourced purchases | At least one creator beats paid social CPA after amplification | Whitelist top creator content |
| G | CRM | Cart abandoners | Complete your setup | Incremental recovered revenue | Holdout-adjusted revenue positive | Scale automation and tune cadence |

## 7. Measurement and instrumentation

### Conversion events

| Event | Definition | Source | Required setup |
|---|---|---|---|
| Purchase | Completed ecommerce transaction | Website | Pixel, analytics purchase event, order value, currency |
| Add to cart | Product added to cart | Website | Pixel and analytics event |
| Product view | Cycling accessory PDP view | Website | Pixel and analytics event |
| Qualified visit | Session with product view or minimum engagement threshold | Analytics | UTM and event tracking |
| Creator sale | Purchase from creator code or link | Ecommerce / affiliate system | Unique code, UTM, post-purchase survey |

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
| Daily | Check spend, tracking, disapprovals, stock issues, broken URLs |
| Weekly | Review search terms, creative fatigue, audience proxy performance, placement quality, creator pipeline |
| Monthly | Reallocate budget by incremental performance, update HTE mapping, refresh landing pages and SEO priorities |

### Feedback loop into HTE

```text
platform proxy performance
→ compare conversion lift by audience signal and creative angle
→ identify which proxy best represents the HTE segment
→ update audience definition and campaign weights
```

## 8. Prioritized launch plan

| Phase | Timing | Actions | Exit criteria |
|---|---|---|---|
| Phase 0: foundation | Week 0 | Tracking, product feed, Hungarian landing pages, consent, UTM schema, baseline reporting | Purchase and add-to-cart tracking reliable |
| Phase 1: intent capture | Weeks 1-2 | Google Search, Shopping or PMax if feed ready, retargeting | Stable search-term quality and first purchase benchmark |
| Phase 2: audience expansion | Weeks 2-4 | Meta, YouTube/Demand Gen, TikTok creative tests | Identify 2 to 3 winning proxy + creative combinations |
| Phase 3: trust channels | Weeks 3-6 | Creators, local cycling publishers, community-safe content | At least one creator or publisher proves qualified traffic or sales |
| Phase 4: scale and retention | Week 6+ | Scale winners, CRM sequences, lookalikes, holdout testing | Incremental revenue supports larger budget |

## 9. Quality checks

- This plan uses Hungary-specific language assumptions and a Budapest reporting split.
- The cycling audience is translated into search, interest, custom segment, contextual, creator, community, and first-party proxies.
- Each paid channel includes geography, language, audience, creative, budget, landing, and measurement.
- Operational channels include cadence, content format, and KPIs.
- The plan treats platform audiences as proxies and requires validation experiments.
