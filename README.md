# Agent Team (MVP)

## Run

python main.py --input "Build an agent team system"

## Config

Edit configs/pipeline.json to enable/disable agents.

## GitHub Workflow

CI runs on push/PR and executes main.py with a sample input.

## Quality

ruff check .

black --check .

pytest -q

## Release

Push a tag like v0.1.0 to trigger the release workflow.
