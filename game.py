# importing Python modules

import random
import time
import sys

print("Welcome to classic Rock, Paper, Scissors!")

userScore = 0
computerScore = 0


def countdown(game_time):
    while game_time:
        mins, secs = divmod(game_time, 60)

        timeformat = "Rock, Paper, Scissors, Shoot! {:2d}:{:2d}\n".format(mins, secs)

        print(timeformat, end="\r")

        time.sleep(0.5)
        game_time -= 1


def startGame():
    global userScore
    global computerScore

    userMove = input(
        "\nPlease type your move: Rock, Paper, or Scissors: \n"
    ).capitalize()
    computerMove = random.choice(["Rock", "Paper", "Scissors"])

    countdown(4)

    print(f"\nUser: {userMove}")
    print(f"Computer: {computerMove}\n")

    if (
        userMove == "Rock"
        and computerMove == "Paper"
        or userMove == "Scissors"
        and computerMove == "Rock"
        or userMove == "Paper"
        and computerMove == "Scissors"
    ):
        print("Computer wins")
        computerScore += 1

        print(userScore)
        print(computerScore)

    elif (
        userMove == "Paper"
        and computerMove == "Rock"
        or userMove == "Rock"
        and computerMove == "Scissors"
        or userMove == "Scissors"
        and computerMove == "Paper"
    ):
        print("User wins")
        userScore += 1

        print(userScore)
        print(computerScore)

    else:
        print("Its a draw")

        print(userScore)
        print(computerScore)

    while True:
        if userScore < 4 and computerScore < 4:
            startGame()
        else:
            print("\nBest of 7 reached. Game Over")
            print("\nRun program to play again\n")
            sys.exit()


startGame()
