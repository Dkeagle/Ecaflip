import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Importing bot modules
from modules.config import PREFIX, NAME
from modules.log import log

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
async def on_command(ctx):
    if ctx.message.author == bot.user:
        return
    splitted = ctx.message.content.split()
    if len(splitted) >= 2:
        log(f"{splitted[0]} {splitted[1:]}", ctx.message.channel.name, ctx.message.author)
    else:
        log(f"{splitted[0]}", ctx.message.channel.name,ctx.message.author)

@bot.event
async def on_command_error(ctx, error):
    splitted = ctx.message.content.split()
    text = f"{error}"
    lvl = "ERROR"
    if isinstance(error, commands.CommandNotFound):
        text = f"{splitted[0]}: Unknown command"
        lvl = "WARN"
    elif isinstance(error, commands.MissingPermissions):
        text = f"{splitted[0]}: You're not allowed to execute this command"
        lvl = "WARN"
    await ctx.send(text)
    log(text, channel=ctx.message.channel.name, user=ctx.message.author, level=lvl)

@bot.event
async def on_disconnect():
    log(f"{NAME} logged out!", level="INFO")

# Commands
@bot.command()
@commands.has_permissions(administrator=True)
async def logout(ctx):
    await bot.close()

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx):
    bot.reload_extension("modules.extensions")

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx):
    splitted = ctx.message.content.split()
    if len(splitted) == 1:
        return
    else:
        for extension in splitted[1:]:
            ext = f"modules.{extension}"
            try:
                bot.unload_extension(ext)
            except Exception as err:
                log(f"{ext} not unloaded! ({err})", level="ERROR")
            else:
                log(f"{ext} unloaded!", level="INFO")

# Load extensions
bot.load_extension("modules.extensions")

# Start the bot
if __name__ == "__main__":
    bot.run(TOKEN)
