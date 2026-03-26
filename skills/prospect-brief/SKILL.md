---
name: prospect-brief
description: Pre-conversation research tool. Takes a name, company, or LinkedIn URL and generates a phone-readable cheat sheet with ICP fit, conversation strategy, objections to expect, and which proof points to use. Use before any meeting, call, or intentional conversation. Triggers on "research", "who is", "prep for meeting", "brief me on", "about to meet".
---

# Prospect Brief -- ACTIVATED

You are preparing the user for a conversation. Generate a phone-readable cheat sheet.

---

## Process

### 1. Research

From the input (name, company, LinkedIn URL, or any combination):

- Search existing contact database for person + company
- Web search: company website, recent news, LinkedIn profile, funding, team size
- Look for: revenue estimate, employee count, industry, location, tech stack, current marketing approach

### 2. ICP Assessment

Score against ICP criteria:
- **Primary ICP** -- B2B service business, $500K-$5M revenue, 5-50 employees
- **Secondary ICP** -- Adjacent fit
- **Not a fit** -- Disqualification flags present

Note specific fit signals or disqualification reasons.

### 3. Conversation Strategy

Based on their situation:
- **Lead with:** Which pitch variation fits this audience
- **Expect:** Top 2-3 objections with one-line responses
- **Prove with:** Most relevant proof point for their industry
- **Competitor context:** Are they likely using any competing tools/agencies?

### 4. Generate Brief

**Output -- optimized for phone screen:**

```
PROSPECT BRIEF

[Name] -- [Title]
[Company] -- [Industry] -- [~Size] -- [Location]
ICP Fit: [Primary/Secondary/Not a fit] -- [one-line reason]

THEIR SITUATION
- [Key fact about the company]
- [Key fact about the person]
- [Pain signal or opportunity]
- [Current marketing/sales approach if known]

CONVERSATION PLAN
- Lead with: "[specific pitch variation]"
- Proof point: [most relevant stat or case study]
- Ask about: [good discovery question for their situation]

EXPECT THESE OBJECTIONS
1. "[Objection]" -> [one-line response]
2. "[Objection]" -> [one-line response]

ONE THING TO REMEMBER
[The single most important insight about this prospect]
```

---

## Rules

- Keep it scannable -- the user reads this on their phone before walking into a meeting
- Be specific -- "they're a 30-person MSP in Oakland" not "they're a tech company"
- If you can't find much data, say so -- don't pad with guesses
- Always include objection pre-loads -- the conversation will go better
- If there's an existing deal history, include it
