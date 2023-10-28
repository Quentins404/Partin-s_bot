#imports
import random
import colorsys
import discord
import defer
import datetime
from datetime import timedelta
from datetime import datetime
from discord import app_commands
from discord import embeds
from discord import colour
from discord import *
from discord import ui
from discord.ext import *
from discord.ext import commands, tasks
from discord import Client, Intents
from blockedWords import BlockedWords
import os
import time
from token_1 import TOKEN
import pyrandmeme
from pyrandmeme import *
import requests
import re
import traceback
import discord_webhook
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord import Webhook
import aiohttp

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1164254536370753617/H_DRo-v8dOasB-jbTwFpHLNTnSXlknrHiOVQ7cK2Q7l7bxialucxId_Teu7DRjIMix4r")

# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color="03b2f8") number
embed = DiscordEmbed(title="Bot Status", description="The bot is on", color="86FF33")

# add embed object to webhook
webhook.add_embed(embed)
response = webhook.execute()


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



async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1163207286265757746/_lMMvWZk0oElY9zvjgZAgQnZa2JaekN5VdqSt6527OU_32PpMtH9ttGts3kHcm1cx1el', session=session)
        await webhook.send(content='Hello World', username='Foo')

#join message
@client.listen('on_member_join')
async def f3(member):
    channel = client.get_channel(1154470707032494142)
    embed=discord.Embed(title="Welcome!",description=f"{member.mention}just arrived!" , color=discord.Colour.green())
    await channel.send(embed=embed)

# Commands 

@client.tree.command(name="help" , description="Gives ypou all the commands")
async def help(interaction: discord.Interaction):
    embed=discord.Embed(title="**Commands list**",description="/status \n \n /youtube \n \n /help \n \n /commands \n \n /version \n \n /ping \n \n /random \n \n /express_rage \n \n /meme  " , color=discord.Colour.yellow())
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="ping" , description="Replies with a Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(view=MyView2())



@client.tree.command(name="version" , description="Gives you the version of the bot")
async def version(interaction: discord.Interaction):
    embed=discord.Embed(title="Version of the bot" , description="Bot version: V.1.20 \n Python version: 3.11.4 " , color=discord.Colour.dark_purple())
    embed.set_image(url="https://i.ibb.co/T2KvY7w/t-l-chargement.png")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="youtube" , description="Gives you info about the owners youtube channels ")
async def youtube(interaction: discord.Interaction):
    embed=discord.Embed(title="Youtube channels" , description="Quentin's : https://www.youtube.com/@Quentins_dev \n \n Par : https://www.youtube.com/@parYTGshorts " , color=discord.Colour.red())
    await interaction.response.send_message(embed=embed)



@client.tree.command(name="status", description="gives you the status of the server")
async def status(interaction: discord.Interaction):
        embed=discord.Embed(title="**I'm checking the status...**",description="The server is ON :green_square: \n \n To connect , just go on the #How-to-connect channel." , color=discord.Colour.green())
        await interaction.response.send_message(embed=embed)
        await defer(ephemeral=False, thinking=False)


@client.tree.context_menu(name="vocalmute")
async def mute2(interaction:discord.Interaction, member:discord.Member):
    await member.edit(mute=True)
    await interaction.response.send_message(f"{member} has been muted")

#events
#reminder to use listen and f everytime

@client.listen('on_message')
async def f2(message:discord.Message): 
    if any(x in message.content for x in BlockedWords):
        await message.delete() 
    await client.process_commands(message)

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
    await interaction.response.send_message(random.randint(0, 1000000))

@client.tree.command(name="express_rage" , description="EXPRESS YOUR RAGE")
async def express_rage(interaction: discord.Interaction):
    await interaction.response.send_message(view=MyView3())


@client.tree.command(name="meme" , description="Send a random meme")
async def meme(interaction:discord.Interaction):
    await interaction.response.send_message(view=MyView())



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
  await client.response.send_message(f"{number} message(s) deleted")




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
