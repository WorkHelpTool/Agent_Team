import json
from pathlib import Path
from typing import Dict, List

from agents.pm_agent import PMAgent
from agents.tech_lead_agent import TechLeadAgent
from agents.dev_agent import DevAgent
from agents.qa_agent import QAAgent
from agents.ops_agent import OpsAgent
from agents.analyst_agent import AnalystAgent

AGENT_REGISTRY = {
    "pm": PMAgent,
    "tech_lead": TechLeadAgent,
    "dev": DevAgent,
    "qa": QAAgent,
    "ops": OpsAgent,
    "analyst": AnalystAgent,
}

ARTIFACT_MAP = {
    "pm": "PRD.md",
    "tech_lead": "TECH_SPEC.md",
    "dev": "TASKS.md",
    "qa": "TEST_PLAN.md",
    "ops": "DEPLOY.md",
    "analyst": "METRICS.md",
}


def _load_config(config_path: Path) -> Dict:
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    if config_path.suffix in {".json"}:
        return json.loads(config_path.read_text(encoding="utf-8"))
    if config_path.suffix in {".yml", ".yaml"}:
        try:
            import yaml  # type: ignore
        except Exception as exc:
            raise RuntimeError("PyYAML not installed. Use JSON or install pyyaml.") from exc
        return yaml.safe_load(config_path.read_text(encoding="utf-8"))
    raise ValueError("Unsupported config format. Use .json or .yaml.")


def run_flow(input_text: str, config_path: Path, artifacts_dir: Path) -> List[Path]:
    config = _load_config(config_path)
    enabled_agents = config.get("agents", [])
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    outputs: List[Path] = []
    for agent_key in enabled_agents:
        agent_cls = AGENT_REGISTRY.get(agent_key)
        if not agent_cls:
            raise ValueError(f"Unknown agent: {agent_key}")
        content = agent_cls().run(input_text)
        artifact_name = ARTIFACT_MAP.get(agent_key, f"{agent_key}.md")
        artifact_path = artifacts_dir / artifact_name
        artifact_path.write_text(content, encoding="utf-8")
        outputs.append(artifact_path)
    return outputs
