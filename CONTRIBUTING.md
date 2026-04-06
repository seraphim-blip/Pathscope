# Contributing to Pathscope

Thank you for your interest in contributing to **Pathscope**.

This project is designed as a high-performance asynchronous web discovery framework for **authorized internal auditing**, route intelligence, and scalable security engineering workflows.

We welcome high-quality contributions that improve reliability, modularity, and maintainability.

---

## Development Principles
Please keep contributions aligned with the following goals:

- performance-first async architecture
- modular scanner design
- production-safe defaults
- clean package boundaries
- minimal dependency overhead
- readable and testable code

---

## Local Setup
Clone the repository:

```bash id="i5z3zj"
git clone https://github.com/seraphim-blip/pathscope.git
cd pathscope
````

Create virtual environment:

```bash id="0m1s4t"
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash id="2a6n1r"
pip install -r requirements.txt
```

Optional browser rendering:

```bash id="r8u0lm"
playwright install chromium
```

---

## Branching

Create a feature branch:

```bash id="3l0v8e"
git checkout -b feature/your-module-name
```

Examples:

* `feature/playwright-renderer`
* `feature/redis-queue`
* `fix/parser-normalization`

---

## Code Style

Please follow:

* Python 3.10+
* PEP8 formatting
* explicit imports
* descriptive function names
* modular responsibilities
* no dead code
* no hardcoded secrets

Recommended tooling:

```bash id="6d5x8g"
pip install ruff pytest
```

Run checks:

```bash id="m4f6n2"
python -m compileall .
ruff check .
pytest
```

---

## Pull Request Guidelines

A high-quality PR should include:

* clear problem statement
* implementation details
* expected impact
* test coverage where applicable
* documentation updates if behavior changes

Please keep pull requests focused and avoid unrelated refactors.

---

## Areas of Contribution

We especially welcome work in:

* async crawl optimization
* parser robustness
* SPA route rendering
* reporting exporters
* authentication-aware crawling
* scanner plugin interfaces
* CI improvements
* documentation quality

---

## Responsible Use

Contributions must preserve the project’s intended purpose:
**authorized internal auditing and engineering visibility only**.

Do not introduce features intended to bypass authorization, abuse access controls, or increase operational risk.

---

## Community Standards

Please be respectful, technically precise, and solution-oriented in issues and pull requests.

---

Thank you for helping improve Pathscope.
