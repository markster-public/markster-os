# Competitive Intelligence Prompt

**Purpose:** Understand what your buyer already sees when they look at your category. What are competitors claiming? How are they positioning? Where are they weak?

---

## Variables to fill in

- `[CATEGORY]` - the category you compete in (e.g., "B2B email marketing," "sales training for CPA firms," "AI content tools for agencies")
- `[ICP]` - your ICP description (from F1)
- `[GEOGRAPHY]` - the market you are focused on (e.g., "US market," "English-speaking markets," "SMB segment")

---

## Research prompt

Use this prompt in your AI environment (Claude, Gemini, Perplexity, or similar):

---

I am researching the competitive landscape for [CATEGORY] targeting [ICP] in [GEOGRAPHY].

Please help me with the following:

**1. Top competitors**
List the 5-10 most visible companies in [CATEGORY]. For each, provide:
- Their primary positioning claim (the one-liner they use)
- The outcome they promise
- Their most common proof points or claims
- Their pricing model if known
- Any notable weaknesses based on public reviews, complaints, or positioning gaps

**2. Category positioning patterns**
What language does the entire category use? What buzzwords, outcome claims, and value propositions appear across most competitors? (These are the phrases my buyer has already heard and is numb to.)

**3. White space**
What is NOT being said in this category? What real problem is everyone avoiding talking about? What does the buyer care about that none of the competitors are addressing directly?

**4. Differentiation opportunities**
Based on the positioning patterns you found, what 2-3 angles would stand out from the category noise for a buyer who has seen the standard messaging?

---

## Supplementary research to run manually

After running the AI prompt, verify findings with these sources:

- G2 or Capterra reviews of top competitors: what are the most common complaints?
- Reddit threads where your ICP discusses your category: what frustrations do they voice?
- LinkedIn posts by competitors: what tone and content do they push?
- Job postings from competitors: what roles are they hiring? (Reveals strategic priorities)

---

## Output format

Save findings as:

```
COMPETITIVE INTELLIGENCE - [DATE]

Category: [CATEGORY]
ICP: [ICP description]

Top Competitors:
1. [Company] - [Positioning] - [Key weakness]
2. [Company] - [Positioning] - [Key weakness]
3. [Company] - [Positioning] - [Key weakness]
...

Category Language to Avoid:
(phrases that have become invisible to the buyer)
- [phrase]
- [phrase]
- [phrase]

White Space Identified:
[2-3 sentences on what is NOT being addressed]

Differentiation Angles:
1. [Angle 1]
2. [Angle 2]
3. [Angle 3]
```

Feed findings into: F3 (Message) - specifically, the problem statement and the mechanism.
