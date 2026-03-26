# Buying Signals Prompt

**Purpose:** Identify the observable signals that indicate your ICP is actively in-market for your solution. Use to prioritize who to reach out to first and what triggers to look for when building lists.

---

## Variables to fill in

- `[ICP_DESCRIPTION]` - your ICP (from F1): role, company type, typical situation
- `[SOLUTION_CATEGORY]` - what your solution helps with
- `[BUYING_TRIGGER]` - the buying trigger you identified in F1

---

## Research prompt

---

I am identifying buying signals for [ICP_DESCRIPTION] that indicate they are actively in-market for [SOLUTION_CATEGORY].

The buying trigger I have identified is: [BUYING_TRIGGER]

**1. Company-level signals**
What observable things happen at the company level that indicate they have the problem you solve and are likely thinking about addressing it? Include:
- Hiring signals (what job postings suggest they have this problem?)
- Growth signals (what milestones or growth patterns coincide with this need?)
- News signals (what press releases, announcements, or coverage signals the trigger?)
- Technology signals (what tools they are adding or replacing?)
- Funding signals (what investment events coincide with this need?)

**2. Person-level signals**
What does the individual decision-maker do publicly that signals buying intent?
- What do they post about on LinkedIn when they have this problem?
- What questions do they ask in communities or forums?
- What content do they engage with?
- What job changes signal they are building or rebuilding in this area?

**3. Timing signals**
When in the calendar year, business cycle, or company lifecycle does this problem tend to peak?
- Quarter-end behaviors?
- Post-raise behaviors?
- Post-hiring behaviors?
- Seasonal patterns in their industry?

**4. Intent data proxies**
What search behavior, content consumption, or community activity would indicate they are researching solutions in your category right now?

---

## Output format

```
BUYING SIGNALS - [DATE]

ICP: [description]
Solution: [what you offer]
Buying trigger: [trigger]

Company-level signals:
- [signal] - [where to look for it]
- [signal] - [where to look for it]
...

Person-level signals:
- [signal] - [where to see it]
- [signal] - [where to see it]
...

Timing signals:
- [when this peaks]
- [cycle patterns]

List-building filter criteria from signals:
- [filter 1]
- [filter 2]
...

Outreach priority: reach these people first: [who, based on signals]
```

Feed findings into: F1 (ICP) - situational layer. Also use to prioritize your list by signal strength.
