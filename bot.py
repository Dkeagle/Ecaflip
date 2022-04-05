import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Importing bot modules
from config import PREFIX, NAME
from log import log

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create the bot client
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX))

# Event Handlers
@bot.event
async def on_ready():
    log(f"{NAME} logged in!", level="INFO")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    splitted = message.content.split()
    if len(splitted) >= 2:
        log(f"{splitted[0]} {splitted[1:]}", message.channel.name, message.author)
    else:
        log(f"{splitted[0]}", message.channel.name, message.author)
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    splitted = ctx.message.content.split()
    if isinstance(error, commands.CommandNotFound):
        text = f"{splitted[0]}: Unknown command!"
    elif isinstance(error, commands.MissingPermissions):
        text = f"{splitted[0]}: You're not allowed to execute this command!"
    await ctx.send(text)
    log(text, channel=ctx.message.channel.name, user=ctx.message.author, level="WARN")

@bot.event
async def on_disconnect():
    log(f"{NAME} logged out!", level="INFO")

# Commands
@bot.command()
@commands.has_permissions(administrator=True)
async def logout(ctx):
    await bot.close()

# Load extensions
bot.load_extension("dice")

# Start the bot
if __name__ == "__main__":
    bot.run(TOKEN)
