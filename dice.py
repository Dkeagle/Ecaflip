from discord.ext import commands

# Importing bot modules
from log import log, not_alone

# Commands
@commands.command(name="d6", help="Roll a d6")
async def d6(ctx):
    await ctx.send("Hello!")

# Code
def setup(bot):
    bot.add_command(d6)

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()