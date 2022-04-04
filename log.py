# Importing python libraries
from datetime import datetime

# Importing bot modules
from config import NAME

# Functions
def time():
    return datetime.now().strftime("[%Y/%m/%d %H:%M:%S.%f]")

def log(message, channel="None", user=NAME):
    print(f"{time()}: #{channel}: @{user}: {message}")
    with open("logs/{}.log".format(log_file_name),"a") as lf:
        lf.write(f"{time()}: #{channel}: @{user}: {message}\n")

def not_alone():
    log("This module is part of the Ecaflip Discord Bot Project and should not be used alone, please use bot.py")

# Code
log_file_name = datetime.now().strftime('%Y%m%d-%H%M%S')
log(f"{__name__} module loaded!")

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()