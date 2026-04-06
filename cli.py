import asyncio
from core.banner import BANNER
from crawler.engine import Engine

async def main():
    print(BANNER)

    target = input("Target URL: ").strip()

    engine = Engine(target, depth=50)
    await engine.run()

if __name__ == "__main__":
    asyncio.run(main())
