# bot.py
import os

import discord
from discord import Intents, Client, Message, has_permission, app_commands

import responses
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name="target",
    description="Choose a person to target for brick wall."
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

async def send_message(message: Message) -> None:
   
    try:
        await message.channel.send('https://tenor.com/view/brick-wall-talk-gif-5290288')
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!', flush=True)
    await tree.sync()
    print("Ready!")
@client.event
async def on_message(message)-> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    
    print(f"[{channel} {username} '{user_message}']", flush=True)
    if str(message.author) != str("bazingasdead"):
        return
    await send_message(message)
client.run(TOKEN)
@bot.command(pass_context=True)
@has_permission(administrator=True)
async def on_message(target)-> None:
    
   

 client.run(TOKEN)