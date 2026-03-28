# Markster OS

Markster OS is an open-source B2B growth operating system for small teams.

This ClawHub package is a thin entrypoint. It helps the agent:

- explain what Markster OS is
- ask whether the user wants to approve a full Markster OS installation
- guide the user through the official reviewable install path
- create a Git-backed company workspace
- check workspace readiness
- install additional public Markster OS skills when needed

This package is not the full operating system by itself.

To use the full system, review and run the setup from the official repository:

```bash
git clone https://github.com/markster-public/markster-os.git
cd markster-os
bash install.sh
```

Repository:

- https://github.com/markster-public/markster-os

OpenClaw guide:

- https://github.com/markster-public/markster-os/blob/master/setup-prompts/openclaw.md

Important:

- this package should ask for explicit approval before any install, remote, or push command
- this package should not use `curl | bash`
