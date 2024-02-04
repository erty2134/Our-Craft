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
    TOKEN = (os.getenv("ENV_TOKEN1")+os.getenv("ENV_TOKEN2")+os.getenv("ENV_TOKEN3"));

    #intents = discord.Intents.default()
    #intents.message_content = True

    client = discord.Client(intents=discord.Intents.default());

    @client.event
    async def on_disconect():
        testChannel = client.get_channel(1203134153386885130);
        await testChannel.send("Disconected DM erty11 to get the servers running again");

    @client.event
    async def on_ready():
        testChannel = client.get_channel(1203134153386885130);
        await testChannel.send("Hello, World!");
        await testChannel.send("'>>' is my prefix >>help to see commands");
        await testChannel.send("reply to me to execute a command");

    @client.event
    async def on_message(message):
        testChannel = client.get_channel(1203134153386885130);
        #sys.stdout.write(message.author);
        if message.author == client.user:
            return;
        if message.content == ">>help":
            await testChannel.send("reply to me to execute a command\n commands:\n >>version -> shows version\n >>poll -> currently being built")
        
        if message.content == ">>version":
            await testChannel.send("Version 1.0.0 Early Aplha");

        if ">>poll" in str(message.content):
            reactions = 0;
            if "-V1" in str(message.content): reactions= 1;
            if "-V2" in str(message.conents): reactions= 2;
            if "-V3" in str(message.content): reactions= 3;
            if "-V4" in str(message.content): reactions= 4;
            if "-V5" in str(message.content): reactions= 5;

            await testChannel.send(f"Poll! reactions{reactions}");

    try:
        client.run(TOKEN);
    except:
        sys.stderr.write(f"incorrect token, {TOKEN}\n");





if __name__ == "__main__": main(sys.argv[1:], len(sys.argv[1:]));