import asyncio
from os import path, mkdir


def main():
    if not path.exists("search"):
        mkdir("search")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(player.run())


main()
