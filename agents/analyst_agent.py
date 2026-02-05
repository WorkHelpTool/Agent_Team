class AnalystAgent:
    name = "analyst"

    def run(self, input_text: str) -> str:
        return (
            "# Metrics\n"
            "## KPIs\n- Cycle time\n- Defect rate\n\n"
            "## Data Sources\n- CI logs\n- Issue tracker\n"
        )
