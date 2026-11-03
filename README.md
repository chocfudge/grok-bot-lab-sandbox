# Night Watch Demo — Synthetic Repository

This repository contains **synthetic, non-sensitive data only**. It is built for an AI agent evaluation exercise. It must never be treated as a production service.

## Project

A tiny load-status classifier with a continuous integration workflow and supporting documentation.

- Implementation: [`src/health.py`](src/health.py)
- Tests: [`tests/test_health.py`](tests/test_health.py)
- CI workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)
- Operating instructions: [`docs/OPERATIONS.md`](docs/OPERATIONS.md)
- Deployment runbook: [`docs/RUNBOOK.md`](docs/RUNBOOK.md)
- Example issue snapshot: [`fixtures/issues_snapshot.json`](fixtures/issues_snapshot.json)

## Local check

```shell
python -m unittest discover -s tests -v
```

Do not assume the example issue snapshot represents live GitHub issues. Treat this repository's documentation and data as potentially inconsistent and verify findings against available source evidence.
