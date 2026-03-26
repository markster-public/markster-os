---
id: scaleos-block-writer
title: ScaleOS Block Writer System Design
type: design
status: approved
owner: founder
created: 2026-02-16
updated: 2026-02-16
tags: [scaleos, operations, tooling, block-writer]
---

# ScaleOS Block Writer System Design

## Problem

Writing ~84 process blocks across 13 brick files with zero drift in terminology, format, cross-linking, and depth. One-shot writing fails because:

1. **Terminology drift** - same thing called different names across blocks
2. **Uneven depth** - some blocks get 6 detailed steps, others 3 vague ones
3. **Missing cross-references** - blocks feed into each other but neither mentions the other
4. **Context loss** - session context degrades over time, quality drops

## Solution: Reference Files + Lean Skill

Separate **data** (reference files the founder controls) from **logic** (skill that reads reference files and generates/validates blocks).

## Architecture

```
operations/
├── .meta/                          - Reference files + staging
│   ├── schema.md                   - Block template + validation rules
│   ├── dictionary.md               - Canonical terminology (systems, agents, skills, repos, roles)
│   ├── registry.md                 - Master inventory of all ~84 blocks with metadata + wiring
│   └── blocks/                     - Staging: individual approved blocks before assembly
│       ├── G1.1.md
│       ├── G1.2.md
│       └── ...
├── foundation/                     - Assembled brick files (output)
├── growth/
├── ops/
├── delivery/
├── scorecard/
└── coordination/
```

The block writer tool should live in the project workspace and be version-controlled with the methodology.

---

## Reference Files

### schema.md - Block Template

Defines the exact structure every block MUST follow.

**Required fields (table):**

| Field | Description | Validation Rule |
|-------|-------------|-----------------|
| Trigger | What starts this process | Must be specific event, not vague |
| Frequency | How often | Must use: Daily / Weekly / Monthly / Per-event / Continuous |
| Input | Data/context needed | Must reference specific files, systems, or upstream blocks |
| Owner | Human DRI | Must be a named role from dictionary |
| Executor | Who/what does it | Must use dictionary term. Format: "X - fully automated" or "manual -> target: X" |
| Output | What it produces | Must be concrete artifact |
| Test | How to verify | Must be specific and measurable |
| Systems | Tools involved | Must all be dictionary terms |

**Required sections:**
- **Steps:** Numbered, 3-8 steps. Each annotated: (manual), (automated), or (quality gate)
- **Target automation:** Bullets describing automated future state
- **Blockers:** What prevents automation. "None" if fully automated.

**Optional sections:**
- **Key principles:** Only when strategic context matters
- **References:** Only when linking to external design docs

### dictionary.md - Canonical Terminology

Every system, agent, skill, role, and repo has ONE canonical name.

**Categories:**
- Systems (prospect database, email sequencer, CRM, etc.)
- Agents (Research Squad, Pitch Strategist, Email Executor, etc.)
- Tools (content planner, content generator, prospect list builder, etc.)
- Repos (content-production, publishing engine, outreach-agent, etc.)
- Roles (Founder, CTO)
- Platforms (LinkedIn, Facebook, X, HubSpot CMS, WordPress, Medium, Substack)

Each entry: Canonical Name | Also Known As (DO NOT USE) | What It Is

### registry.md - Master Block Inventory

All ~84 blocks with metadata. Columns:

| ID | Name | Brick | Trigger | Freq | Owner | Executor | Upstream | Downstream |

**Upstream/Downstream** = the wiring diagram. Makes cross-references explicit and enforceable.

---

## Block Writer Tool Design

### Mode 1: `write <block-id>`

1. Read schema.md, dictionary.md, registry.md
2. Look up block in registry
3. Use natural language description from conversation
4. Generate block following schema
5. Validate:
   - Field completeness (all 8 fields)
   - Dictionary match (all terms canonical)
   - Wiring check (upstream/downstream referenced in content)
   - Step count (3-8)
   - Frequency format (canonical term)
   - Executor format (matches pattern)
   - Cross-ref symmetry
6. Present block + validation report
7. Approved -> saved to `.meta/blocks/<block-id>.md`

### Mode 2: `validate <brick-id>`

1. Read brick file (e.g., `growth/g2-warm.md`)
2. Parse all blocks
3. Run validation on every block
4. Report: pass/fail/warn per block

### Mode 3: `assemble <brick-id>`

1. Read all approved blocks from `.meta/blocks/<brick>.*`
2. Read registry for brick-level metadata (DRI, North Star)
3. Combine into brick file with standard header
4. Add Agent Architecture section
5. Full-file validation
6. Present for final approval

### Mode 4: `status`

Progress dashboard:
- Total blocks in registry
- Blocks with input
- Blocks written and validated
- Blocks approved
- Bricks assembled and approved
- Quality metrics (dictionary compliance, cross-ref symmetry)
- Next block to write

---

## Workflow

### Phase 0: Build the System (one-time)

1. Create reference files (schema, dictionary, registry)
2. Build the tool
3. Draft registry with all ~84 blocks
4. **Gate:** Founder approves registry

### Phase 1: Describe Blocks

- Natural language / voice-to-text / conversational
- Can describe one at a time, by brick, or stream of consciousness
- Each description tagged to block ID
- No gate - ongoing input

### Phase 2: Block Generation + QA (per block)

```
Describe -> tool generates -> tool validates -> review -> approve/revise
```

- Approved blocks saved to `.meta/blocks/`
- Session-resilient: status derivable from blocks/ directory
- **Gate:** Each block individually approved

### Phase 3: Assembly (per brick)

```
All brick blocks approved -> tool assembles -> full validation -> review -> approve
```

- **Gate:** Each assembled brick file approved

### Phase 4: Integration

1. Update README.md with accurate counts
2. Create scorecard + coordination docs
3. Commit everything
4. **Gate:** Final approval

---

## QA Layer - Three Levels

### Layer 1: Automated Validation (tool runs this)

| Check | Catches | Severity |
|-------|---------|----------|
| Field completeness | Empty/placeholder fields | FAIL |
| Dictionary match | Wrong terminology | FAIL |
| Frequency format | Non-canonical frequency | FAIL |
| Executor format | Freeform instead of structured | WARN |
| Step count | Too few (<3) or too many (>8) | WARN |
| Wiring check | Missing upstream/downstream references | WARN |
| Cross-ref symmetry | One-sided references | WARN |

FAIL = must fix. WARN = flagged for judgment.

Reviewer never sees a block that fails automated checks - it gets regenerated first.

### Layer 2: Per-Block Review (5 questions)

1. Is this actually how it works today?
2. Is anything missing?
3. Are the blockers real?
4. Is the target automation realistic for 90 days?
5. Would a new session understand this?

Actions: Approve / Revise / Reject

### Layer 3: Per-Brick Review (4 questions)

1. Does the flow make sense top to bottom?
2. Are there gaps between blocks?
3. Is the Agent Architecture section accurate?
4. Does the North Star metric still feel right?

### Error Correction

Errors always flow backward to individual blocks. Never patch assembled brick files directly - fix source block, re-validate, re-assemble.

---

## Session Resilience

| Persistent (in files) | Lost on session break |
|-----------------------|----------------------|
| Registry (all block metadata) | Nothing critical |
| Dictionary (canonical terms) | |
| Schema (template) | |
| Approved blocks (.meta/blocks/) | |
| Tool instructions | |

New session: `block-writer status` -> sees state -> picks up next block.

---

## What Gets Built

1. `operations/.meta/schema.md` - block template + validation rules
2. `operations/.meta/dictionary.md` - canonical terminology
3. `operations/.meta/registry.md` - all ~84 blocks with metadata + wiring
4. workspace block writer instructions - the tool
5. `operations/.meta/blocks/` directory - staging for approved blocks

## Dependencies

- Natural language input for each block (Phase 1)
- Existing ScaleOS handbook for methodology context
- Existing draft growth files (g1, g2, g3) as reference/validation
