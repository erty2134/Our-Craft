#!/usr/bin/python3
# main.py

import sys
import discord



def main(argv, argc, *args, **kwargs) -> None:
    client = discord.Client(intents=discord.Intents.default());

    client.run("MTIwMzEzMTQ1MjM1MTU3ODEzMw.GS8r95.WNmzTab7qBshJvVrsb5XaPKzUlVR1xDB3u1g5E");


if __name__ == "__main__": main(sys.argv[1:], len(sys.argv[1:]));