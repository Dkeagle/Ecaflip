from discord.ext import commands

# Importing bot modules
from log import log

@commands.command(name="d6")
async def d6(ctx):
    await ctx.send("coucou")

def setup(bot):
    bot.add_command(d6)

log(f"{__name__} module loaded!")