import asyncio
import json
from urllib.parse import urlparse
import aiohttp

from crawler.fetcher import fetch
from crawler.parser import extract_links, normalize
from scanners.secrets import scan_secrets
from scanners.endpoints import scan_endpoints

class Engine:
    def __init__(self, start_url, depth=20):
        self.start_url = start_url
        self.base_host = urlparse(start_url).netloc
        self.max_depth = depth
        self.visited = set()
        self.findings = []

    async def crawl(self, session, url, depth):
        url = normalize(url)

        if url in self.visited or depth > self.max_depth:
            return

        self.visited.add(url)
        print(f"[{depth}] {url}")

        html = await fetch(session, url)
        if not html:
            return

        self.findings.extend(scan_secrets(url, html))
        self.findings.extend(scan_endpoints(url, html))

        links = extract_links(html, url, self.base_host)

        tasks = [self.crawl(session, link, depth + 1) for link in links]
        await asyncio.gather(*tasks)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            await self.crawl(session, self.start_url, 0)

        with open("output/findings.json", "w") as f:
            json.dump(self.findings, f, indent=2)
