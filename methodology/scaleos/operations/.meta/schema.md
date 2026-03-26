# Block Schema

> Every process block in the ScaleOS Operational Blueprint MUST follow this exact structure.
> The `/scaleos-block-writer` skill enforces these rules automatically.

---

## Field Definitions

| Field | Description | Validation Rule |
|-------|-------------|-----------------|
| **Trigger** | What starts this process | Must be a specific event, not vague ("when needed" = FAIL) |
| **Frequency** | How often it runs | Must use canonical term: `Daily` / `Weekly` / `Monthly` / `Per-event` / `Continuous` |
| **Input** | Data/context needed to start | Must reference specific files, systems, or upstream block IDs |
| **Owner** | Human DRI (decision maker) | Must be a named role from the dictionary |
| **Executor** | Who/what actually does the work | Must use dictionary term. Format: `[term] - fully automated` or `manual -> target: [term]` or `[term] (semi-automated)` |
| **Output** | What it produces | Must be a concrete artifact (document, record, report, published asset) |
| **Test** | How to verify it worked | Must be specific and measurable (numbers, yes/no, observable state) |
| **Systems** | Tools and services involved | Must all be dictionary terms, comma-separated |

## Section Definitions

### Required Sections

| Section | Rules |
|---------|-------|
| **Steps** | Numbered, 3-8 steps. Each step annotated with `(manual)`, `(automated)`, or `(quality gate)` |
| **Target automation** | Bullet list describing what the fully automated version looks like |
| **Blockers** | What prevents automation today. Use `None` if fully automated |

### Optional Sections

| Section | When to Include |
|---------|-----------------|
| **Key principles** | Only when strategic context is critical to understanding the process (e.g., outreach voice rules) |
| **References** | Only when linking to external design docs or plans that define implementation details |

---

## Block Template

Copy this template exactly when generating a new block:

```markdown
### [BLOCK-ID] [Block Name]

| Field | Value |
|-------|-------|
| **Trigger** | [specific event] |
| **Frequency** | [Daily / Weekly / Monthly / Per-event / Continuous] |
| **Input** | [data/context, referencing upstream blocks and specific files] |
| **Owner** | [role from dictionary] |
| **Executor** | [dictionary term - fully automated / manual -> target: dictionary term] |
| **Output** | [concrete artifact] |
| **Test** | [specific, measurable verification] |
| **Systems** | [dictionary terms, comma-separated] |

**Steps:**
1. [Step description] ([manual] / [automated] / [quality gate])
2. ...

**Target automation:**
- [What the automated version looks like]

**Blockers:** [What prevents automation, or "None"]
```

---

## Validation Rules (for /scaleos-block-writer skill)

### FAIL - Must fix before review

| Check | Catches |
|-------|---------|
| Field completeness | Any of the 8 fields empty or placeholder |
| Dictionary match | System, agent, skill, or repo name not in dictionary.md |
| Frequency format | Value not in canonical list (Daily/Weekly/Monthly/Per-event/Continuous) |

### WARN - Flagged for judgment

| Check | Catches |
|-------|---------|
| Executor format | Freeform text instead of structured `X - fully automated` or `manual -> target: X` |
| Step count | Fewer than 3 or more than 8 steps |
| Wiring check | Upstream block (from registry) not mentioned in Input or Steps |
| Cross-ref symmetry | Block A references Block B downstream, but Block B doesn't list A upstream |
