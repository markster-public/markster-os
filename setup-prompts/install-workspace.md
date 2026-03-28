# Install Markster OS Workspace

Copy and paste this into Claude Code, Codex, or Gemini CLI:

```text
Set up Markster OS for me.

Requirements:
- Install the Markster OS CLI if it is not already installed.
- Use the official installer:
  curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/master/install.sh | bash
- Create a Git-backed workspace for my company with:
  markster-os init <company-slug> --git --path ./<company-slug>-os
- Move into that workspace.
- Install Markster OS skills if useful with:
  markster-os install-skills
- If I need an extra public skill later, list and install it with:
  markster-os list-skills
  markster-os install-skills --skill <skill-name>
- Check the workspace readiness with:
  markster-os start
- Validate the workspace with:
  markster-os validate .
- Keep the local validation hooks installed so validation runs before commits and pushes, and so commit subjects follow `type(scope): summary`.

Then stop and ask me for my Git repository URL so you can attach the remote with:
- markster-os attach-remote <git-url>

If the remote is attached successfully, tell me the exact push command to run next.

Important rules:
- Treat the upstream markster-os repo as the product source, not as my company workspace.
- Treat the new workspace repo as the place where my business context will live.
- Keep raw notes in learning-loop/inbox and do not treat them as canonical.
- Use markster-os validate before saying the workspace is ready.
- Summarize what you changed in plain language at the end.
```

## Notes

- Replace `<company-slug>` with a simple lowercase slug like `acme` or `northstar`.
- If your AI tool can ask follow-up questions, let it ask for the slug and Git remote URL.
- If your AI tool supports Git operations, it can also help you commit and push after setup.
