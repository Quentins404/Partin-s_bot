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
from blockedWords import BlockedWords
from token_1 import TOKEN
from dotenv import load_dotenv
import re
import pyrandmeme
from pyrandmeme import *
import requests


#Load .env file
load_dotenv()
# Load .env variables
discord_token = os.getenv(TOKEN)
discord_channel = os.getenv('CHANNEL')

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Events
@client.event
async def on_message(message):
    print(f"{str(message.author)} in {message.guild.name}: {message.content}")

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
    channel = client.get_channel(discord_channel)
    embed=discord.Embed(title="Welcome!",description=f"{member.mention}just arrived!" , color=discord.Colour.green())
    await channel.send(embed=embed)

# Commands 
@client.tree.command(name="connect")
async def connect(interaction: discord.Interaction):
    embed=discord.Embed(title="**To connect on the server you need to**",description="Start Minecraft \n \n Click on ```Multiplayer```  \n Then on ```Add server``` \n Then paste ```YOUR_SERVER_IP``` \n  in ""server adress"" \n \n  then , click on done \n \n Finally double-click on the server to join it" ,color=discord.Colour.blue())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="help" , description="Gives ypou all the commands")
async def help(interaction: discord.Interaction):
    embed=discord.Embed(title="**Commands list**",description="/status \n \n /help \n \n /commands \n \n /version \n \n /ping \n \n /random \n \n /express_rage \n \n /meme  " , color=discord.Colour.yellow())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="ping" , description="Replies with a Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms")


@client.tree.command(name="version" , description="Gives you the version of the bot")
async def version(interaction: discord.Interaction):
    embed=discord.Embed(title="Version of the bot" , description="Bot version: V.1.10 \n Python version: 3.11.4 " , color=discord.Colour.dark_purple())
    embed.set_image(url="https://i.ibb.co/T2KvY7w/t-l-chargement.png")
    await interaction.response.send_message(embed=embed)





@client.tree.command(name="test" , description="DO NOT USE OR YOU WILL GET BANNED")
async def test(interaction: discord.Interaction):
   await interaction.response.send_message("https://tenor.com/view/python-powered-logo-programming-language-gif-16957606")


@client.tree.command(name="commands")
async def commands(interaction: discord.Interaction):
    embed=discord.Embed(title="IG-Commands", description="/sethome homename (sets an home) \n \n /home homename (teleports you to your home) \n \n /hub (teleports you to the hub)")
    await interaction.response.defer()
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="status", description="gives you the status of the server")
async def status(interaction: discord.Interaction):
        embed=discord.Embed(title="**I'm checking the status...**",description="The server is ON :green_square: \n \n To connect , just go on the #How-to-connect channel." , color=discord.Colour.green())
        await interaction.response.send_message(embed=embed)
        await defer(ephemeral=False, thinking=False)




@client.tree.command(name="mute", description="add role 'mute' to someone")
async def mute(ctx, member: discord.Member):
        # Rôle "Muted"
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            # Apply Restriction
            permissions = discord.Permissions(send_messages=False, speak=False)
            await muted_role.edit(permissions=permissions)
        # Add "Muted" to member
        await member.add_roles(muted_role)
        print((f"{member.mention} Has been Muted."))


# TODO Find a way to make the bot send a message when the command is send.

@client.tree.command(name="unmute", description="Unmute someone")
async def unmute(ctx, member: discord.Member):
        # Rôle "Muted" check
        unmuted_role = discord.utils.get(ctx.guild.roles, name="Muted")
            # Apply Restriction    
        permissions = discord.Permissions(send_messages=True, speak=True)    
        await unmuted_role.edit(permissions=permissions)
        # Remove "Muted" to member
        await member.remove_roles(unmuted_role)
        print((f"{member.mention} Has been Unmuted."))


@client.event
async def on_message(ctx):
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    if any(x in ctx.content for x in BlockedWords):
        await ctx.delete()


#Makes the bot respond to a message where he is mentioned.

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    pattern = re.compile(f"<@!?{client.user.id}>") # The exclamation mark is optional

    if pattern.match(message.content.lower()) is not None: # Checking whether the message matches our pattern
        await message.channel.send(f"**I am going to implode.** {message.author.mention}" , reference=message) 

        

@client.tree.command(name="random" , description="Gives you a random number beetween 1 and 1000000")
async def random(interaction: discord.Interaction):
    import random
    await interaction.response.send_message(random.randint(0, 1000000))

@client.tree.command(name="express_rage" , description="EXPRESS YOUR RAGE")
async def express_rage(interaction: discord.Interaction):
    await interaction.response.send_message("**I am going to implode.**")


@client.tree.command(name="meme" , description="Send a random meme")
async def meme(interaction:discord.Interaction):
    await interaction.response.send_message(embed=await pyrandmeme())




client.run(TOKEN)
