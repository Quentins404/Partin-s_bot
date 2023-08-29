import random
import colorsys
import discord
import defer
from discord import app_commands
from discord import embeds
from discord import colour
from discord.ext import commands
from discord import *
from discord.ext import commands, tasks
import os
from token_1 import TOKEN
from blockedWords import BlockedWords




intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())




@client.event
async def on_message(message):
    print("{} in {}: {}".format(str(message.author), message.guild.name, message.content))



@client.event
async def on_ready():
    # this runs when the account is logged into
    print("We have logged in as {0.user}".format(client))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(YOUR_CHANNEL_ID)
    embed=discord.Embed(title="Welcome!",description=f"{member.mention}just arrived!" , color=discord.Colour.green())
    await channel.send(embed=embed)

@client.tree.command(name="connect")
async def connect(interaction: discord.Interaction):
        embed=discord.Embed(title="**To connect on the server you need to**",description="Start Minecraft \n \n Click on ```Multiplayer```  \n Then on ```Add server``` \n Then paste ```YOUR_SERVER_IP``` \n  in ""server adress"" \n \n  then , click on done \n \n Finally double-click on the server to join it" ,color=discord.Colour.blue())
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="help" , description="Gives ypou all the commands")
async def help(interaction: discord.Interaction):
     embed=discord.Embed(title="**Commands list**",description="/status \n \n /help \n \n /commands \n \n /version \n \n /ping " , color=discord.Colour.yellow())
     await interaction.response.send_message(embed=embed)

@client.tree.command(name="ping" , description="Replies with a Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms")

@client.tree.command(name="version" , description="Gives you the version of the bot")
async def version(interaction: discord.Interaction):
     embed=discord.Embed(title="Version of the bot" , description="Bot version: V.1.10 \n Python version: 3.11.4" , color=discord.Colour.dark_purple())
     await interaction.response.send_message(embed=embed)
     await defer(ephemeral=False , thinking=False)


@client.tree.command(name="youtube" , description="gives you the link")
async def status(interaction: discord.Interaction):
     embed=discord.Embed(title="Owners Channels links",description="**Quentin's:** https://www.youtube.com/channel/UClKOEpqCOlIFmK6rzht9uKg \n \n **Par:** https://www.youtube.com/channel/UChZss9UUr9webpB2hcrs4gg" , color=discord.Colour.red())
     await interaction.response.send_message(embed=embed)





@client.tree.command(name="commands")
async def commands(interaction: discord.Interaction):
     embed=discord.Embed(title="IG-Commands", description="/sethome homename (sets an home) \n \n /home homename (teleports you to your home) \n \n /hub (teleports you to the hub)")
     await interaction.response.send_message(embed=embed)

@client.tree.command(name="status", description="gives you the status of the server")
async def status(interaction: discord.Interaction):
        embed=discord.Embed(title="**I'm checking the status...**",description="The server is ON :green_square: \n \n To connect , just go on the #How-to-connect channel." , color=discord.Colour.green())
        await interaction.response.send_message(embed=embed)
        await defer(ephemeral=False, thinking=False)



@client.event
async def on_message(ctx):
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    if any(x in ctx.content for x in BlockedWords):
        await ctx.delete()


client.run(TOKEN)


