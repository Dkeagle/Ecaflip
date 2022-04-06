from discord.ext import commands
import random
import json

# Importing bot modules
from .log import not_alone

# Functions
def help_hangman():
    """Show help message"""
    return "Start a new game:\n => hangman start\n\nSubmit a letter:\n => hangman submit [letter]\n\nStop the game:\n => hangman stop"

def random_word():
    """Return a random word from the hangman.txt file"""
    with open("modules/hangman.txt", "r") as f:
        words_list = f.readlines()
        word = random.choice(words_list)

    return word.rstrip()

def format_block(message):
    """Return a string with the discord codeblock markdown"""
    return f"```{message}```"

def search_letter(text, char):
    """Return a list with the position of char in text (empty list if no match)"""
    return [i for i, letter in enumerate(text) if letter == char]

def end_game(word, win):
    """Return win or lose message and reset the game cache"""
    if win:
        text = f"You win! the word was: {word}"
    else:
        text = f"You lose! the word was: {word}"

    with open("modules/hangman.json", "w") as f:
        json.dump({"word": "", "hidden_word": "", "lives":0, "letters": []}, f)

    return text 

def show_hangman(lives, letters):
    """Show the hanged man status depending of remaining life points"""
    formated_letters = ", ".join(letter for letter in letters)
    if lives == 9:
        return f"{letters}"
    elif lives == 8:
        return f"\n\n\n\n\n\n=======\n{formated_letters}"
    elif lives == 7:
        return f"\n|\n|\n|\n|\n|\n=======\n{formated_letters}"
    elif lives == 6:
        return f"\n+----+\n|    |\n|\n|\n|\n|\n=======\n{formated_letters}"
    elif lives == 5:
        return f"\n+----+\n|    |\n|    o\n|\n|\n|\n=======\n{formated_letters}"
    elif lives == 4:
        return f"\n+----+\n|    |\n|    o\n|    |\n|\n|\n=======\n{formated_letters}"
    elif lives == 3:
        return f"\n+----+\n|    |\n|    o\n|   /|\n|\n|\n=======\n{formated_letters}"
    elif lives == 2:
        return f"\n+----+\n|    |\n|    o\n|   /|\\\n|\n|\n=======\n{formated_letters}"
    elif lives == 1:
        return f"\n+----+\n|    |\n|    o\n|   /|\\\n|   /\n|\n=======\n{formated_letters}"
    elif lives == 0:
        return f"\n+----+\n|    |\n|    o\n|   /|\\\n|   / \\\n|\n=======\n{formated_letters}"

# Commands
@commands.command(name="hangman", help="Play Hangman")
async def hangman(ctx):
    # Check if file exists
    try:
        with open("modules/hangman.json", "r") as f:
            data = json.load(f)
            word = data['word']
            hidden_word = data['hidden_word']
            lives = data['lives']
            letters = data['letters']
    except FileNotFoundError:
            word = ""
            hidden_word = ""
            lives = 0
            letters = []

    splitted = ctx.message.content.split()

    if len(splitted) >= 2 and splitted[1] == "start":
        # Start a new game
        word = random_word()
        hidden_word = len(word)*"-" 
        with open("modules/hangman.json", "w") as f:
            json.dump({"word": word, "hidden_word":hidden_word, "lives":9, "letters":[]}, f)
        await ctx.send(format_block(f"New game as started, the word you're looking for is {len(word)} characters long!\n\n{hidden_word}"))
    elif len(splitted) >= 2 and splitted[1] == "stop":
        # reset the game
        if word == "":
            await ctx.send(format_block("No game is running, you must start a game first with\n => hangman start"))
        else:
            await ctx.send(format_block(end_game(word, 0)))
    elif len(splitted) >= 2 and splitted[1] == "submit":
        # Check if game is already running
        if word == "":
            await ctx.send(format_block("No game is running, you must start a game first with\n => hangman start"))
            return
        # Check if a letter have been specified
        if len(splitted) == 2:
            await ctx.send(format_block("You must specify a letter to submit!"))
        # Search for letter in word
        else:
            letter = splitted[2].lower()
            # Check if user submitted a letter or a word
            if len(letter) > 1:
                if letter != word:
                    lives -= 1
                else:
                    hidden_word = word
            else:
                result = search_letter(word, letter)
                if len(result) == 0:
                    lives -= 1
                else:
                    tmp = list(hidden_word)
                    for i in result:
                        tmp[i] = letter
                    hidden_word = "".join(tmp)

            # Add letter to used letters
            if letter not in letters:
                letters.append(letter)

            # Show status of the game 
            await ctx.send(format_block(show_hangman(lives, letters)))
            await ctx.send(format_block(hidden_word))
            print(word)

            # Update JSON file
            with open("modules/hangman.json", "w") as f:
                json.dump({"word": word, "hidden_word":hidden_word, "lives":lives, "letters":letters}, f)

            if lives == 0:
                await ctx.send(format_block(end_game(word, 0)))
            if hidden_word == word:
                await ctx.send(format_block(end_game(word, 1)))

        # Display help message
    else:
        await ctx.send(format_block(help_hangman()))

# Code
def setup(bot):
    bot.add_command(hangman)

# Block execution of this file alone
if __name__ == "__main__":
    not_alone()