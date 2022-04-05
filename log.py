from datetime import datetime

# Importing bot modules
from config import NAME

# Functions
def time():
    return datetime.now().strftime("[%Y/%m/%d %H:%M:%S.%f]")

def log(message, channel=None, user=NAME, level="DEFAULT"):
    levels = {"DEFAULT": '\033[0m', "INFO": '\033[0;36m', "WARN": '\033[0;33m', "ERROR": '\033[0;31m'}
    if level not in levels:
        log("Incorrect log level, please fix next command logging level", channel=None, user=NAME, level="ERROR")
        level="ERROR"

    text = f"{levels['DEFAULT']}{time()}:{levels[level]} #{channel}: @{user}: {message}" 
    print(text)
    with open("logs/{}.log".format(log_file_name),"a") as lf:
        lf.write(f"{text}\n")

def not_alone():
    log("This module is part of the Ecaflip Discord Bot Project and should not be used alone, please use bot.py")

# Code
log_file_name = datetime.now().strftime('%Y%m%d-%H%M%S')
log(f"{__name__} module loaded!", level="INFO")

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()