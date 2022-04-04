# Importing python libraries
import os
import discord
from dotenv import load_dotenv

# Importing bot modules
from log import log

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
NAME = os.getenv('BOT_NAME')

# Create the bot client
client = discord.Client()

@client.event
async def on_ready():
    log(f"{NAME} is online!")
    await client.close()

# Start the bot
if __name__ == "__main__":
    client.run(TOKEN)