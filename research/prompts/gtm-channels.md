# GTM Channels Prompt

**Purpose:** Identify which channels your ICP actually uses for vendor discovery, research, and decision-making. Use to validate and refine your F4 channel selection.

---

## Variables to fill in

- `[ICP_DESCRIPTION]` - your ICP (from F1)
- `[SOLUTION_CATEGORY]` - what your solution helps with
- `[DEAL_SIZE]` - your typical deal size

---

## Research prompt

---

I am mapping the GTM channel behavior of [ICP_DESCRIPTION] when they are evaluating or purchasing [SOLUTION_CATEGORY] at approximately [DEAL_SIZE].

**1. Discovery channels**
How does this buyer type first become aware of vendors in your category?
- Where do they hear about new solutions? (peer recommendations, conferences, content, LinkedIn, search, communities, newsletters, podcasts)
- What is the most common way they find a vendor they eventually buy from?
- What sources do they distrust for vendor discovery?

**2. Research channels**
After becoming aware of a vendor, where do they go to learn more and validate?
- What review sites or comparison tools do they use?
- Who do they ask? (Peers, advisors, community members?)
- What content format do they prefer for evaluation? (Case studies, demos, articles, calls with references)
- How long does the research phase typically last for a purchase in this size range?

**3. Outreach receptivity**
How does this buyer type respond to different outbound approaches?
- Cold email: do they engage? At what rate? What gets them to reply?
- LinkedIn cold message: receptive or annoying?
- Phone: acceptable or immediately off-putting?
- Video message: novel or intrusive?
- Events and conferences: high or low effectiveness for first-touch?

**4. Trust transfer channels**
What introductions or endorsements carry the most weight with this buyer?
- Referral from a current customer
- Referral from a professional advisor (accountant, consultant)
- Endorsement in a community they are part of
- Endorsement from a known name in their industry
- Content they found and came to you from

**5. Decision timing**
At what point in the buying process does this buyer type typically engage with a vendor?
- Very early (before they have defined the solution)
- Mid-research (comparing options)
- Late-stage (they know what they want, validating execution)

---

## Output format

```
GTM CHANNELS - [DATE]

ICP: [description]
Solution: [what you offer]
Deal size: [range]

Primary discovery channel: [channel]
Secondary discovery channel: [channel]

Research behavior:
- [what they do to evaluate vendors]
- [how long it takes]
- [who they ask]

Outreach receptivity:
- Cold email: [high / medium / low] - [reason]
- LinkedIn cold: [high / medium / low] - [reason]
- Events: [high / medium / low] - [reason]
- Referral: [high - baseline for all buyer types]

Highest trust transfer: [what intro or endorsement carries the most weight]

F4 channel recommendation (updated):
Primary: [channel - justified by above]
Support: [channel - justified by above]
```

Feed findings into: F4 (Channel) - validate or update your channel selection.
