#!/usr/bin/python3
# main.py

import sys
import discord
import os
from pollsort import inbetween
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
            await testChannel.send("reply to me to execute a command\n commands:\n >>version -> shows version\n >>poll -> to change title description or other values just put the value in <> and to choose which value infront of and after each > put the name of the value eg title<FOO vs BAR>title");
        
        if message.content == ">>version":
            versionEmbed = discord.Embed(title="Version", description="version is Version 1.0.0 Early Aplha", color=0x0fff0f);
            versionEmbed.add_field(name="version", value="v1.0.0", inline=False);
            versionEmbed.add_field(name="release date", value="future", inline=False);
            await testChannel.send(embed=versionEmbed);

        if ">>poll" in str(message.content):
            pollInfo = str(message.content);
            pollDict = {
                "title": inbetween(pollInfo,"title<",">title"),
                "description": inbetween(pollInfo,"description<",">description"),
                "options": inbetween(pollInfo, "options<", ">options"),
                "announce": inbetween(pollInfo, "!<",">!")
            };
            pollsEmbed = discord.Embed(title="**Poll!**", description='-'+message.author.name, color=0x55ff55);
            pollsEmbed.add_field(name="Title", value='**__'+pollDict["title"]+'__**', inline=False);
            pollsEmbed.add_field(name="Description", value=pollDict["description"]);
            pollsEmbed.add_field(name="Options", value=pollDict["options"]);
            if pollDict["announce"] == "announce" or pollDict["announce"] == "!": await testChannel.send("@everyone");
            await testChannel.send(embed=pollsEmbed);

    try:
        client.run(TOKEN);
    except:
        sys.stderr.write(f"incorrect token, {TOKEN}\n");





if __name__ == "__main__": main(sys.argv[1:], len(sys.argv[1:]));