import discord
import os
import randfacts
#imports discord
from datetime import date
today = date.today() 
#import the date
import discord.ext
import re
from discord.ext import commands
from randfacts import getFact
client = discord.Client()
client = commands.Bot(command_prefix = '!')
from better_profanity import profanity
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity =discord.Game("tf2"))

@client.command(pass_context=True)
async def version(ctx):
        myEmbed = discord.Embed (title="current Version", description= " version 1.0 :)", color=0x00ff00)
        myEmbed.add_field( name = "Version Code", value = 'V1.0' , inline=False)
        myEmbed.add_field( name = "released", value = today , inline=False)
        myEmbed.set_author (name= "cinemassacres")
        myEmbed.set_footer (text = "LULW")
        
        await ctx.channel.send(embed=myEmbed)
        
@client.event
async def on_message(message):

    if message.content.find("!fact") != -1:
        await message.channel.send(getFact(False)) 



client.run(os.environ["DISCORD_TOKEN"])
