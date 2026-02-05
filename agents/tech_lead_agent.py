class TechLeadAgent:
    name = "tech_lead"

    def run(self, input_text: str) -> str:
        return (
            "# Tech Spec\n"
            "## Architecture\n- Modules: agents, orchestrator, artifacts\n\n"
            "## Decisions\n- Language: Python\n- Config: JSON/YAML\n\n"
            "## Risks\n- Dependency for YAML parsing\n"
        )
