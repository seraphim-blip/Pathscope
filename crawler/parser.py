from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag

def normalize(url):
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

def extract_links(html, base_url, base_host):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for tag in soup.find_all(["a", "script", "link", "form"]):
        attr = "href" if tag.name in ["a", "link"] else "src"
        if tag.name == "form":
            attr = "action"

        val = tag.get(attr)
        if not val:
            continue

        full = normalize(urljoin(base_url, val))
        if urlparse(full).netloc == base_host:
            links.add(full)

    return links
