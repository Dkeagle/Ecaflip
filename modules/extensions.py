from discord.ext import commands

# Importing bot modules
from .log import log, not_alone

# Code
extensions = ["dice", "hangman"]
load_list = [f"modules.{ext}" for ext in extensions]
reload_list = []

def setup(bot):
    for ext in load_list:
        try:
            bot.load_extension(ext)
        except commands.ExtensionAlreadyLoaded:
            reload_list.append(ext)
        except Exception as err:
            log(f"{ext} not loaded! ({err})", level="ERROR")
        else:
            log(f"{ext} loaded!", level="INFO")

    for ext in reload_list:
        try:
            bot.reload_extension(ext)
        except Exception as err:
            log(f"{ext} not reloaded! ({err})", level="ERROR")
        else:
            log(f"{ext} reloaded!", level="INFO")

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()