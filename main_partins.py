#imports
import random
import colorsys
import discord
import defer
from discord import app_commands
from discord import embeds
from discord import colour
from discord import *
from discord.ext import *
from discord.ext import commands, tasks
from discord import Client, Intents
from blockedWords import blockedWords
import os
import time
from token_1 import TOKEN
import pyrandmeme
from pyrandmeme import *
import requests
import re




#Bot Setup
intents = discord.Intents.all()
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@client.listen('on_message')
async def f4(message):
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


#join message
@client.listen('on_member_join')
async def f3(member):
    channel = client.get_channel(1139570392973975553)
    embed=discord.Embed(title="Welcome!",description=f"{member.mention}just arrived!" , color=discord.Colour.green())
    await channel.send(embed=embed)

# Commands 
@client.tree.command(name="connect")
async def connect(interaction: discord.Interaction):
    embed=discord.Embed(title="**To connect on the server you need to**",description="Start Minecraft \n \n Click on ```Multiplayer```  \n Then on ```Add server``` \n Then paste ``` 172.99.189.127:35600``` \n  in ""server adress"" \n \n  then , click on done \n \n Finally double-click on the server to join it" ,color=discord.Colour.blue())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="help" , description="Gives ypou all the commands")
async def help(interaction: discord.Interaction):
    embed=discord.Embed(title="**Commands list**",description="/status \n \n /help \n \n /commands \n \n /version \n \n /ping \n \n /random \n \n /express_rage \n \n /meme  " , color=discord.Colour.yellow())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="ping" , description="Replies with a Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(view=MyView2())


@client.tree.command(name="version" , description="Gives you the version of the bot")
async def version(interaction: discord.Interaction):
    embed=discord.Embed(title="Version of the bot" , description="Bot version: V.1.10 \n Python version: 3.11.4 " , color=discord.Colour.dark_purple())
    embed.set_image(url="https://i.ibb.co/T2KvY7w/t-l-chargement.png")
    await interaction.response.send_message(embed=embed)



@client.tree.command(name="commands")
async def commands(interaction: discord.Interaction):
    embed=discord.Embed(title="IG-Commands", description="/sethome homename (sets an home) \n \n /home homename (teleports you to your home) \n \n /homes (List all of your homes) \n \n /spawn (teleports you to the hub)" , color=discord.Colour.dark_orange())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="status", description="gives you the status of the server")
async def status(interaction: discord.Interaction):
        embed=discord.Embed(title="**I'm checking the status...**",description="The server is ON :green_square: \n \n To connect , just go on the #How-to-connect channel." , color=discord.Colour.green())
        await interaction.response.send_message(embed=embed)
        await defer(ephemeral=False, thinking=False)



#mute command
@client.tree.command(name="mute", description="add role 'mute' to someone")
async def mute(interaction: discord.Interaction, member: discord.Member):
    # Role "Muted"
    muted_role = discord.utils.get(interaction.guild.roles, name="Muted")
    newbie = discord.utils.get(interaction.guild.roles, name="Newbie")
    if not muted_role:
        # Create the "Muted" role with necessary permissions
        muted_role = await interaction.guild.create_role(name="Muted", permissions=discord.Permissions(send_messages=False, speak=False))

        # Apply the "Muted" role to the default text channels (optional)
        for channel in interaction.guild.text_channels:
            await channel.set_permissions(muted_role, send_messages=False)

    # Add the "Muted" role to the member
    await member.add_roles(muted_role)
    print(f"{member.mention} has been muted.")

    # Send a DM to the muted user
    embed = discord.Embed(title="You have been Muted", description="You have been muted in the server.")
    await member.send(embed=embed)

    # Send a message using interaction response
    response_embed = discord.Embed(title="User Muted", description=f"{member.mention} has been muted :white_check_mark:" , color=discord.Colour.red())
    await interaction.response.send_message(embed=response_embed)

    # Remove the "Newbie" role (optional)
    await member.remove_roles(newbie)


# TODO 
#unmute command
@client.tree.command(name="unmute", description="Unmute someone")
async def mute(interaction: discord.Interaction, member: discord.Member):
    # Role "Muted"
    muted_role = discord.utils.get(interaction.guild.roles, name="Muted")
    newbie = discord.utils.get(interaction.guild.roles, name="Newbie")
    if not muted_role:
        # Create the "Muted" role with necessary permissions
        muted_role = await interaction.guild.create_role(name="Muted", permissions=discord.Permissions(send_messages=False, speak=False))

        # Apply the "unMuted" role to the default text channels (optional)
        for channel in interaction.guild.text_channels:
            await channel.set_permissions(muted_role, send_messages=False)

    # Add the "unMuted" role to the member
    await member.remove_roles(muted_role)
    print(f"{member.mention} has been unmuted.")

    # Send a DM to the unmuted user
    embed = discord.Embed(title="You have been unmuted", description="You have been Unmuted in the server.")
    await member.send(embed=embed)

    # Send a message using interaction response
    response_embed = discord.Embed(title="User Unmuted", description=f"{member.mention} has been Unmuted :white_check_mark:" , color=discord.Colour.green())
    await interaction.response.send_message(embed=response_embed)

    # Remove the "Newbie" role (optional)
    await member.add_roles(newbie)


@client.tree.context_menu(name="vocalmute")
async def mute2(interaction:discord.Interaction, member:discord.Member):
    await member.edit(mute=True)
    await interaction.response.send_message(f"{member} has been muted")

#events
#reminder to use listen and f everytime

@client.listen('on_message')
async def f2(message:discord.Message): 
    if any(x in message.content for x in blockedWords):
        await message.delete()
    client.process_commands(message)

@client.listen('on_message')
async def f1(message:discord.Message):
    if message.author == client.user:
        return
  
    pattern = re.compile(f"<@!?{client.user.id}>") # The exclamation mark is optional

    if pattern.match(message.content.lower()) is not None: # Checking whether the message matches our pattern
        await message.channel.send(f"**I am going to implode.** {message.author.mention}" , reference=message) 





#commands

@client.tree.command(name="random" , description="Gives you a random number beetween 1 and 1000000")
async def random(interaction: discord.Interaction):
    import random
    await interaction.response.send_message(view=MyView2())

@client.tree.command(name="express_rage" , description="EXPRESS YOUR RAGE")
async def express_rage(interaction: discord.Interaction):
    await interaction.response.send_message(view=MyView3())


@client.tree.command(name="meme" , description="Send a random meme")
async def meme(interaction:discord.Interaction):
    await interaction.response.send_message(view=MyView())

@client.tree.command(name="rules")
async def rules(interaction:discord.Interaction):
    embed=discord.Embed(title="Rules", description="https://docs.google.com/document/d/14fmVt4_eU3QesQVC8VfkSKL0i4EB5hQVI1c3RRCUUOE/edit?usp=sharing" , color=discord.Colour.dark_blue())
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="clear",description="Delete Messages automatically from the current channel")
async def clear(bot, number:int, member:discord.Member = None):
  channel = bot.channel
  if number > 50:
    number = 50
  def check_(m):
    return m.author == member
  if not member:
    await channel.purge(limit=number)
  else:
    await channel.purge(limit=number,check=check_)
  await bot.response.send_message(f"**{number}** message(s) deleted")




#buttons

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me to generate a meme !", style=discord.ButtonStyle.primary, emoji="🤣") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self , interaction , button):
        await interaction.response.send_message(embed=await pyrandmeme()) # Send a message when the button is clicked

class MyView2(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me to check the ping", style=discord.ButtonStyle.success) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self , interaction , button):
        await interaction.response.send_message(f"Pong! {round(client.latency * 1000)}ms") # Send a message when the button is clicked


class MyView3(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me to EXPRESS YOUR RAGE", style=discord.ButtonStyle.danger) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self , interaction , button):
        button.label = "No more pressing!" # change the button's label to something else
        button.disabled = True # set button.disabled to True to disable the button
        await interaction.response.send_message("**I am going to implode.**") # Send a message when the button is clicked



#TOKEN

client.run(TOKEN)
