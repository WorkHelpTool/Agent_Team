class PMAgent:
    name = "pm"

    def run(self, input_text: str) -> str:
        return (
            "# PRD\n"
            f"## Background\n{input_text}\n\n"
            "## Goals\n- Clarify user value\n- Define scope\n\n"
            "## Requirements\n- Functional: TBD\n- Non-functional: TBD\n\n"
            "## Acceptance Criteria\n- Criteria 1\n- Criteria 2\n"
        )
