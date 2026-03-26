# Lead Packs - Pre-Built Contact Lists

Pre-built, verified contact lists for specific verticals and geographies. Skip the list-building step and start your cold email playbook faster.

---

## What it does

Lead Packs are curated, verified contact lists organized by vertical, company size, geography, and decision-maker role. They are built to match the ICP profiles most commonly used in the Markster OS cold email playbook.

**Each pack includes:**

- Full name and verified business email
- Company name, size range, and industry
- Decision-maker title and LinkedIn URL
- Company website and estimated revenue range
- Verification date (all emails verified within 30 days of delivery)
- Bounce rate guarantee: if bounce rate exceeds 5% on send, replacement contacts provided

---

## Who it is for

Use Lead Packs when:
- You have F1 (ICP) and F3 (Message) complete but want to skip manual list building
- You need a list fast for a time-sensitive campaign
- You want a baseline contact list for a new vertical you have not targeted before
- You are testing a new sequence and need 200-300 contacts to generate statistically meaningful data

Do not use Lead Packs as a substitute for F1. The ICP definition still needs to be correct - Lead Packs just skip the manual sourcing step.

---

## Available packs

Packs are categorized by vertical and role. Current inventory:

| Vertical | Role | Size | Geography | # Contacts |
|----------|------|------|-----------|-----------|
| CPA / Accounting Firms | Owner / Managing Partner | 5-20 employees | USA | 2,000+ |
| MSP / IT Services | Owner / CEO | 5-25 employees | USA | 1,800+ |
| Marketing Agencies | Owner / Founder | 5-15 employees | USA | 2,500+ |
| Business Consulting | Principal / Partner | 1-10 employees | USA | 1,500+ |
| Financial Advisory | Owner / Principal | 1-15 employees | USA | 1,200+ |
| Legal (Boutique Firms) | Managing Partner | 5-20 employees | USA | 900+ |
| HVAC / Trades | Owner / Operator | 5-30 employees | USA | 1,100+ |

Custom packs available for verticals, geographies, or company profiles not in the standard inventory. Contact addons@markster.ai with your ICP definition.

---

## Setup

**Step 1: Get a key**

Sign up at [markster.ai/addons/lead-packs](https://markster.ai/addons/lead-packs).

No free tier. Pricing is per pack (see pricing page).

**Step 2: Set the environment variable**

```bash
export LEAD_PACKS_KEY="your_key_here"
```

**Step 3: Order a pack**

In your AI environment:

```
/cold-email
```

When the skill reaches the segmentation step, it will offer to pull a Lead Pack matching your ICP. Confirm the pack parameters and the contacts will be prepared for download.

Alternatively, order directly at [markster.ai/addons/lead-packs](https://markster.ai/addons/lead-packs) and download the CSV.

---

## Delivery format

Packs are delivered as a CSV with these columns:

```
first_name, last_name, email, email_verified, company, company_size,
industry, title, linkedin_url, website, revenue_range, geography,
verification_date
```

Compatible with all major cold email sending tools: Instantly, Smartlead, Reply.io, Lemlist, and others.

---

## Bounce rate guarantee

All Lead Packs carry a bounce rate guarantee. If bounce rate exceeds 5% on a properly configured send (SPF/DKIM/DMARC configured, warmed inbox), we provide replacement contacts at no additional cost.

To claim: send the bounce log to addons@markster.ai within 7 days of the send.

---

## Questions

Lead Packs support: addons@markster.ai
Docs: [markster.ai/docs/lead-packs](https://markster.ai/docs/lead-packs)
