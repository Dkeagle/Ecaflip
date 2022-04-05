from discord.ext import commands

# Importing bot modules
from log import log, not_alone

# Code
extensions = ["dice"]
reload_list = []

def setup(bot):
    for ext in extensions:
        try:
            bot.load_extension(ext)
        except commands.ExtensionAlreadyLoaded:
            reload_list.append(ext)
        except Exception as err:
            log(f"{ext} module not loaded! ({err})", level="ERROR")
        else:
            log(f"{ext} module loaded!", level="INFO")

    for ext in reload_list:
        try:
            bot.reload_extension(ext)
        except Exception as err:
            log(f"{ext} module not reloaded! ({err})", level="ERROR")
        else:
            log(f"{ext} module reloaded!", level="INFO")

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()