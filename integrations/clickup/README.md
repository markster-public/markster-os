# ClickUp Integration

Connect Markster OS to ClickUp to automatically route pipeline actions, follow-up tasks, and deal tracking to your workspace.

---

## What this integration enables

| Skill | ClickUp actions |
|-------|----------------|
| Cold Email | Creates follow-up tasks for reply conversations. Logs campaign milestones. |
| Events | Creates post-event follow-up tasks with 48-hour deadlines. |
| Sales | Creates deal cards in your pipeline list. Sets next-action tasks per deal. |
| Fundraising | Creates investor pipeline cards. Sets follow-up tasks per investor relationship. |

---

## Setup

### Step 1: Get your ClickUp API key

1. Log into ClickUp
2. Go to Settings -> Apps
3. Generate a personal API token
4. Copy the token

### Step 2: Configure your AI environment

Add your API key to your environment:

```bash
export CLICKUP_API_KEY="your_key_here"
```

For persistent configuration, add this to your shell profile (`~/.zshrc`, `~/.bash_profile`, or equivalent).

### Step 3: Set your workspace IDs

The integration needs to know which ClickUp list to write tasks to.

Find your list IDs:
- Open ClickUp in the browser
- Navigate to the list you want to use
- The URL contains the list ID: `app.clickup.com/[team_id]/[space_id]/list/[list_id]`

Set the IDs:

```bash
export CLICKUP_PIPELINE_LIST="list_id_for_deals"
export CLICKUP_TASK_LIST="list_id_for_follow_up_tasks"
```

### Step 4: Verify

In your AI environment, ask it to check the ClickUp connection:

```
Check if my ClickUp integration is configured. List the first 3 tasks in my pipeline list.
```

---

## Using the integration with skills

Once configured, skills will offer ClickUp actions automatically.

Example (cold email skill):
"A prospect replied to your cold email. Would you like me to create a ClickUp follow-up task for tomorrow at 9am?"

Example (sales skill):
"Discovery call notes captured. Should I create a deal card in your ClickUp pipeline with these details and set a task to send the proposal by Thursday?"

---

## Task naming convention

Tasks created by Markster OS skills follow this format:

```
[SKILL] [ACTION] - [COMPANY/CONTACT NAME]
```

Examples:
- `[CE] Follow up - Acme Corp (replied positive)`
- `[SALES] Send proposal - John Smith, ABC Advisory`
- `[EVENTS] Post-event follow-up - Jane Doe, met at SF FinTech Summit`

---

## Troubleshooting

**Tasks not being created:** Verify your API key is set and has write access to the target list.

**Wrong list:** Double-check your list IDs. The list ID in the URL is the number at the end after `/list/`.

**Permissions error:** Ensure your API token has permission to create tasks in the target workspace.
