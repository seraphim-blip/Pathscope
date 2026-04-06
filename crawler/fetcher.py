import aiohttp

async def fetch(session, url):
    try:
        async with session.get(url, timeout=20) as resp:
            return await resp.text(errors="ignore")
    except Exception:
        return ""
