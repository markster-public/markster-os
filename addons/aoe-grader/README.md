# AOE Grader - AI Visibility Scorer

Score your company's visibility to AI-powered buying tools. Know exactly how LLMs, AI search engines, and AI-assisted research tools perceive your brand when a buyer asks about your category.

---

## What it does

When a buyer researches your category using an AI tool (Claude, Perplexity, ChatGPT, Gemini), the AI generates a response based on what it knows about your market. AOE Grader measures how prominently - and how accurately - your company appears in those responses.

**What you get:**

- An AOE Score (0-100) rating your AI visibility in your category
- A breakdown of which AI tools mention you and how
- The language AI tools use to describe your company
- Competitor comparison: how your AI visibility stacks up against the top 5 players in your category
- A gap analysis: what content and signals would improve your score
- Recommended actions prioritized by expected impact

---

## Why it matters

Buyers are increasingly using AI tools to research vendors before ever reaching out. If your company does not appear - or appears inaccurately - in AI-generated answers, you are invisible to a growing segment of buyers in the research phase.

This is the new version of "not ranking on Google page 1." And like SEO in 2008, most companies have not started optimizing for it yet.

---

## Integration with skills

When `AOE_GRADER_KEY` is set, the following skills gain AI visibility features:

| Skill | What unlocks |
|-------|-------------|
| `/research` | AI visibility audit as part of competitive intelligence |
| `/content` | Content recommendations optimized to improve AOE score |
| `/cold-email` | Awareness of how AI-aware your ICP contacts already are |

---

## Setup

**Step 1: Get a key**

Sign up at [markster.ai/addons/aoe-grader](https://markster.ai/addons/aoe-grader).

Free tier: 1 full audit per month.
Paid plans: from $49/month for unlimited audits + monthly score tracking.

**Step 2: Set the environment variable**

```bash
export AOE_GRADER_KEY="your_key_here"
```

**Step 3: Run your first audit**

In your AI environment:

```
/research
```

Select "AI visibility audit" from the research menu. The skill will ask for your company name, category, and target keywords, then return your full AOE Score report.

---

## Sample output

```
AOE SCORE REPORT - [Company Name]
Category: [category]
Score: 64/100

AI Tool Coverage:
- Claude: Mentioned in 3/5 category queries (relevant context, accurate)
- Perplexity: Mentioned in 1/5 category queries (limited context)
- ChatGPT: Not mentioned in top results
- Gemini: Mentioned in 2/5 category queries (mentioned alongside 8 competitors)

Top gap: You are not appearing when buyers search for "[specific query]"
Top recommendation: Publish [specific content type] addressing [specific topic] to increase coverage in this query type.

Competitor comparison:
[Competitor 1]: 82/100
[Competitor 2]: 71/100
[Your company]: 64/100
[Competitor 3]: 58/100
```

---

## Questions

AOE Grader support: addons@markster.ai
Docs: [markster.ai/docs/aoe-grader](https://markster.ai/docs/aoe-grader)
