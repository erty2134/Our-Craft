#!/usr/bin/python3
# main.py

import sys
import discord
import os
from dotenv import find_dotenv, load_dotenv


def main(argv:"list", argc:"int", *args:"any", **kwargs:"any") -> None:

    # load up the env
    envPath = find_dotenv();
    load_dotenv(envPath);
    TOKEN = os.getenv("ENV_TOKEN");


    client = discord.Client(intents=discord.Intents.default());

    client.run(TOKEN);


if __name__ == "__main__": main(sys.argv[1:], len(sys.argv[1:]));