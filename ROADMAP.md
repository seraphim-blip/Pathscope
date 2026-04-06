# Pathscope Roadmap

This roadmap outlines the planned evolution of **Pathscope** as a scalable asynchronous web discovery and route intelligence framework.

---

## Near-Term
### Crawl Engine
- improved queue scheduling
- crawl session resume support
- deduplicated crawl graph model
- redirect chain visibility
- adaptive concurrency tuning

### Parsing
- JavaScript endpoint extraction
- SPA route inference
- robots.txt ingestion
- sitemap.xml parsing
- framework-aware frontend route detection

### Output
- CSV exporter
- HTML reporting
- normalized JSON schema v2
- stream-safe large result export
- deduplicated endpoint models

---

## Mid-Term
### Distributed Crawling
- Redis-backed crawl queue
- distributed worker model
- shard-aware route scheduling
- resumable crawl checkpoints

### Authenticated Discovery
- cookie session injection
- bearer token support
- SSO-aware crawl workflows
- authenticated route inventory

### Scanner Plugins
- plugin registration system
- scanner lifecycle hooks
- custom output serializers
- organization-specific rulesets

---

## Long-Term
### Platform Expansion
- web dashboard
- historical crawl diffing
- asset ownership mapping
- route drift detection
- multi-tenant reporting
- CI pipeline integrations
- SARIF security workflow export

---

## Future Milestones
### Crawl Intelligence
- JavaScript route discovery
- SPA rendering support
- authenticated crawl sessions
- adaptive concurrency

### Reporting
- CSV exporter
- HTML reports
- SARIF support
- output schema versioning

### Scale & Platform
- distributed crawl workers
- Redis queue backend
- historical route diffing
- dashboard interface
- plugin ecosystem
