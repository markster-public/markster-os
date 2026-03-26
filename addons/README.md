# Add-ons

Add-ons extend Markster OS with proprietary data and intelligence that is not available in the open-source layer.

---

## How the add-on model works

**Free skills** call public or open APIs, or require no API at all. All six skills in this OS are free and fully functional without any add-on key.

**Paid add-ons** extend the skills with proprietary data - verified contact lists, event attendee intelligence, AI visibility scoring. When you set the add-on API key, the skill detects it and unlocks the additional functionality.

The base workflow always works. Add-ons make specific steps faster or more powerful.

---

## Installing an add-on

All add-ons follow the same pattern:

**Step 1: Get a key**

Sign up at [markster.ai/addons](https://markster.ai/addons). Each add-on has its own page with pricing and a free tier (where available).

**Step 2: Set the environment variable**

```bash
export AOE_GRADER_KEY="your_key_here"
export EVENT_SCOUT_KEY="your_key_here"
export LEAD_PACKS_KEY="your_key_here"
```

Add to your shell profile for persistence.

**Step 3: Restart Claude / Codex / Gemini**

The skill reads the environment variable on load. Restart your AI environment after setting the key.

**Step 4: Confirm activation**

In your AI environment, type the skill command (e.g., `/cold-email`). The skill will confirm which add-ons are active.

---

## Available add-ons

| Add-on | Key | Free tier | Paid plans | Details |
|--------|-----|-----------|-----------|---------|
| AOE Grader | `AOE_GRADER_KEY` | 1 audit/month | From $49/month | [README](aoe-grader/README.md) |
| Event Scout | `EVENT_SCOUT_KEY` | 10 events/month | From $79/month | [README](event-scout/README.md) |
| Lead Packs | `LEAD_PACKS_KEY` | None | Per pack | [README](lead-packs/README.md) |

---

## Roadmap add-ons

The following add-ons are in development or planning:

- **Intent signals** - real-time buying intent data for your ICP segment
- **Podcast intelligence** - who is guesting on podcasts your ICP listens to
- **LinkedIn enrichment** - additional data fields from LinkedIn for contact enrichment

To request an add-on, contact hello@markster.ai or open a GitHub issue.

---

## Questions

Add-on support: addons@markster.ai
General questions: hello@markster.ai
