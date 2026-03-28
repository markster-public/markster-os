# O2: Automate

**Pillar:** Operations
**North Star:** Hours saved per week through automation

---

## What It Covers

Workflow automation, AI agents, email automation, document generation, scheduling automation, reporting automation, and integration building.

O2 removes manual work from processes that have already been documented (O1). The rule: standardize first, then automate. Never automate an undocumented process -- you are scaling the wrong thing.

---

## Key Questions It Answers

- Which manual tasks consume the most hours relative to their value?
- What is the minimum viable automation that saves the most time first?
- How do we test automations so failures are caught before they affect clients?
- When is AI the right tool versus simple automation?
- What does a reliable automation stack look like for a team under 20 people?

---

## Metrics

| Metric | Target |
|--------|--------|
| Hours saved per week | 20-40+ |
| Automation success rate | 95%+ |
| Manual tasks as % of total volume | Under 20% |
| Error rate on automated processes | Under 5% |

---

## Automation Priority Matrix

Score each candidate automation:

| Factor | Weight | Scoring |
|--------|--------|---------|
| Time saved (hours/week) | 30% | 1-10 |
| Frequency (times per week) | 25% | 1-10 |
| Error reduction potential | 20% | 1-10 |
| Complexity to implement | 15% | 1-10 (inverse: 1=complex) |
| Risk if it fails | 10% | 1-10 (inverse: 1=high risk) |

Automate the highest-scoring candidates first. Do not automate anything with a complexity score below 3 before documenting the manual process well.

---

## Automation Design Template

```
Purpose: [what this automation replaces or enables]
Trigger: [what starts the automation]
Inputs: [data or files required]
Logic: [what the automation does, step by step]
Outputs: [what it produces or sends]
Error Handling: [what happens when it fails]
Monitoring: [how you verify it is running correctly]
Owner: [who is accountable for maintaining it]
Dependencies: [tools, APIs, or data sources it requires]
```

---

## Common Failures

**Automating before documenting:** Running Make or Zapier workflows on processes that are not yet written down. The automation encodes the current broken process, and fixing it later requires rebuilding the automation.

**Over-engineering first automations:** Building a 15-step Zapier workflow when a 3-step one would save 80% of the time. Start simple. Add complexity only when the simple version is stable and working.

**No monitoring:** Automations fail silently. A broken onboarding workflow that does not send the welcome email, a reporting automation that stops running -- these need monitoring that alerts a human when something is wrong.

**Replacing human judgment with automation:** Automating decisions that require context. Automations are for repeatable, rule-based work. Judgment calls, client escalations, and edge cases still require humans.

---

## Automate Done Right

O2 is working when: 20+ hours per week are provably saved through automation, measured by tracking the manual time before and after. The automation stack runs with a 95%+ success rate. Failures trigger alerts and are resolved within 24 hours. New automations are added quarterly against the priority matrix.
