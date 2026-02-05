import argparse
from pathlib import Path

from orchestrator.flow import run_flow


def main() -> None:
    parser = argparse.ArgumentParser(description="Agent Team Orchestrator")
    parser.add_argument("--input", required=True, help="Project or feature input")
    parser.add_argument(
        "--config",
        default=str(Path("configs/pipeline.json")),
        help="Path to config (.json/.yaml)",
    )
    parser.add_argument(
        "--artifacts",
        default=str(Path("artifacts")),
        help="Directory for output artifacts",
    )
    args = parser.parse_args()

    outputs = run_flow(
        input_text=args.input,
        config_path=Path(args.config),
        artifacts_dir=Path(args.artifacts),
    )

    print("Generated artifacts:")
    for path in outputs:
        print(f"- {path}")


if __name__ == "__main__":
    main()
