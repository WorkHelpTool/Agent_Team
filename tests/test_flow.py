from pathlib import Path

from orchestrator.flow import run_flow


def test_run_flow_generates_artifacts(tmp_path: Path) -> None:
    config = tmp_path / "pipeline.json"
    config.write_text('{"agents": ["pm", "tech_lead"]}', encoding="utf-8")

    outputs = run_flow(
        input_text="Test input",
        config_path=config,
        artifacts_dir=tmp_path / "artifacts",
    )

    assert len(outputs) == 2
    assert (tmp_path / "artifacts" / "PRD.md").exists()
    assert (tmp_path / "artifacts" / "TECH_SPEC.md").exists()
