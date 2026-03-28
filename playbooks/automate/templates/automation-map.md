# Automation Map

What to automate, in what order, and how to verify it's working.

**Rule:** Standardize before automating. An automated broken process fails faster and at scale. Only automate processes that are documented, tested, and producing the right output manually. Reference O1 (Standardize) first.

---

## Automation Priority Framework

Three questions determine whether something should be automated:

1. **Frequency:** Does this happen more than 5 times per week?
2. **Consistency:** Does it need to happen the same way every time?
3. **Cost:** Does doing it manually take more than 30 minutes per week?

If yes to all three: automate it. If no to any: document it first.

---

## The Automation Stack (Build in This Order)

### Tier 1: Immediate ROI (Build First)

These automations each save 2-5+ hours per week. Build before anything else.

| Automation | What it does | Time saved | Tool options |
|-----------|-------------|-----------|-------------|
| Meeting confirmation sequence | Sends confirmation + reminder + prep materials automatically after booking | 1-2 hrs/week | Calendly + email automation |
| Lead follow-up sequence | Sends follow-up emails to prospects who haven't booked | 3-5 hrs/week | Instantly, Reply.io, Clay |
| Client check-in sequence | Sends weekly progress updates to active clients automatically | 2-3 hrs/week | HubSpot, ActiveCampaign |
| Invoice and payment reminders | Sends invoice + overdue reminders without manual tracking | 1-2 hrs/week | Stripe, QuickBooks, FreshBooks |
| New lead notification | Alerts the right person when a new inbound lead comes in | 30 min/week | Zapier, Make |

**Tier 1 total time saved: 7-13 hours/week**

---

### Tier 2: High Value (Build Second)

Build these once Tier 1 is stable and producing results.

| Automation | What it does | Time saved | Tool options |
|-----------|-------------|-----------|-------------|
| Lead scoring and routing | Tags and routes leads based on fit criteria automatically | 2-3 hrs/week | Apollo, HubSpot, Clay |
| Proposal generation | Generates draft proposals from discovery call notes | 2-4 hrs/week | Custom GPT, Notion AI |
| Content distribution | Publishes and schedules content across channels from one source | 2-3 hrs/week | Buffer, Zapier, Make |
| Client reporting | Pulls metrics and generates weekly report automatically | 2-4 hrs/week | Google Data Studio, Notion |
| Referral ask sequence | Triggers a referral request after client hits first milestone | 1-2 hrs/week | Email automation tool |

**Tier 2 total time saved: 9-16 additional hours/week**

---

### Tier 3: Scale (Build Third)

Build these only when Tier 1 and Tier 2 are stable. These amplify what's working.

| Automation | What it does | Time saved | Tool options |
|-----------|-------------|-----------|-------------|
| AI-assisted outreach personalization | Generates first-line hooks from ICP data at scale | Hours at scale | Clay, GPT-4, Smartlead |
| CRM auto-update | Logs email opens, replies, and meetings to CRM without manual entry | 2-3 hrs/week | HubSpot, Salesforce native |
| Churn prediction trigger | Flags clients who haven't engaged in 14+ days for proactive outreach | Variable | Custom + CRM |
| Onboarding automation | Sends onboarding sequence, intake form, and kickoff scheduling automatically | 3-5 hrs/week | HubSpot, Customer.io |
| Upsell trigger | Triggers an upsell conversation when a client hits a milestone | Variable | CRM + email automation |

---

## Automation Build Protocol

For each automation, follow this sequence:

### Step 1: Document the manual process first

Write down every step, in order, that a human does today. If you cannot write it down, you cannot automate it.

Use the SOP template: `methodology/scaleos/templates/sop-template.md`

### Step 2: Map the trigger and output

Every automation has one trigger and one output.

```
Trigger: [What event starts the automation?]
Input data: [What data does it need?]
Process: [What steps happen automatically?]
Output: [What does it produce?]
Recipient: [Who or what receives the output?]
```

Example:
```
Trigger: Prospect books a meeting via Calendly
Input data: Name, email, company, meeting time
Process: Send confirmation email -> Set reminder sequence (24hr, 1hr before) -> Log to CRM
Output: Three emails sent, CRM updated
Recipient: Prospect + CRM
```

### Step 3: Build and test on one instance

Never build and deploy to all contacts at once. Test on one real instance first.

- Trigger it manually
- Confirm every step executed correctly
- Confirm the output looks right (no broken variables, correct formatting)
- Confirm no unintended side effects

### Step 4: Deploy with monitoring

Turn it on. Set up monitoring so failures are caught before they affect clients.

**Minimum monitoring for each automation:**
- Error notifications to your email or Slack (Zapier/Make have built-in error alerts)
- Weekly check: did the automation fire the expected number of times?
- Monthly check: are the outputs still correct?

### Step 5: Document and hand off

Before this automation runs unsupervised, document it.

```
Automation name: ___
What it does: ___
Trigger: ___
Tool: ___
Last tested: ___
Owner: ___
How to pause it: ___
How to edit it: ___
What to do if it breaks: ___
```

---

## Automation Health Check (Weekly)

Add to your O3 weekly dashboard review.

- [ ] All Tier 1 automations fired as expected this week
- [ ] No error notifications received
- [ ] Check-in sequence reached all active clients
- [ ] Follow-up sequence reached all active prospects
- [ ] Any automation failures investigated and resolved

If an automation fails silently (fires but produces wrong output), it is worse than no automation. Clients miss follow-ups, leads fall through. Set error alerts before deploying.

---

## What Not to Automate

| Process | Why |
|---------|-----|
| First outreach message to singular high-value leads | Automation is detectable. High-ACV deals need human specificity. |
| Objection handling | Context-dependent. Automation produces generic responses. |
| Discovery calls | Automation cannot ask the follow-up question that surfaces the real pain. |
| Any client-facing communication during a problem | Automation at the wrong moment destroys trust. |
| Anything you cannot verify is working correctly | Silent failures at scale damage your brand. |

---

## Automation ROI Tracker

After each Tier 1 automation is built, track the actual time saved.

| Automation | Estimated hours saved/week | Actual hours saved/week | Build time (hrs) | Payback (weeks) |
|-----------|--------------------------|------------------------|-----------------|----------------|
| Meeting confirmation | | | | |
| Lead follow-up | | | | |
| Client check-in | | | | |
| Invoice reminders | | | | |
| Lead notification | | | | |

Target: each automation pays back its build time within 4 weeks.

---

## Reference

- O1 Standardize (document before automating): `playbooks/standardize/README.md`
- O3 Instrument (tracking that automations are working): `playbooks/instrument/README.md`
- Full O2 Automate playbook: `playbooks/automate/README.md`
