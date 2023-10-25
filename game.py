import random

print("Welcome to classic Rock, Paper, Scissors!")

userScore = 0
computerScore = 0


def startGame():
    global userScore
    global computerScore

    userMove = input("\nPlease type your move: Rock, Paper, or Scissors: \n")
    computerMove = random.choice(["Rock", "Paper", "Scissors"])


startGame()
