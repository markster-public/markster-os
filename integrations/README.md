# Integrations

Integrations connect Markster OS to the tools you use to manage tasks, domains, and operations.

---

## Available integrations

| Integration | Purpose | Status |
|-------------|---------|--------|
| [ClickUp](clickup/README.md) | Task management - route pipeline actions and follow-ups to ClickUp | Available |
| Namecheap | Domain management - check and configure domains for cold email infrastructure | Via MCP |

---

## How integrations work

Each integration enables the skills and playbooks to read from and write to your existing tools.

Examples:
- The cold email playbook can create ClickUp tasks for follow-ups at each step
- The sales playbook can create pipeline deals and next-action tasks in ClickUp
- The events playbook can create post-event follow-up tasks with deadlines

Integrations are optional. All playbooks work without them. Integrations add automation and reduce manual work.

---

## Configuration

Each integration has its own README with setup instructions.

General pattern:
1. Set up the integration (API key, OAuth, or MCP configuration)
2. Confirm connection in your AI environment
3. The skill will detect the integration is available and offer to use it

---

## Coming integrations

- HubSpot CRM
- Notion workspace
- Google Workspace (calendar, docs)

To request an integration, open an issue on GitHub.
