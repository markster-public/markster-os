# Objection Research Prompt

**Purpose:** Surface the specific objections, hesitations, and skepticisms your ICP carries into vendor conversations. Use to prepare cold email follow-up responses, discovery call objection handling, and proposal risk reversals.

---

## Variables to fill in

- `[ICP_DESCRIPTION]` - your ICP (from F1)
- `[SOLUTION_CATEGORY]` - what your solution helps with
- `[COMMON_FAILURE_MODES]` - what typically goes wrong when buyers try to solve this problem themselves or with a vendor

---

## Research prompt

---

I am mapping the objections and hesitations of [ICP_DESCRIPTION] when considering purchasing [SOLUTION_CATEGORY].

The common failure modes they have experienced (or heard about) include: [COMMON_FAILURE_MODES]

**1. Primary objections**
What are the top 5 reasons this buyer type does not buy, or delays buying?
- Include both stated objections (what they say) and real objections (what they actually mean)
- Include pre-conversation objections (what makes them not reply to outreach) and in-conversation objections (what comes up after they are engaged)

**2. Past experience objections**
What bad experiences with vendors in this category are they carrying? What went wrong for them (or for someone they know)?
- What did the vendor promise that did not materialize?
- What was the failure mode? (Slow, generic, too much work for the buyer, results unclear)
- How does this past experience affect how they evaluate new vendors?

**3. Internal objections**
What internal political or organizational factors create hesitation?
- Who else needs to approve?
- What competing priorities make this a lower priority?
- What previous commitments (other vendors, internal projects) make it harder to say yes?

**4. Objection responses that work**
For each of the top 3 objections, what response would:
- Acknowledge the objection without dismissing it
- Address the root cause (not just the surface statement)
- Move the conversation forward

---

## Output format

```
OBJECTION RESEARCH - [DATE]

ICP: [description]
Solution: [what you offer]

Top 5 objections:
1. [Stated]: "[what they say]" / [Real]: [what they actually mean]
2. [Stated]: "[what they say]" / [Real]: [what they actually mean]
3. [Stated]: "[what they say]" / [Real]: [what they actually mean]
4. [Stated]: "[what they say]" / [Real]: [what they actually mean]
5. [Stated]: "[what they say]" / [Real]: [what they actually mean]

Past experience baggage:
- [What went wrong before]
- [What this creates in their evaluation process]

Internal blockers:
- [political / organizational factors]

Response frameworks:
Objection 1: [how to address it]
Objection 2: [how to address it]
Objection 3: [how to address it]

Risk reversal design based on top objection:
[What risk reversal removes the dominant objection]
```

Feed findings into:
- F2 (Offer): risk reversal design
- Cold email follow-up templates: `playbooks/cold-email/templates/follow-up.md`
- Discovery call preparation: `playbooks/biz-dev/sales/templates/discovery-call.md`
