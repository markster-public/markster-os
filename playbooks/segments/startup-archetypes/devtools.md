# Developer Tools, API, and Open Source

Covers: developer tools (CLI, SDK, IDE plugins), API products, infrastructure/platform products, open source + commercial (open core).

What unifies these: your buyer is a developer or engineer, adoption is bottom-up (the practitioner uses it before the company buys it), and the community is part of the product.

---

## What is different about GTM

Developers do not respond to sales. They respond to documentation, GitHub activity, and peer recommendation. The G2 Warm brick here is GitHub stars, technical blog posts, conference talks, and developer community presence -- not LinkedIn content or cold email sequences.

The sequence for open source + commercial: build OSS community first, charge for managed hosting or enterprise features second. Skipping the community step and going straight to enterprise sales fails because there is no proof of adoption.

For API products: usage-based pricing means your revenue is a function of volume. The Stage 1 metric is not MRR, it is API call growth and the number of active consumers.

---

## GOD Engine priorities by stage

| Stage | Priority bricks | What to skip |
|-------|----------------|--------------|
| Stage 0-1 | G1 Find (developer ICP), G2 Warm (OSS/community), G3 Book (self-serve, not sales calls) | Sales-led G3 -- wrong motion for this stage |
| Stage 2 ($100K-500K ARR) | D2 Prove (case studies for enterprise), G3 Book (now enterprise sales), O1 Standardize | -- |
| Stage 3 ($500K-2M ARR) | D3 Expand (usage expansion within accounts), O3 Instrument, G2 at scale | -- |
| Stage 4 ($2M+ ARR) | Enterprise sales motion, O2 Automate developer onboarding | -- |

Note: the path from community to enterprise revenue takes 12-24 months. This is not a slow sales cycle -- it is a different acquisition model. Plan accordingly.

---

## Key metrics

| Metric | What it measures | Healthy benchmark |
|--------|-----------------|-------------------|
| GitHub stars / weekly active contributors | OSS health and discoverability | Context-dependent; trajectory matters more than absolute |
| Active API consumers | Real adoption, not just signups | Growth rate 10%+ MoM at Stage 1 |
| API call volume | Usage expansion | Leading indicator of revenue for usage-based |
| Trial-to-paid conversion | Self-serve funnel | 3-8% for developer tools |
| Expansion revenue | Usage growth within accounts | Net expansion should exceed churn |
| Enterprise ACV | Average contract value for paid tier | $15K-$100K+ for true enterprise |

---

## Biggest failure modes

1. **Charging too early.** Monetizing before the OSS community is real kills adoption. Developers talk. A premature paywall becomes a reputation problem.

2. **Building for developers but selling to procurement.** Developer tools have a bottom-up motion. Marketing to C-suite before developers are already using the product is backwards.

3. **No enterprise tier.** Open source without a commercial path is a charity. The enterprise tier (SSO, audit logs, SLA, dedicated support) is what makes the business model work.

4. **Documentation as an afterthought.** For developer tools, documentation is the product. Poor docs kill adoption faster than poor features.

---

## Fundraising path

Pre-seed to seed: GitHub activity and developer adoption are the traction signal. Revenue is secondary at this stage.
Seed: $2M-$8M. Needs: meaningful OSS adoption (10K+ stars or real enterprise pilots).
Series A: $5M-$20M. Needs: $1M+ ARR, enterprise contracts, clear expansion motion.

Non-VC path: consulting or integration services can fund early development while OSS grows.

---

## Playbooks to run in order

1. `methodology/foundation/F1-positioning.md` -- define the developer ICP precisely (language, tools, problem)
2. `playbooks/warm/content/README.md` -- technical content is your G2 engine
3. `playbooks/find/README.md` -- GitHub, HN, Reddit communities are your list source
4. `playbooks/book/README.md` -- self-serve first, enterprise sales after adoption is proven
5. `playbooks/prove/README.md` -- developer case studies and integration stories
6. `playbooks/expand/README.md` -- usage expansion and enterprise upsell
