import re

def scan_endpoints(url, content):
    findings = []
    endpoints = re.findall(r'["\'](\/[^"\']+)["\']', content)

    for ep in endpoints:
        findings.append({
            "type": "endpoint",
            "url": url,
            "endpoint": ep
        })

    return findings
