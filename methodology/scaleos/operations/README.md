---
id: scaleos-ops-readme
title: ScaleOS Operationalization Overview
type: docs
status: active
owner: founder
created: 2026-02-16
updated: 2026-02-17
tags: [scaleos, operations, block-writer]
---

# ScaleOS Operationalization - What This Is and How It Works

---

## The Non-Technical Version (For Humans)

### What Problem Are We Solving?

A business can be running - revenue coming in, agents working, content being created, outreach going out - but nobody can look at one place and see exactly how the company operates. Every process lives in someone's head, in scattered repos, or in ad-hoc workflows that change depending on who's running the session.

This is why things stall. Not because the tools don't work. Because there's no deterministic definition of how the business actually runs.

### What Are We Building?

An **Operational Blueprint** - a complete map of every repeating process in the business, organized by ScaleOS brick (Find, Warm, Book, Standardize, Automate, Instrument, Deliver, Prove, Expand).

For each process, the blueprint answers:
- What triggers it?
- What does it need to start?
- What are the exact steps?
- Who's responsible?
- What does it produce?
- How do you know it worked?
- What tools/systems are involved?
- What's preventing it from being automated?
- What the automated version looks like

About 84 processes total. When complete, any founder, co-founder, or AI session can look at one brick file and know exactly how that part of the business works.

### Why Can't We Just Write It All at Once?

Three problems show up immediately:

1. **Terminology drift** - the same tool gets called different names in different files
2. **Inconsistent quality** - some processes get detailed steps, others get vague summaries
3. **Missing connections** - Process A feeds into Process B, but neither mentions the other

Over 84 processes across 13 files, these problems compound. The result would be documentation that looks complete but misleads.

### How Are We Solving This?

A **Block Writer System** - like a factory that produces consistent process blocks, one at a time, with built-in quality checks.

**How it works:**

1. **Review the master registry** - a one-page table of all 84 processes with their basic metadata. Approve the map before anything gets expanded.

2. **Describe processes in your own words** - talk naturally, voice-to-text, whatever's comfortable. "G2.3 is when we generate social content from briefs using the content skill..."

3. **The system translates your words** - into a standardized format, using correct terminology, with cross-references to related processes.

4. **Review each block** - Is this actually how it works? Is anything missing? Are the blockers real? Approve, revise, or reject.

5. **Blocks get assembled into brick files** - review each assembled file as a final QA pass.

**What the system guarantees:**
- Every process uses the exact same terminology (enforced by a dictionary)
- Every process follows the exact same structure (enforced by a schema)
- Every connection between processes is explicit and verified (enforced by a registry)
- If a session breaks mid-work, the next session picks up exactly where we left off

**Your role:** Architect and final quality gate. You define what's true. The system ensures it's consistent.

---

## The Technical Version (For Sessions)

### Architecture

```
operations/
├── .meta/                                 - Block writer reference files
│   ├── schema.md                          - Block template + validation rules
│   ├── dictionary.md                      - Canonical terminology
│   ├── registry.md                        - Master inventory of all blocks + wiring
│   └── blocks/                            - Staging: individual approved blocks
│
├── README.md                              - You are here
├── foundation/                            - F1-F4 brick files (assembled)
├── growth/                                - G1-G3 brick files (assembled)
├── ops/                                   - O1-O3 brick files (assembled)
├── delivery/                              - D1-D3 brick files (assembled)
├── scorecard/                             - Weekly verification (separate layer)
└── coordination/                          - Multi-session protocol
```

### The Tool: Block Writer

A workspace tool with 4 modes:

| Mode | Command | What It Does |
|------|---------|-------------|
| write | `block-writer write G2.3` | Generate one block from description, validate, present |
| validate | `block-writer validate G2` | Check all blocks in a brick file |
| assemble | `block-writer assemble G1` | Combine approved blocks into a brick file |
| status | `block-writer status` | Progress dashboard |

### Reference Files

**schema.md** - 8 required fields (Trigger, Frequency, Input, Owner, Executor, Output, Test, Systems). 3 required sections (Steps, Target automation, Blockers). Validation rules per field.

**dictionary.md** - Canonical name for every system, agent, skill, repo, role, platform. If not in dictionary, it cannot appear in a block.

**registry.md** - All blocks listed: ID, Name, Brick, Trigger, Freq, Owner, Executor, Upstream, Downstream. The wiring diagram that makes cross-references enforceable.

### Workflow Phases

| Phase | What Happens | Gate |
|-------|-------------|------|
| 0: Build | Create schema, dictionary, registry, skill | Founder approves registry |
| 1: Describe | Natural language input per block | None (ongoing) |
| 2: Generate | Skill generates + validates, founder reviews | Each block approved |
| 3: Assemble | Combine blocks into brick files | Each brick approved |
| 4: Integrate | Update README, scorecard | Final approval |

### QA Layers

1. **Automated** - Skill validates before founder sees it (field completeness, dictionary, wiring, format)
2. **Per-block** - Is this real? Anything missing? Blockers accurate? Automation realistic?
3. **Per-brick** - Flow correct? Gaps? Agent Architecture right? North Star right?

### Session Resilience

All state in files. New session runs `block-writer status` to see progress and continue.

### Current Status

**Phase 0 (Build) is COMPLETE.** The system is ready to describe blocks.

- Design: Approved
- Reference files: All created
  - `schema.md` - 8 fields, block template, FAIL/WARN validation rules
  - `dictionary.md` - canonical entries across 6 categories (Systems, Agents, Skills, Repos, Roles, Platforms)
  - `registry.md` - 84 blocks mapped across 13 bricks with upstream/downstream wiring, 0 orphans
- Tool: block writer - designed with 4 modes (write, validate, assemble, status)
- Test block: G2.7 (Blog Publishing) - generated, validated, approved
- Blocks approved: 1 of 84
- Bricks assembled: 0 of 13

**Next:** Describe blocks starting with G2 (current constraint). Run `block-writer write G2.1` to begin.

---

## Foundation Health

| Component | Score | Status |
|-----------|-------|--------|
| F1: Positioning & Differentiation | assess | - |
| F2: Business Model Design | assess | - |
| F3: Organizational Structure | assess | - |
| F4: Financial Architecture | assess | - |

Run `assessments/foundation-scorecard.md` to score each component.

---

## GOD Engine Status

| Brick | Owner | Processes |
|-------|-------|-----------|
| G1: Find | Founder | 8 |
| G2: Warm | Founder | 12 |
| G3: Book | Founder | 8 |
| O1: Standardize | CTO | 7 |
| O2: Automate | CTO | 6 |
| O3: Instrument | Founder | 6 |
| D1: Deliver | Founder | 6 |
| D2: Prove | Founder | 5 |
| D3: Expand | Founder | 5 |
| **TOTAL** | | **63** |

---

## 90-Day Targets

Constraint-ordered - fix the bottleneck first:

| Priority | Brick | Key Action |
|----------|-------|------------|
| 1 | G2: Warm | Content production - systematic cadence |
| 2 | O3: Instrument | Unified dashboard, weekly scorecard |
| 3 | D3: Expand | Client health scoring, referral system |
| 4 | F4: Financial | Weekly cash forecast, break-even calc |

---

## File Map

```
operations/
├── README.md                     - You are here
├── .meta/                        - Block writer system (reference files + staging)
│   ├── schema.md                 - Block template + 8 fields + FAIL/WARN validation rules
│   ├── dictionary.md             - Canonical terms (systems, agents, skills, repos, roles, platforms)
│   ├── registry.md               - All 84 blocks with metadata + upstream/downstream wiring
│   └── blocks/                   - Staging: individual approved blocks before assembly
│       └── G2.7.md               - First approved block (Blog Publishing)
├── foundation/
│   ├── f1-positioning.md         - 6 processes (review cadence) - not yet created
│   ├── f2-business-model.md      - 5 processes (review cadence) - not yet created
│   ├── f3-org-structure.md       - 5 processes (review cadence) - not yet created
│   └── f4-financial.md           - 5 processes (weekly cadence) - not yet created
├── growth/
│   ├── g1-find.md                - 8 processes (prospecting pipeline) - DRAFT, pending regeneration
│   ├── g2-warm.md                - 12 processes (CONSTRAINT - content pipeline) - DRAFT, pending regeneration
│   └── g3-book.md                - 8 processes (outreach pipeline) - DRAFT, pending regeneration
├── ops/
│   ├── o1-standardize.md         - 7 processes (documentation discipline) - not yet created
│   ├── o2-automate.md            - 6 processes (agent development) - not yet created
│   └── o3-instrument.md          - 6 processes (measurement) - not yet created
├── delivery/
│   ├── d1-deliver.md             - 6 processes (client execution) - not yet created
│   ├── d2-prove.md               - 5 processes (proof collection) - not yet created
│   └── d3-expand.md              - 5 processes (account growth) - not yet created
├── scorecard/
│   └── weekly-scorecard.md       - Monday verification template - not yet created
└── coordination/
    └── multi-session-protocol.md - How founders + sessions coordinate - not yet created
```

### Block Writer Workflow

All brick files will be regenerated through the block writer system:
1. Describe a block -> `block-writer write G2.1`
2. System generates + validates -> review -> approve/revise/reject
3. Approved blocks saved to `.meta/blocks/`
4. When all blocks in a brick are approved -> `block-writer assemble G2`
5. Assembled brick file replaces draft file

---

## Connection to Existing Docs

| Existing Doc | Relationship |
|-------------|-------------|
| `handbook/scaleos-v1.md` | The methodology (WHAT each brick should do). Blueprint = HOW we actually do it. |
| `handbook/ai-native-upgrade.md` | The vision (agents per brick). Blueprint = current vs target state per process. |
| `assessments/` | Brick-level questions. Blueprint = process-level answers. |
