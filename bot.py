# Importing python libraries
import os
import discord
from dotenv import load_dotenv

# Importing bot modules
from config import PREFIX, NAME
from log import log

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the bot client
client = discord.Client()

@client.event
async def on_ready():
    log(f"{NAME} is online!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(PREFIX):
        splitted = message.content.split()
        if len(splitted) >= 2:
            log(f"{splitted[0]} {splitted[1:]}", message.channel.name, message.author)
        else:
            log(f"{splitted[0]}", message.channel.name, message.author)

# Start the bot
if __name__ == "__main__":
    client.run(TOKEN)