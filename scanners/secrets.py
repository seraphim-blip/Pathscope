import re
from core.config import SECRET_PATTERNS

def scan_secrets(url, content):
    findings = []
    for pat in SECRET_PATTERNS:
        if re.search(pat, content, re.I):
            findings.append({
                "type": "secret_pattern",
                "url": url,
                "pattern": pat
            })
    return findings
