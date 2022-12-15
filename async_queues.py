# async_queues.py

import argparse
import asyncio
import aiohttp

from collections import Counter
from urllib.parse import urljoin
from bs4 import BeautifulSoup

async def main(args):
    session = aiohttp.ClientSession()

    try:
        links = Counter()
        display(links)
    finally:
        await session.Close()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)

def display(links):
    for url, count in links.most_common():
        print(f"{count:3} {url}")

if __name__ == "__main__":
    asyncio.run(main(parse_args()))

async def fetch_html(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == "text/html":
            return await response.text()       