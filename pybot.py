from datetime import date
from dotenv import load_dotenv
import aiohttp
import time
from discord.ext import commands
import requests
import json
import random
import re
import discord.ext
import os
import discord
from aiohttp.client import request
TOKEN = ""
# keep all imports here
# keep all from here
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
url = "https://useless-facts.sameerkumar.website/api"
load_dotenv()
response = requests.get(url)
data = response.text
parsed = json.loads(data)


def get_prefix(client, message):  # first we define get_prefix
    # we open and read the prefixes.json, assuming it's in the same file
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)  # load the json as prefixes
        # recieve the prefix for the guild id given
        return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("tf2"))


@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency * 1000)}ms")

@commands.command(aliases=['roll'])
async def roll(self, ctx):
        n = random.randint(0,500)
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/762430826755260449/764946212527931392/die.png')
        embed.add_field(name='Roll', value=(f'Your random number is {n}/500.'), inline=False)

        await ctx.send(embed=embed)

@client.command()
async def fact(ctx):
    async with aiohttp.ClientSession() as session:

        # This gets the fact request
        request2 = await session.get("https://useless-facts.sameerkumar.website/api")
    factjson = await request.json()
    await ctx.send(factjson.get("data"))


@client.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_guild_join(guild):  # when the bot joins the guild
    with open('prefixes.json', 'r') as f:  # read the prefix.json file
        prefixes = json.load(f)  # load the json file

    prefixes[str(guild.id)] = '!'  # default prefix

    with open('prefixes.json', 'w') as f:  # write in the prefix.json "message.guild.id": "!"
        # the indent is to make everything look a bit neater
        json.dump(prefixes, f, indent=4)


@client.command()
# ensure that only administrators can use this command
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):  # command: !changeprefix ...
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:  # writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)


client.run(")
