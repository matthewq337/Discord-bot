import discord
#imports discord
from datetime import date
today = date.today() 
#import the date
import discord.ext
import re
from discord.ext import commands
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
        

    




#Admin commands
@client.command()
@commands.has_role('lul')
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''just be admin <:4Head:795144565744861215>''')
@client.command()
@commands.has_role('lul')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send('''just be admin <:4Head:795144565744861215>''')

@client.command()
@commands.has_role('lul')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
@ban.error
async def ban_error(ctx, error):
 if isinstance(error, commands.MissingRole):
        await ctx.send('''just be admin <:4Head:795144565744861215>''')


@client.event
async def on_message(message):
    if profanity.contains_profanity(message.content): 
        await message.delete()
        await message.author.send("""Those Words are Not Allowed To Be Used! Continued Use Of Mentioned Words Will Lead To a Punishment!""")
    else:
        await client.process_commands(message)
	

client.run('insert id here ')