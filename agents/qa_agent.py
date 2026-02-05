class QAAgent:
    name = "qa"

    def run(self, input_text: str) -> str:
        return (
            "# Test Plan\n"
            "## Functional\n- Validate artifact generation\n\n"
            "## Non-functional\n- CLI handles missing config\n"
        )
