# Research Prompt: Pricing & Value Perception Analysis

**To be executed by:** Perplexity, Gemini, or other research-capable LLM
**Estimated time:** 45-60 minutes of research
**Output format:** Markdown document with pricing strategy recommendations

---

## Your Task

You are a pricing strategist. Your client needs to understand how B2B buyers perceive value, what they're willing to pay for growth solutions, and how to price to maximize both win rate and revenue.

**Your job:** Research pricing psychology, competitive pricing strategies, and buyer willingness-to-pay to recommend an optimal pricing structure.

---

## Background Context

**What this type of service sells:**
- AI agents for outbound, content, pipeline (managed service)
- Typical pricing: $3-15K/mo
- Target: B2B service companies, $500K-$5M revenue
- Value prop: Replaces $225K/year in-house team, transparent via approval mode

**The questions:**
- Is $3-15K the right range?
- Should we lead with price or hide it?
- What anchoring strategy should we use?
- How do buyers calculate ROI in their heads?
- What pricing models work best (per-month, per-result, per-seat)?

---

## Research Questions

1. What do B2B companies actually PAY for growth solutions (tools vs agencies vs hires)?
2. How do buyers calculate value/ROI when evaluating growth spend?
3. What pricing strategies do successful competitors use?
4. What psychological pricing tactics work in B2B services?
5. Should pricing be transparent (on website) or hidden (sales-qualified)?

---

## Research Method

### Part 1: Buyer Willingness-to-Pay Research

**Find what B2B buyers are ACTUALLY paying for growth solutions:**

**Sources:**
- Reddit: r/startups, r/entrepreneur, r/sales (search "how much does X cost", "paying $X for agency")
- Indie Hackers: posts about agency costs, tool spend
- LinkedIn: founders posting about "we pay $X for Y"
- Podcasts: SaaStr, My First Million (search "how much we spend on sales")
- G2/Capterra reviews: Often mention price in context ("expensive for what you get" or "great value at $X")

**Search queries:**
- "how much does growth agency cost"
- "paid $X for outbound agency"
- "Clay pricing too expensive"
- "hired SDR salary"
- "marketing agency retainer"

**Extract 15-20 data points:**

| Buyer Profile | What They Bought | Price Paid | Perceived Value | Would Pay More? | Alternative They Considered |
|---------------|------------------|------------|-----------------|----------------|----------------------------|
| $2M SaaS | Agency retainer | $5K/mo | Bad (no results) | No | Hire in-house |
| $3M B2B services | Clay + VA | $400/mo tool + $2K/mo VA | Good | Maybe | 11x.ai ($6K/mo) |
| $1M B2B SaaS | Hired SDR | $80K/year = $6.7K/mo | Mixed (took 6mo to ramp) | No | Would try agency now |
| etc. | | | | | |

**Insights to extract:**
- What's the median spend for tools vs agencies?
- What price point triggers sticker shock? ("too expensive")
- What price point feels like a bargain? ("steal for the value")
- What's the willingness-to-pay range for this ICP?

### Part 2: Competitive Pricing Strategy Analysis

**Analyze how 15-20 competitors handle pricing:**

**For each competitor:**

| Company | Pricing on Website? | Pricing Model | Entry Price | Top Tier Price | Anchoring Strategy | Free Trial/Demo? |
|---------|--------------------|--------------| ------------|----------------|-------------------|-----------------|
| Clay | Yes | Per-seat + usage | $149/mo | $800+/mo | Free trial -> tiers | Yes (14-day) |
| 11x.ai | No | Per-seat | $3K/mo (rumored) | $8K+/mo | "Replace $80K SDR" | No (sales-led) |
| Agency X | No | Retainer | $5K/mo | $15K/mo | "Investment not expense" | No (discovery call) |
| Apollo | Yes | Freemium + paid | $0 (free) | $149/user/mo | Free tier -> upsell | Yes (free forever) |
| etc. | | | | | | |

**Patterns to identify:**
- Tools show pricing (self-serve), services hide pricing (sales-led)
- Entry price for tools: $0-$500/mo
- Entry price for services: $3K-$5K/mo
- Common anchoring: "Replace [expensive thing] with [cheaper thing]"
- Free trials work for PLG tools, not for services

### Part 3: Pricing Psychology Research

**Research B2B pricing tactics that increase conversion:**

**Tactics to validate:**

1. **Anchoring (high -> low):**
   - Show expensive option first to make others feel reasonable
   - Example: "$15K/mo Scale tier" makes "$5K/mo Growth tier" feel like a deal
   - Research: Does this work in B2B? Find examples.

2. **Decoy pricing (3-tier strategy):**
   - Low tier (too basic), Mid tier (perfect), High tier (overkill)
   - Most buyers choose Mid tier
   - Research: Find B2B examples (SaaS pricing pages)

3. **Value metric (what you're paying for):**
   - Per-user (Slack, Salesforce)
   - Per-result (meeting booked, lead generated)
   - Per-service level (Pipeline, Growth, Scale)
   - Research: What metric makes sense?

4. **Comparison pricing (vs alternative):**
   - "$5K/mo vs $225K/year to hire a team"
   - Research: Does this resonate? Find examples from agencies/services.

5. **Transparent vs hidden pricing:**
   - Transparent (on website): Self-serve, PLG, builds trust
   - Hidden (sales-led): High-touch, custom, higher ACV
   - Research: What do buyers prefer for this category?

**Compile findings:**

| Tactic | Description | Works in B2B? | Example | Best for This Service? |
|--------|-------------|---------------|---------|------------------------|
| Anchoring | Show high price first | Yes | Salesforce Enterprise -> Professional | Yes - show high tier first |
| Decoy pricing | 3 tiers, middle is best value | Yes | Most SaaS pricing | Yes - Growth tier as "sweet spot" |
| Value metric | What buyer pays for | Depends | Slack per-user, 11x per-worker | "Per service level" clearer than per-result |
| Comparison pricing | vs alternative cost | Yes | "Replace $80K SDR" | Yes - "$5K vs $225K team" |
| Transparent pricing | Show on website | Mixed | PLG = yes, high-touch = no | Probably no (custom scoping) |

### Part 4: ROI Calculation Research

**How do B2B buyers calculate ROI for growth spend?**

**Find buyer decision frameworks:**
- Reddit/Indie Hackers: "how to calculate if agency is worth it"
- CFO/finance blogs: ROI calculation for marketing spend
- Sales blogs: Payback period, CAC calculations

**Common buyer math:**

**Example 1: Cost per meeting**
> "I'm paying $5K/mo. If they book 10 meetings/mo, that's $500 per meeting. Our ACV is $20K and close rate is 20%, so each meeting is worth $4K. ROI is 8x."

**Example 2: Replacement cost**
> "SDR costs $80K/year = $6.7K/mo. Agency costs $5K/mo and books same meetings. Savings = $1.7K/mo. ROI is immediate."

**Example 3: Time saved**
> "I was spending 40 hours/mo on outbound. My time is worth $150/hr (CEO salary). That's $6K/mo. Agency costs $5K/mo. ROI = $1K/mo in time saved."

**Compile buyer ROI frameworks:**

| ROI Framework | Formula | When Buyers Use This | How to Position |
|---------------|---------|---------------------|-----------------|
| Cost per meeting | Price / Meetings booked | When they have clear meeting goals | "We book X meetings/mo at $Y per meeting" |
| Replacement cost | In-house cost - Our cost | When they're considering hiring | "$225K team vs $3-15K/mo" |
| Time saved | (Hours saved x Hourly rate) - Our cost | When founder is doing it all | "Save 40 hrs/mo = $6K value, pay $5K" |
| Payback period | Months to recover investment | When they're CFO-focused | "Pays for itself in Month 2" |
| Revenue attribution | New revenue / Cost | When they track pipeline closely | "Generated $X pipeline for $Y spend" |

### Part 5: Pricing Transparency Research

**Should pricing be shown on the website?**

**Arguments FOR transparency:**
- Builds trust
- Pre-qualifies leads (cheap shoppers self-select out)
- Speeds up sales cycle
- Works for PLG/self-serve

**Arguments AGAINST transparency:**
- Enables competitors to undercut
- Prospects anchor to low end
- Loses custom pricing flexibility
- High-touch sales can justify higher prices

**Find examples of each:**

| Company | Shows Pricing? | Why? | Does It Work? |
|---------|---------------|------|---------------|
| Gong | No | Enterprise, custom | Yes (Category leader) |
| HubSpot | Yes | PLG + sales-led hybrid | Yes (Grows with customer) |
| Clay | Yes | Self-serve tool | Yes (High adoption) |
| 11x.ai | No | High-touch service | Unknown (young company) |

---

## Expected Output

Deliver a markdown document with these sections:

### 1. Willingness-to-Pay Data
Full table from Part 1 showing what buyers actually pay for growth solutions.

**Insights:**
- Median spend: $X for tools, $Y for agencies, $Z for hires
- Price sensitivity threshold: $X = "too expensive"
- Sweet spot range: $X-Y

### 2. Competitive Pricing Analysis
Full table from Part 2 showing competitor pricing strategies.

**Patterns:**
- Tools: $X-Y range, self-serve
- Services: $X-Y range, sales-led
- Most common entry: $X
- Most common top tier: $Y

### 3. Pricing Psychology Tactics
Full table from Part 3 validating which tactics work in B2B.

**Recommendations:**
- Use [tactic X] because [evidence]
- Avoid [tactic Y] because [evidence]

### 4. Buyer ROI Frameworks
Full table from Part 4 showing how buyers calculate value.

**Lead with:**
1. [Framework X] - because [ICP uses this]
2. [Framework Y] - as secondary justification

### 5. Pricing Visibility Recommendation
Analysis from Part 5.

**Recommendation:**
- Show pricing: Yes/No
- If yes: Show [full pricing / ranges / entry tier only]
- If no: Reasoning + what to show instead ("Custom pricing, book a call")

### 6. Optimal Pricing Structure

Based on all research, recommend:

**Pricing model:** [Retainer / Per-result / Per-seat / Hybrid]

**Pricing tiers:**

| Tier | Price | Positioning | Target Customer | Anchoring |
|------|-------|-------------|-----------------|-----------|
| Pipeline | $3-5K/mo | Entry, essentials | <$1M revenue, founder-led | vs "Hiring SDR for $80K" |
| Growth | $6-9K/mo | Sweet spot | $1-3M revenue, small team | vs "$225K in-house team" |
| Scale | $10-15K/mo | Premium | $3-5M revenue, established | vs "Agency retainer $15-25K" |

**Value metric:** [What they're paying for - service level, not results]

**Comparison anchoring:** "$3-15K/mo vs $225K/year in-house team"

**ROI framing:** Lead with [Framework X], use case study proof

**Pricing visibility:** [Show ranges / Hide pricing / Show entry tier]

### 7. Pricing Page Copy (if showing pricing)

Draft the actual copy for pricing tiers:

**Pipeline Tier**
> **$3,000-5,000/mo**
>
> For early-stage B2B companies ready to scale outbound.
>
> Includes: [bullets]
>
> vs Hiring an SDR: $80K/year

[etc. for other tiers]

---

## Research Tips

- Focus on ACTUAL prices paid (not list prices)
- Look for buyer complaints about price ("too expensive", "worth it")
- Validate psychological tactics with B2B examples (not B2C)
- CFOs and finance teams think differently than founders (find both perspectives)

---

## Deliverable

A single markdown file with all sections - this is your pricing reference for setting rates, positioning value, and justifying cost.
