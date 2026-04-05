# Offer Stack Playbook

The price architecture that makes a funnel work financially.

The front end exists only to acquire buyers. Margin lives in the stack above it. Brunson, Kennedy, and Kern all use the same five-layer structure. The layers differ in price and format. The logic is identical.

---

## Prerequisites

- [ ] Funnel type selected -- see `funnel-types.md`
- [ ] ICP defined with buying trigger
- [ ] Continuity offer exists or has a build date
- [ ] At least one proof point with a specific number and timeframe

If continuity is missing: build it before scaling the front end. The front end exists to acquire continuity subscribers, not one-time buyers.

---

## The Five Layers

Build in this order. Each layer funds the next.

| Layer | Price range | Job | Unit economics |
|-------|------------|-----|----------------|
| Front-end / tripwire | $0-$97 | Manufacture buyers | Don't need to work at this layer |
| Order bump | 20-50% of front-end | Immediate lift on checkout page | 37.8% avg take rate |
| OTO1 | 51-100% of what buyer just spent | First post-purchase upsell | 16.2% avg take rate |
| OTO2 / downsell | 30-50% of OTO1 | Recovers OTO1 declines | 10-15% take rate |
| Continuity | $47-$297/mo | The actual margin engine | Measured by churn, not conversion |
| Backend / mastermind | ~50x core OTO price | Application-only high-ticket | Feeds from continuity relationships |

### Layer 1 -- Front-end / Tripwire

Price: $0-$97. The only job is manufacturing buyers. Unit economics at this layer do not matter. Paying 100% affiliate commission is viable because the backend pays for the customer.

Do not optimize this layer for profit. Optimize it for buyer count.

### Layer 2 -- Order Bump

Presented on the order form, not a separate page. The buyer has already decided to purchase. The bump removes friction from a second decision.

Rules:
- Price at 20-50% of the front-end price
- One clear line of benefit -- no sub-bullets
- Framed as a complement, not an upgrade

Benchmark: 37.8% average take rate. Below 25%: rewrite the bump copy or lower the price.

### Layer 3 -- OTO1

Fires immediately post-purchase. This is the highest-leverage transaction in the funnel.

Take rate benchmark: 16.2% at 51-100% of what the buyer just spent.

Copy rule: open with identity reinforcement, not a product pitch. The buyer is now a buyer -- treat them as one.

Example opening: "You just made a smart decision. Here's the next one."

Do not open with a feature list. Do not open with a price. Reinforce the identity before presenting the offer.

OTO1 copy rules:
- Stack perceived value with ROI anchors for B2B ("You'd spend $X/month on a hire to get this result")
- Never stack more than 5-6 components
- Guarantee belongs at the end of the close, not the beginning -- placing it earlier signals defensiveness

### Layer 4 -- OTO2 / Downsell

Price: 30-50% of OTO1. Recovers people who declined OTO1. The decision to decline was usually about price, not desire.

Take rate: 10-15%. If below 8%: the price gap between OTO1 and OTO2 is too small, or the downsell is not meaningfully different.

Two downsell formats:
- Reduced scope version of OTO1 at lower price
- Payment plan for OTO1 at same total cost

### Layer 5 -- Continuity

Price: $47-$297/mo. This is the margin engine. Everything above it exists to fill it.

The front end is a customer acquisition mechanism for continuity subscribers. Model the funnel economics around the cost to acquire a continuity subscriber, not the cost to acquire a front-end buyer.

### Layer 6 -- Backend / Mastermind

Price: approximately 50x the core OTO. A $997 OTO implies a $25K-$50K mastermind. Application-only. Does not need volume. Feeds from the relationships built in continuity.

---

## Documented Offer Stacks with Real Numbers

### Brunson / ClickFunnels

$7.95 S&H book -> $37 order bump -> $997 Funnel Hacks OTO -> $1,997 coaching OTO -> $97-$297/mo SaaS -> $50K/yr mastermind.

Average order value on the book funnel: $238.

### Kennedy / GKIC (Brunson-rebuilt)

$0-$1 MIFGE (most incredible free gift ever) -> $117.95 order bumps -> $2,500 swipe file upsell -> $47-$97/mo Gold or $297/mo Diamond continuity.

Average order value: $300 across 5,100 subscribers in month one.

### Kern / Mass Control

Free pre-launch video sequence -> $1,997 limited release ($23.8M in 24 hours) -> book funnel era $19 entry -> $997+ OTO -> application-only backend.

---

## Price Ratio Template

Apply these ratios to any front-end price.

| Layer | Ratio to front-end | Benchmark conversion |
|-------|-------------------|---------------------|
| Front-end | 1x baseline | Varies by funnel type |
| Order bump | 0.2-0.5x front-end | 37.8% avg |
| OTO1 | 0.5-1x front-end | 16.2% avg |
| OTO2 / downsell | 30-50% of OTO1 | 10-15% |
| Continuity | Monthly, ~1-3x front-end | Measured by churn |
| Backend | ~50x core OTO | Application-only |

---

## The Bidding Moat

If your backend LTV is 3-5x a competitor's because you have a profit maximizer and return path, you can outbid them at every ad auction. You acquire customers at a loss they cannot sustain. They get priced out.

This is the structural reason offer stacks matter for paid traffic. A single-product offer competes on margin. A stacked offer competes on LTV.

Build the stack before scaling spend. Scaling spend on a single-product offer is the most common reason paid traffic campaigns fail.

---

## Offer Stack Readiness Checklist

- [ ] Front-end priced for buyer manufacture, not margin
- [ ] Order bump priced at 20-50% of front-end
- [ ] OTO1 opens with identity reinforcement
- [ ] OTO2 exists or is scheduled
- [ ] Continuity offer exists with a price and a churn benchmark
- [ ] Backend pathway exists (even if informal)
- [ ] LTV calculated across all layers

---

## Reference files

- `playbooks/funnel/funnel-types.md` -- pick funnel type before designing the stack
- `playbooks/funnel/high-ticket-backend.md` -- if any layer of the stack is $3K+
- `playbooks/funnel/affiliate-mechanics.md` -- if the front end will be affiliate-distributed
- `playbooks/funnel/vsl-architecture.md` -- how to write the sales assets for each layer
- `playbooks/offer/README.md` -- offer design before funnel architecture
