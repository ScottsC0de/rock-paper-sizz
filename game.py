import random

print("Welcome to classic Rock, Paper, Scissors!")

userScore = 0
computerScore = 0


def startGame():
    global userScore
    global computerScore

    userMove = input("\nPlease type your move: Rock, Paper, or Scissors: \n")
    computerMove = random.choice(["Rock", "Paper", "Scissors"])

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


startGame()
