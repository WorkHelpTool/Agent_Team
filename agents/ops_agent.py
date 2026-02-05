class OpsAgent:
    name = "ops"

    def run(self, input_text: str) -> str:
        return (
            "# Deploy\n"
            "## Steps\n- Package app\n- Run in CI\n\n"
            "## Monitoring\n- Logs\n- Metrics\n"
        )
