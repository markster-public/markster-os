# Marketplace (2-Sided)

Covers: B2B marketplaces, B2C marketplaces, gig platforms, aggregators, exchange models.

What unifies these: you have two distinct ICPs (supply side and demand side), value for one side depends on the other side being there, and the hard problem is always liquidity -- getting both sides dense enough that the marketplace works.

---

## What is different about GTM

You are not running one G1/G2/G3 cycle. You are running two simultaneously, and they are sequenced: supply first, then demand (in most cases).

The classic mistake is launching to both sides at the same time. You get thin supply, thin demand, zero matches, and both sides leave. Seed one side to density in a narrow market before opening the other.

The revenue model is a transaction fee (rake). Typical rake: 5-30% depending on category. The unit economics question is not LTV:CAC in the traditional sense -- it is: does GMV grow faster than the cost to acquire and retain both sides?

---

## GOD Engine priorities by stage

| Stage | Priority bricks | What to skip |
|-------|----------------|--------------|
| Stage 0-1 | G1 Find (both ICPs), G3 Book (manual matching, high-touch), D1 Deliver (make first transactions work manually) | O2 Automate -- do it manually until the pattern is clear |
| Stage 2 ($100K-500K GMV/mo) | O1 Standardize (the matching and onboarding process), G2 Warm (supply-side community), D2 Prove | -- |
| Stage 3 ($500K-2M GMV/mo) | O2 Automate (matching, payments, onboarding), O3 Instrument (liquidity ratios), D3 Expand | -- |
| Stage 4 | Geographic or vertical expansion, full automation, enterprise/API layer | -- |

---

## Key metrics

| Metric | What it measures | Healthy benchmark |
|--------|-----------------|-------------------|
| GMV (Gross Merchandise Value) | Total transaction volume through the platform | Primary growth metric |
| Take rate | Revenue as % of GMV | 5-30% depending on category |
| Liquidity ratio | % of supply-side listings that result in a transaction | 20%+ per period for healthy marketplace |
| Fill rate | % of demand-side requests that find a match | 70%+ to avoid abandonment |
| Supply-side retention | % of active suppliers returning month-over-month | 60%+ monthly for healthy supply |
| CAC (both sides) | Cost to acquire a supplier and a buyer | Both should be recoverable from transaction revenue |

---

## Biggest failure modes

1. **Launching both sides simultaneously without seeding supply.** The result is a dead marketplace. Pick a narrow geography or vertical, seed supply manually, then invite demand.

2. **Building the platform before proving the transaction.** Do the first 10-50 transactions manually (Google Sheets, email, phone). Understand what breaks before building automation.

3. **Optimizing for signups, not transactions.** A marketplace with 10,000 users and zero transactions is not a business. Optimize for completed transactions from day one.

4. **Pricing the rake wrong.** Too high and supply goes direct. Too low and the business never makes money. Study comparable marketplaces in your category before setting take rate.

---

## Fundraising path

Marketplaces are VC-fundable when the GMV growth rate is visible and the unit economics on individual transactions work. The TAM argument is the primary pitch: the bigger the total transaction volume in the category, the larger the potential take rate revenue.

Pre-seed to seed: $1M-$5M. Needs: proof of liquidity in a narrow segment, early GMV traction.
Series A: $5M-$20M. Needs: clear GMV trajectory, retention on both sides, path to take rate expansion.

---

## Playbooks to run in order

1. `methodology/foundation/F1-positioning.md` -- define both ICPs separately
2. `playbooks/find/README.md` -- build supply-side list first
3. `playbooks/book/README.md` -- manual outreach to seed supply
4. `playbooks/deliver/README.md` -- the first transactions are the product; make them work manually
5. `playbooks/standardize/README.md` -- once you know what good looks like, write the SOP
6. `playbooks/prove/README.md` -- transaction success stories are your demand-side acquisition tool
