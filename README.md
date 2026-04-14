## Overview
Pathscope is a **high-performance asynchronous web discovery framework** built for **authorized internal security auditing**, **route intelligence**, and **surface mapping**.

Designed with a modular architecture, Pathscope combines:
- deep recursive crawling
- endpoint discovery
- secret pattern scanning
- SPA-aware extensibility
- structured JSON output

It is optimized for modern engineering and security teams working with complex internal web estates.

---

## Architecture
```mermaid
flowchart TD
    A[CLI Entry] --> B[Crawl Engine]
    B --> C[Async Fetcher]
    B --> D[HTML Parser]
    D --> E[Link Extractor]
    B --> F[Scanner Modules]
    F --> G[Endpoint Scanner]
    F --> H[Secret Scanner]
    F --> I[Future Plugins]
    B --> J[JSON Output]
````

---

## Core Capabilities

*  High-concurrency asynchronous crawling
*  Deep recursive internal route traversal
*  Endpoint extraction from HTML and JavaScript
*  Secret pattern discovery
*  Modular scanner architecture
*  Structured JSON findings
*  SPA-ready rendering extension path
*  Clean package structure for scaling teams

---

## Terminal Preview

```bash id="83x5dm"
$ python3 cli.py https://example.com --depth 100 --concurrency 80

███████╗███████╗██████╗  █████╗ ██████╗ ██╗  ██╗██╗███╗   ███╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║  ██║██║████╗ ████║
███████╗█████╗  ██████╔╝███████║██████╔╝███████║██║██╔████╔██║
╚════██║██╔══╝  ██╔══██╗██╔══██║██╔═══╝ ██╔══██║██║██║╚██╔╝██║
███████║███████╗██║  ██║██║  ██║██║     ██║  ██║██║██║ ╚═╝ ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝

[0] https://example.com
[1] https://example.com/search
[1] https://example.com/about
[2] https://example.com/preferences
```

---

## Installation

Clone repository:

```bash id="0z9wzj"
git clone https://github.com/seraphim-blip/pathscope.git
cd pathscope
```

Create virtual environment:

```bash id="zt4u0e"
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash id="o8e5j1"
pip install -r requirements.txt
```

Optional Playwright support:

```bash id="nztc95"
playwright install chromium
```

---

## Quick Start

### Interactive

```bash id="uz4w5e"
python3 cli.py
```

### CLI mode

```bash id="d9u3v0"
python3 cli.py https://example.com --depth 100 --concurrency 80
```

---

## Output

Findings are exported to:

```text id="ywus6g"
output/findings.json
```

Example:

```json id="x07m2m"
[
  {
    "type": "endpoint",
    "url": "https://example.com/app.js",
    "endpoint": "/api/v1/users"
  },
  {
    "type": "secret_pattern",
    "url": "https://example.com/config.js",
    "pattern": "token"
  }
]
```

---

## Project Structure

```text
pathscope/
├── cli.py
├── requirements.txt
├── output/
├── core/
├── crawler/
└── scanners/
```

---

## CI / Quality

Recommended GitHub Actions workflow:

```text id="rq9tv5"
.github/workflows/python.yml
```

Checks:

* import validation
* syntax test
* package integrity
* future pytest integration

---

## Security & Responsible Use

Pathscope must only be used for:

* systems you own
* internal engineering audits
* explicitly authorized environments
* approved security assessments

Always maintain:

* safe concurrency
* documented authorization
* operational awareness
* production-safe rate controls

---

## Roadmap

*  Playwright SPA renderer
*  Redis distributed queue
*  HTML reporting
*  CSV / SARIF exporters
*  authenticated crawling
*  sitemap ingestion
*  plugin scanner API

---

## License

Licensed under **GNU Affero General Public License v3.0 (AGPLv3)**.

---

## Trademark Notice

The **Pathscope** name, logo, and branding assets are reserved.

---

## Author

Built by **Seraphim**.
