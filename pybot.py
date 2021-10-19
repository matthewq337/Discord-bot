import json
import os
import random
 
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv
 
load_dotenv()
 
 
DEFAULT_PREFIX = "!"
 
 
class JsonDict(dict):
    def __init__(self, file_name: str):
        self.file_name = file_name
        try:
            with open(self.file_name, "r") as file:
                self.update(json.load(file))
        except FileNotFoundError:
            pass
 
    def save(self):
        with open(self.file_name, "w+") as file:
            json.dump(self, file, indent=2)
 
 
prefixes = JsonDict("prefixes.json")
 
 
def get_prefix(bot, message):
    return prefixes.get(str(message.guild.id), DEFAULT_PREFIX)
 
 
bot = commands.Bot(command_prefix=get_prefix)
 
 
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game("tf2")
    )
 
 
@bot.event
async def on_guild_join(guild):
    prefixes[str(guild.id)] = DEFAULT_PREFIX
    prefixes.save()
 
 
@bot.command()
async def ping(ctx: commands.Context):
    """
    Returns the bots estimated latency to discord servers
    """
    await ctx.send(f"pong {round(bot.latency * 1000)}ms")
 
 
@bot.command()
async def roll(ctx: commands.Context):
    """
    Get a random number from 0-500
    """
    n = random.randint(0, 500)
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/762430826755260449/764946212527931392/die.png"
    )
    embed.add_field(
        name="Roll", value=(f"Your random number is {n}/500."), inline=False
    )
    await ctx.send(embed=embed)
 
 
@bot.command()
async def fact(ctx: commands.Context):
    """
    Returns a random fact
    """
    url = "https://useless-facts.sameerkumar.website/api"
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status == 200:
            _json = await response.json()
            await ctx.send(_json.get("data"))
 
 
@bot.command()
async def clear(ctx, amount=6):
    """
    Clear messages from a channel
 
    Args:
        amount (optional): Number of messages to remove. Defaults to 6.
    """
    await ctx.channel.purge(limit=amount)
 
 
@commands.has_permissions(administrator=True)
@bot.command()
async def changeprefix(ctx, prefix):
    """
    Change the prefix for your guild
 
    Args:
        prefix: The new prefix to use
    """
    prefixes[str(ctx.guild.id)] = prefix
    prefixes.save()
    await ctx.send(f"Prefix has been changed to `{prefix}`")
 
 
bot.run(os.getenv("TOKEN"))
 
