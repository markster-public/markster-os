from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


def load_cli_module():
    module_path = Path(__file__).resolve().parent.parent / "tools" / "markster_os_cli.py"
    spec = importlib.util.spec_from_file_location("markster_os_cli", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


cli = load_cli_module()


class PaperclipHelpersTest(unittest.TestCase):
    def test_normalize_api_base_adds_api_suffix(self) -> None:
        self.assertEqual(cli.normalize_paperclip_api_base("http://localhost:3100"), "http://localhost:3100/api")
        self.assertEqual(cli.normalize_paperclip_api_base("http://localhost:3100/"), "http://localhost:3100/api")
        self.assertEqual(cli.normalize_paperclip_api_base("http://localhost:3100/api"), "http://localhost:3100/api")

    def test_build_codex_adapter_config_uses_workspace_and_model(self) -> None:
        workspace = Path("/tmp/workspace").resolve()
        config = cli.build_paperclip_adapter_config("codex", workspace, model="gpt-5.4")
        self.assertEqual(config["cwd"], str(workspace))
        self.assertEqual(config["model"], "gpt-5.4")
        self.assertEqual(config["timeoutSec"], 0)
        self.assertEqual(config["graceSec"], 15)

    def test_build_openclaw_adapter_requires_url(self) -> None:
        with self.assertRaises(ValueError):
            cli.build_paperclip_adapter_config("openclaw", Path("/tmp/workspace"))

        config = cli.build_paperclip_adapter_config(
            "openclaw",
            Path("/tmp/workspace"),
            openclaw_url="http://127.0.0.1:18789",
        )
        self.assertEqual(config["url"], "http://127.0.0.1:18789")
        self.assertEqual(config["sessionKeyStrategy"], "issue")
        self.assertEqual(config["role"], "operator")
        self.assertEqual(config["scopes"], ["operator.admin"])

    def test_plan_bootstrap_creates_and_updates_agents_in_reporting_order(self) -> None:
        desired = cli.build_paperclip_agent_blueprints("codex", Path("/tmp/workspace"))
        existing = [{"id": "agent-ceo", "name": "Markster CEO"}]
        operations = cli.plan_paperclip_bootstrap(existing, desired)

        self.assertEqual(operations[0]["action"], "update")
        self.assertEqual(operations[0]["agent_id"], "agent-ceo")
        self.assertEqual(operations[1]["action"], "create")
        self.assertEqual(operations[1]["payload"]["reportsTo"], "agent-ceo")

        names = [op["payload"]["name"] for op in operations]
        self.assertEqual(
            names,
            [
                "Markster CEO",
                "Markster GTM Lead",
                "Markster SDR",
                "Markster Content Lead",
                "Markster Researcher",
            ],
        )


if __name__ == "__main__":
    unittest.main()
