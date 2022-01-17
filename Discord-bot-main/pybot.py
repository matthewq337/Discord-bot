import asyncio
import json
from logging import PlaceHolder
import os
import random
import aiohttp
import nextcord
import discord
import pretty_errors
from random import choice, randint
from datetime import datetime
from typing import Optional
from nextcord import Embed
from nextcord.ext.commands import BucketType
from nextcord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown)
from nextcord.ext.commands import cog
from nextcord.ext.commands.cog import Cog
from nextcord.ext.commands.errors import BadArgument
from nextcord.ext.commands import cooldown
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord.ext import commands
from nextcord.ext.commands.help import DefaultHelpCommand
from nextcord.utils import get
from nextcord import client
from dotenv import load_dotenv
from datetime import date
from nextcord.ext.commands import command, cooldown
from better_profanity import profanity
from nextcord.ext import commands
from nextcord import Forbidden
from nextcord.utils import get
today = date.today()
load_dotenv()
intents = nextcord.Intents.all()
TOKEN=""
def get_prefix(bot, message):
    return prefixes.get(str(message.guild.id), DEFAULT_PREFIX)

bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())
intents.members = True
initial_extensions =[]
    
if os.path.exists(os.getcwd() = "/config.json"):
    pass
else:
    configTemplate = {"token": "", "Prefix": "!"}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)


12

 

bot.remove_command("help")
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
    

def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []

    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")


    params = " ".join(params) 
    return f"{cmd_and_aliases} {params}"


@bot.event
async def on_ready():
        print(f"logged in as {bot.user}")
        for folder in os.listdir("modules"):
            if os.path.exists(os.path.join("modules", folder, "cog.py")):
                client.load_extension(f"modules.{folder}.cog")
        await bot.change_presence( 
            status=nextcord.Status.online, activity=nextcord.Game("tf2"))

@bot.event
async def on_message_delete(message):
    embed = nextcord.Embed(title=f"{message.author.name} has edited a message | {message.author.id}", description=f"{message.content}")
    channel  = bot.get_channel(792547157629993032)
    await channel.send(embed=embed)

@bot.event
async def on_message_edit(message_before, message_after):
    embed = nextcord.Embed(title=f"{message_before.author.name} has edited a message | {message_before.author.id}")
    embed.add_field(name="Before Message", value=f"{message_before.content}", inline=False)
    embed.add_field(name="After Message", value=f"{message_after.content}", inline=False)
    channel  = bot.get_channel(792547157629993032)
    await channel.send(embed=embed)


@bot.event
async def on_member_join(member):
    welcomeEmbed = nextcord.Embed(title = f"New member", description = f"{member.name} has joined the server", color = nextcord.Color.blue())
    await bot.get_channel(792547157629993032).send(embed = welcomeEmbed)









 


    
    
    
    
@bot.command()
async def help(ctx):
    embed = nextcord.Embed(title="help commands")
    embed.add_field(name = 'admin', value = "`ban`, `clear`, `changeprefix`, `mute`, `unmute`, `slowmode`, `kick`, `tempban`")
    embed.add_field(name = 'member', value = "`ping`, `roll`, `fact`, `version`")
    await ctx.send(embed = embed)
 
@bot.event
async def on_guild_join(guild):
    prefixes[str(guild.id)] = DEFAULT_PREFIX
    prefixes.save()
 
 
@bot.command()
@commands.cooldown(1, 60, commands.cooldowns.BucketType.user)
async def ping(ctx: commands.Context):
    """
    Returns the bots estimated latency to discord servers
    """
    await ctx.send(f"pong {round(bot.latency * 1000)}ms")


@bot.command(name = "roll")
async def roll(ctx: commands.Context):
    """
    Get a random number from 0-500
    """
    n = random.randint(0, 500)
    embed = nextcord.Embed(colour=nextcord.Colour.green())
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
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

    serverinfoEmbed = nextcord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    serverinfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}", inline =False)
    serverinfoEmbed.add_field(name='Member Count', value=f"{ctx.guild.member_count}", inline =False)
    await ctx.send(embed = serverinfoEmbed)


@bot.command(pass_context=True)
async def version(ctx):
        myEmbed = nextcord.Embed (title="current Version", description= " version 1.0 :)", color=0x00ff00)
        myEmbed.add_field( name = "Version Code", value = 'V1.0' , inline=False)
        myEmbed.add_field( name = "released", value = today , inline=False)
        myEmbed.set_author (name= "matt quintanilla")
        myEmbed.set_footer (text = ".")
        
        await ctx.channel.send(embed=myEmbed)
 



bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


bot.command()
async def unload(ctx, extension):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Invalid command used")
    
    else:
        raise error
       



class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        ammount = argument[:-1]
        unit = argument[-1]
        if ammount.isdigit() and unit in ["s," "m"]:

            return(int(ammount), unit)

        raise commands.BadArgument(message="Not a valid duration")








#Admin commands
@bot.command()
@commands.has_role('administrator')
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Looks like you don't have the permissions to do that action.")


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

@bot.command()
@commands.has_role('administrator')
async def mute(ctx, member : nextcord.Member, *, reason=None):
    guild = ctx.guild
    muteRole = nextcord.utils.get(guild.roles, name="Muted")
    
    if not muteRole:
        
        muteRole = await guild.create_role(name="Muted")
       
        for channel in guild.channels:
            await ctx.send("No mute roll has been found Creating the roll now")
            await channel.set_permissions(muteRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
           
    await member.add_roles(muteRole, reason=reason)
    await member.send(f"you have been muted from **{guild.name}** | Reason: **{reason}**")


@bot.command()
@commands.has_role('administrator')
async def unmute(ctx, member : nextcord.Member, *, reason=None):
    guild = ctx.guild
    muteRole = nextcord.utils.get(guild.roles, name="Muted")
    
    if not muteRole:
        
        muteRole = await guild.create_role(name="Muted")
       
        
           
    await member.remove_roles(muteRole, reason=reason)
    await member.send(f"you have been unmuted from **{guild.name}** | Reason: **{reason}**")


@bot.command()
async def slowmode(ctx, time:int):
    try:
        if time == 0:
            await ctx.send("Slowmode off")
            await ctx.channel.edit(slowmode_delay = 0)
        elif time > 21600:
            await ctx.send("you can not set the slowmode above 6 hours")
            return
        else:
            await ctx.channel.edit(slowmode_delay = time)
            await ctx.semd(f" slow mode set to {time} seconds")
    except Exception:
        await print("failed")


@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Looks like you don't have the permissions to do that action.")

 

@bot.command()
@commands.has_role('administrator')
async def kick(ctx, member : nextcord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
@commands.has_role('administrator')
async def ban(ctx, member : nextcord.Member, *, reason=None):
    await member.ban(reason=reason)
@ban.error
async def ban_error(ctx, error):
 if isinstance(error, commands.MissingRole):
        await ctx.send("Looks like you don't have the permissions to do that action.")

@kick.error
async def kick_error(ctx, error):
 if isinstance(error, BadArgument):
        await ctx.send("user not found.")
@ban.error
async def ban_error(ctx, error):
 if isinstance(error, BadArgument):
        await ctx.send("user not found.")

@bot.command()
async def unban(ctx, user: nextcord.User): 
    banned_users = await ctx.guild.bans()
    if user in banned_users:
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user.mention}")

@bot.command()
async def tempban(ctx, member: commands.MemberConverter, duration: DurationConverter):
    multiplier = {"s": 1, "m" : 60}

    amount, unit = duration


    await ctx.guild.ban(member)
    await ctx.send(f"{member} has been banned for {amount}{ unit}.")
    await asyncio.sleep(amount * multiplier [unit])
    await ctx.guild.unban(member)


            

@mute.error
async def mute_error(ctx, error):
 if isinstance(error, commands.MissingRole):
        await ctx.send("Looks like you don't have the permissions to do that action.")
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Looks like you don't have the permissions to do that action.")

@bot.event
async def on_message(message):
    if profanity.contains_profanity(message.content): 
        await message.delete()
        await message.author.send("""Those Words are Not Allowed To Be Used! Continued Use Of Mentioned Words Will Lead To a Punishment!""")
    else:
        await bot.process_commands(message)

@ping.error
async def error(ctx, error):
 if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("please try this command again after {:.2f}s".format(error.retry_after))

bot.run("")
