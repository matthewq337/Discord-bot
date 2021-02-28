from replit import db
from keep_alive import keep_alive
import discord
import os
#imports discord
from datetime import date
today = date.today()
#import the date
import discord.ext
import re
import json
import requests
from discord.ext import commands
client = discord.Client()
client = commands.Bot(command_prefix='!')
url = "https://useless-facts.sameerkumar.website/api"

response = requests.get(url)
data = response.text
parsed = json.loads(data)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("tf2"))


@client.command(pass_context=True)
async def version(ctx):
    myEmbed = discord.Embed(title="",
                            description=" ",
                            color=0x00ff00)
    myEmbed.add_field(name="Version Code", value='V1.0', inline=False)
    myEmbed.add_field(name="released", value=today, inline=False)
    myEmbed.set_author(name="made by mattq337")

    await ctx.channel.send(embed=myEmbed)


#Admin commands
@client.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


keep_alive()
client.run(os.environ["TOKEN"])

