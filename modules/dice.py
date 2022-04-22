from discord.ext import commands
from random import randint

# Importing bot modules
from .log import not_alone

# Commands
@commands.command(name="d4", help="Roll a D4")
async def d4(ctx):
    await ctx.send(f"d4: {randint(1, 5)}")

@commands.command(name="d6", help="Roll a d6")
async def d6(ctx):
    await ctx.send(f"d6: {randint(1, 7)}")

@commands.command(name="d8", help="Roll a d8")
async def d8(ctx): 
    await ctx.send(f"d8: {randint(1, 9)}")

@commands.command(name="d10", help="Roll a d10")
async def d10(ctx):
    await ctx.send(f"d10: {randint(1, 11)}")

@commands.command(name="d12", help="Roll a d12")
async def d12(ctx):
    await ctx.send(f"d12: {randint(1, 13)}")

@commands.command(name="d20", help="Roll a d20")
async def d20(ctx):
    await ctx.send(f"d20: {randint(1, 21)}")

@commands.commant(name="d100", help="Roll a d100")
async def d100(ctx):
    await ctx.send(f"d100: {randint(1, 101)}")

# TODO: User should be able to roll multiples dices at once

# Code
def setup(bot):
    bot.add_command(d4)
    bot.add_command(d6)
    bot.add_command(d8)
    bot.add_command(d10)
    bot.add_command(d12)
    bot.add_command(d20)
    bot.add_command(d100)

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()