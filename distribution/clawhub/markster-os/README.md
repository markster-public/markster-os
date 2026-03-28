# Markster OS

Markster OS is an open-source B2B growth operating system for small teams.

This ClawHub package is a thin entrypoint. It helps the agent:

- install the official `markster-os` CLI
- create a Git-backed company workspace
- check workspace readiness
- install additional public Markster OS skills when needed

This package is not the full operating system by itself.

To use the full system, install from the official repository:

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
markster-os init your-company --git --path ./your-company-os
```

Repository:

- https://github.com/markster-public/markster-os

OpenClaw guide:

- https://github.com/markster-public/markster-os/blob/master/setup-prompts/openclaw.md
