import GuassGame
import MemoryGame
import CurrencyRouletteGame
from utils import screen_cleaner


def welcome():
    name = str(input("Please enter your name:\n"))
    print("Hello" + " " + name,
          "and welcome to the World of Games(WoG)\n" "Here you can find many cool games to play.\n")


def game_difficulty():

    difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
    while difficulty > 5:
        print("Input should be a number between 1 - 5\n")
        difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
    return difficulty


def load_game():
    welcome()
    difficulty = game_difficulty()

    print("Please choose a game to play:\n"
          "1. Memory game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
          "2. Guess Game - guess a number and see if you choose like the computer.\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n")
    game_number = int(input("Your choice:\n"))
    while game_number > 3:
        print("Input should be a number between 1 - 3\n")
        game_number = int(input("Your choice:\n"))

    if game_number == 1:
        MemoryGame.play(difficulty)
    elif game_number == 2:
        GuassGame.play(difficulty)
    else:
        CurrencyRouletteGame.play(difficulty)

screen_cleaner()
load_game()