from discord.ext import commands

# Importing bot modules
from .log import not_alone

# Commands
@commands.command(name="", help="")
async def name(ctx):
    await ctx.send("Hello World!")

# Code
def setup(bot):
    bot.add_command(name)

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()