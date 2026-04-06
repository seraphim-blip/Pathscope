# Security Policy

## Supported Versions
The latest `main` branch is actively maintained.

Security fixes are prioritized for:
- current stable branch
- latest tagged release
- critical parser and scanner modules

---

## Reporting a Vulnerability
If you discover a security issue in Pathscope, please **do not open a public issue**.

Instead, report responsibly through a private channel:

- GitHub Security Advisories
- private maintainer contact
- encrypted email if available

Please include:

- affected module(s)
- reproduction steps
- impact assessment
- suggested remediation if known
- environment details

---

## Scope
Valid reports may include:

- parser crashes
- unsafe file handling
- output path traversal
- dependency risks
- concurrency deadlocks
- credential leakage in logs
- browser rendering sandbox escapes
- denial-of-service vectors

---

## Disclosure Process
After validation:

1. issue is reproduced
2. severity is assessed
3. fix branch is prepared
4. patch is tested in CI
5. coordinated disclosure is published
6. release notes are updated

---

## Secure Usage Guidance
Pathscope is intended strictly for:

- internal security engineering
- authorized route inventory
- owned application estates
- approved audit workflows

Operators should:
- use safe concurrency values
- avoid production overload
- protect findings output
- avoid committing scan artifacts
- review `.env` handling carefully

---

## Dependency Hygiene
Always keep dependencies updated:

```bash id="9s2n4d"
pip install --upgrade -r requirements.txt
````

For Playwright-enabled environments:

```bash id="5m6w1r"
playwright install --with-deps chromium
```

---

## Trademark Notice

The **Pathscope** name and branding are reserved and may not be reused without permission.
