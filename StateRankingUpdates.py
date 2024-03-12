import os

import discord
from discord import Intents, Client, Message
from discord import app_commands
from discord.ext import commands
import responses
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

r = requests.get('https://osuworld.octo.moe/')






load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
targeted_user = ""
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

TARGET_FILE = "target.txt"

async def send_message(message: Message) -> None:
   
    try:
        await message.channel.send('https://tenor.com/view/brick-wall-talk-gif-5290288')
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!', flush=True)
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name="target", description="target selector for brick wall gif")
@commands.has_role("mod")
async def target(interaction: discord.Interaction, new_targeted_user: str):
    
    global targeted_user 
    targeted_user = new_targeted_user
    with open(TARGET_FILE, "w") as file:
        file.write(targeted_user)
    
    await interaction.response.send_message(f"target has been set: {targeted_user} ")
    


@client.event
async def on_message(message)-> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    
    print(f"[{channel} {username} '{user_message}']", flush=True)
    if str(message.author) != targeted_user:
        return
    await send_message(message)

if os.path.exists(TARGET_FILE):
    with open(TARGET_FILE, "r") as file:
        targeted_user = file.read()
        
client.run(TOKEN)