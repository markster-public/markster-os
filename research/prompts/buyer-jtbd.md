# Buyer Jobs-to-be-Done Prompt

**Purpose:** Surface the functional, emotional, and social jobs your buyer is trying to complete. Find the exact language they use when describing their situation, goals, and frustrations.

---

## Variables to fill in

- `[ICP_DESCRIPTION]` - your ICP (from F1): role, company type, situation
- `[PROBLEM_AREA]` - the broad problem area you help with (e.g., "new client acquisition," "outbound sales," "content marketing")

---

## Research prompt

---

I am mapping the jobs-to-be-done for [ICP_DESCRIPTION] in the area of [PROBLEM_AREA].

**1. Functional jobs**
What are the practical tasks and objectives this person is trying to accomplish in their work related to [PROBLEM_AREA]? List 8-12 specific jobs in plain language (what they are literally trying to do or get done).

**2. Emotional jobs**
What does this person want to feel (or avoid feeling) in relation to [PROBLEM_AREA]? Include both positive goals (what they want to feel) and negative goals (what they are trying to stop feeling).

**3. Social jobs**
How do they want to be perceived by others in relation to this area? What do they want their colleagues, clients, peers, or team to think or say about them?

**4. Pain points**
What frustrations, obstacles, and failures do they encounter in trying to accomplish their functional jobs? Be specific. What breaks down? What takes too long? What does not work?

**5. Their language**
What exact phrases, complaints, and questions does this type of person use when talking about [PROBLEM_AREA]? Look for language that sounds like how a person speaks privately, not how a vendor markets. Include complete sentences where possible.

---

## Supplementary research to run manually

Sources for authentic buyer language:
- Reddit (search for your ICP's industry + problem area)
- LinkedIn posts from people in your ICP's role complaining about the problem
- Amazon reviews for books about the problem area (the 3-star reviews are gold)
- YouTube comments on videos about the problem
- Industry forums and Slack communities
- Your own past client conversations and emails - what exact words did they use?

---

## Output format

```
BUYER JTBD - [DATE]

ICP: [description]
Problem area: [area]

Functional jobs:
1. [specific job]
2. [specific job]
...

Emotional jobs (want to feel):
1. [feeling]
2. [feeling]
...

Emotional jobs (want to stop feeling):
1. [feeling]
2. [feeling]
...

Social jobs:
1. [how they want to be perceived]
2. [how they want to be perceived]
...

Top pain points:
1. [specific frustration]
2. [specific frustration]
...

Verbatims (their actual language):
- "[quote or phrase]"
- "[quote or phrase]"
- "[quote or phrase]"
```

Feed findings into: F3 (Message) - problem statement and proof language. Also use verbatims directly in cold email opening lines.
