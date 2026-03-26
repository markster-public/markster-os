---
id: scaleos-block-writer-impl
title: Block Writer System Implementation Plan
type: plan
status: complete
owner: founder
created: 2026-02-16
updated: 2026-02-17
tags: [scaleos, operations, block-writer, implementation]
---

# Block Writer System Implementation Plan

**Goal:** Build the block writer system (reference files + skill) so blocks can be described and generated.

**Architecture:** Three reference files (.meta/schema.md, dictionary.md, registry.md) provide the data. One Claude Code skill (/scaleos-block-writer) reads them and generates/validates/assembles blocks. All files live in `operations/.meta/`. Skill lives at `skills/scaleos-block-writer/SKILL.md`.

**Tech Stack:** Markdown files, Claude Code skill (markdown with instructions), git.

---

## Task 1: Create Schema File

**Files:**
- Create: `operations/.meta/schema.md`

**Step 1: Create .meta directory**

Run: `mkdir -p <repo>/operations/.meta/blocks`

**Step 2: Write schema.md**

The schema defines the exact structure every process block follows. It has three sections:

1. **Field definitions** - a table of 8 required fields with validation rules
2. **Section definitions** - Steps, Target automation, Blockers (required) + Key principles, References (optional)
3. **Block template** - the literal markdown template to copy when generating a block

The template must look exactly like this:

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

**Step 3: Verify schema.md**

Read the file back. Confirm:
- All 8 fields are defined with validation rules
- Template is present and uses correct markdown formatting
- Frequency canonical values are listed: Daily, Weekly, Monthly, Per-event, Continuous

---

## Task 2: Create Dictionary File

**Files:**
- Create: `operations/.meta/dictionary.md`

**Step 1: Gather canonical terms**

Read these files to extract every system, agent, skill, repo, role, and platform name used in the business:
- `CLAUDE.md` (system map, repo connections)
- `handbook/scaleos-v1.md` (brick definitions)
- Draft growth files: `operations/growth/g1-find.md`, `g2-warm.md`, `g3-book.md`

**Step 2: Write dictionary.md**

Organize into 6 categories. Each entry needs:
- Canonical Name (the ONLY name to use)
- Also Known As (names that MUST NOT be used)
- What It Is (one-line description)

Categories:
1. **Systems** - contact database, CRM, email sequencer, etc.
2. **Agents** - Research Squad, Pitch Strategist, Email Executor, Enrollment Worker, etc.
3. **Skills** - /content-calendar, /content, /contactdb, /campaign-launcher, etc.
4. **Repos** - content-production, autoblog, outreach-agent, etc.
5. **Roles** - Founder, CTO (with scope)
6. **Platforms** - LinkedIn, Facebook, X, HubSpot CMS, WordPress, Medium, Substack, Beehiiv

Expect 50-70 total entries across all categories.

**Step 3: Verify dictionary.md**

Read the file back. Confirm:
- Every term from the draft growth files appears in the dictionary
- No duplicates (same thing in two categories)
- "Also Known As" column populated for terms with known aliases

---

## Task 3: Create Registry File

**Files:**
- Create: `operations/.meta/registry.md`

**Step 1: Gather block definitions**

Source the full block list from:
- The ScaleOS handbook (`handbook/scaleos-v1.md`) for brick definitions
- The draft growth files (for G1, G2, G3 blocks already drafted)

**Step 2: Write registry.md**

Structure:
1. **Brick-level metadata** table - one row per brick with DRI, North Star Metric, Block Count
2. **Block inventory** table - one row per block with: ID, Name, Brick, Trigger, Freq, Owner, Executor, Upstream, Downstream

The block inventory is the critical table. Each block gets ONE row. The Upstream and Downstream columns contain comma-separated block IDs that this block connects to.

Organize blocks by pillar and brick:
- Foundation: F1.1-F1.6, F2.1-F2.5, F3.1-F3.5, F4.1-F4.5 (21 blocks)
- Growth: G1.1-G1.8, G2.1-G2.12, G3.1-G3.8 (28 blocks)
- Operations: O1.1-O1.7, O2.1-O2.6, O3.1-O3.6 (19 blocks)
- Delivery: D1.1-D1.6, D2.1-D2.5, D3.1-D3.5 (16 blocks)
- Total: ~84 blocks

**Step 3: Verify registry.md**

Read the file back. Confirm:
- Every block from the ScaleOS handbook is represented
- Upstream/Downstream columns are populated (at minimum for Growth blocks where we know the wiring)
- No orphan blocks (blocks with no upstream AND no downstream) - every block connects somewhere
- Executor column uses dictionary terms only
- Total count matches expected ~84

**GATE: Founder reviews and approves the registry before proceeding.**

---

## Task 4: Build the Skill

**Files:**
- Create: `skills/scaleos-block-writer/SKILL.md`

**Step 1: Read the skill-forge skill for standards**

Run `/skill-forge` or read the skill-forge skill to understand the current skill format standards (frontmatter, structure, sections).

**Step 2: Write the skill file**

The skill must have:

**Frontmatter:**
- name: scaleos-block-writer
- description: Generate, validate, and assemble ScaleOS process blocks from the operational blueprint registry
- Argument parsing for modes: write, validate, assemble, status

**Body - Mode: write <block-id>**
1. Read `.meta/schema.md`, `.meta/dictionary.md`, `.meta/registry.md` from `operations/`
2. Look up block-id in registry table
3. If natural language description provided in conversation, use it
4. If not, ask to describe this block
5. Generate block following schema template exactly
6. Run validation checks:
   - All 8 fields present and non-empty
   - All system/agent/skill/repo names exist in dictionary.md
   - Frequency uses canonical term
   - Executor matches pattern ("X - fully automated" or "manual -> target: X")
   - Step count between 3 and 8
   - Upstream blocks (from registry) mentioned in Input or Steps
   - Downstream blocks (from registry) mentioned in Output or Target automation
7. If validation FAIL: fix and regenerate before showing
8. If validation WARN: show warnings alongside block
9. Present block + validation report
10. On approve: save to `.meta/blocks/<block-id>.md`
11. On revise: take feedback, regenerate, re-validate

**Body - Mode: validate <brick-id>**
1. Determine brick file path from brick-id (G1 -> growth/g1-find.md, etc.)
2. Read the brick file
3. Parse individual blocks (split on `### [A-Z][0-9]`)
4. Run same validation as write mode on each block
5. Report results per block

**Body - Mode: assemble <brick-id>**
1. Map brick-id to blocks: look up registry for all blocks in that brick
2. Check `.meta/blocks/` for approved block files
3. If any blocks missing: report which are missing, abort
4. Read brick-level metadata from registry (DRI, North Star Metric)
5. Generate brick file header
6. Concatenate all blocks in ID order
7. Append Agent Architecture section (read from registry agent data)
8. Run full validation on assembled file
9. Present for final approval
10. On approve: write to correct brick file path, commit

**Body - Mode: status**
1. Read registry.md - count total blocks
2. Scan `.meta/blocks/` - count written blocks
3. Scan brick files - count assembled bricks
4. Calculate: blocks pending, blocks in progress, validated, approved
5. Show quality metrics: dictionary compliance, cross-ref symmetry
6. Show next recommended block to write (by brick priority: G2 first, then O3, then D3)
7. Display progress summary

**Step 3: Test the skill**

Run `/scaleos-block-writer status` to verify it reads the reference files and reports status correctly.

---

## Task 5: Validate System with Test Block

**Step 1: Pick a test block**

Use G2.7 (Blog Publishing) - it's fully automated and simple, making it a good validation target.

**Step 2: Describe it naturally**

Describe G2.7: "Blog publishing is when an approved blog post gets published to all platforms automatically by the blog publisher worker. It publishes to HubSpot CMS, WordPress, Medium, and Substack. The trigger is when a blog post is approved. The SEO linker runs after to check links."

**Step 3: Run the skill**

Run `/scaleos-block-writer write G2.7` and verify:
- Block generated in correct format
- All dictionary terms validated
- Upstream (G2.4, G2.5) and downstream (G2.8) referenced
- Validation report shown

**Step 4: Compare with draft**

Read the existing G2.7 block in `growth/g2-warm.md` and compare. The skill-generated version should be:
- Same factual content
- Correct terminology (dictionary-enforced)
- Proper cross-references (registry-enforced)
- Standard format (schema-enforced)

**Step 5: Approve and save**

If the test block passes review, save to `.meta/blocks/G2.7.md`.

---

## Task 6: Clean Up Draft Files

After the system is validated:

**Step 1: Add a note to draft growth files**

Add a header note to each draft file (g1-find.md, g2-warm.md, g3-book.md):
```
> **STATUS: DRAFT** - These files were written before the block writer system.
> They will be regenerated block-by-block through `/scaleos-block-writer` and replaced.
> Do not edit these directly.
```

**Step 2: Commit**

```bash
git add operations/growth/
git commit -m "docs(scaleos): mark draft growth files as pending regeneration"
```

---

## Summary

| Task | Creates | Gate |
|------|---------|------|
| 1. Schema | `.meta/schema.md` | Commit |
| 2. Dictionary | `.meta/dictionary.md` | Commit |
| 3. Registry | `.meta/registry.md` | **Founder approves** |
| 4. Skill | `skills/scaleos-block-writer/SKILL.md` | Skill runs |
| 5. Test block | `.meta/blocks/G2.7.md` | Founder reviews test output |
| 6. Clean up | Draft files marked | Push |

After these 6 tasks, the system is ready for Phase 1 (describe blocks) and Phase 2 (block generation).
