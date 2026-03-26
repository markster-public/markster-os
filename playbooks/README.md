# Playbooks

Each playbook is a deterministic sequence. It has defined inputs, a fixed set of steps, and documented outputs.

Playbooks are not general advice. They are step-by-step operating procedures. The steps reference Foundation (F1-F4) directly - which is why Foundation must be complete before most playbooks will produce useful results.

---

## How playbooks work

Every playbook follows the same pattern:

```
INPUTS
What you need before you start. If you do not have these, stop and complete them first.

STEPS
Numbered steps in sequence. Each step has a specific action, a tool or template reference, and a completion signal.

OUTPUTS
The concrete deliverables the playbook produces. You should be able to hand these to someone else.
```

The skills in this OS activate playbooks in your AI environment. When you type `/cold-email`, the skill loads the cold email playbook context and walks you through each step. You can also run playbooks manually - open the README and follow the steps.

---

## Available playbooks

| Playbook | What it produces | Requires |
|----------|-----------------|---------|
| [Cold Email](cold-email/README.md) | Verified list + sequence + send schedule | F1, F2 |
| [Events](events/README.md) | Pre/during/post system + follow-up sequence | F1 |
| [Content](content/README.md) | Theme framework + 30-day publishing calendar | F1, F3 |
| [Sales](biz-dev/sales/README.md) | Discovery framework + proposal template + close checklist | F1, F2, F3 |
| [Fundraising](biz-dev/fundraising/README.md) | Investor pipeline + outreach sequence + deck outline | F1, F2 |
| [Technical Review](technical-review/README.md) | Stack audit across 5 areas + prioritized roadmap | None |

---

## Playbook conventions

**Templates:** Each playbook has a `templates/` subdirectory with real starting-point copy. Not placeholder text - actual drafts you can edit and use.

**Skill activation:** Each playbook has a corresponding skill in `/skills/`. The skill adds context-awareness: it checks your Foundation answers, asks clarifying questions, and tailors the playbook execution to your specific ICP and offer.

**Iteration loops:** Every playbook includes an iteration section at the end. The first run generates output. Subsequent runs improve it. The iteration section tells you what to measure and what to change first.
