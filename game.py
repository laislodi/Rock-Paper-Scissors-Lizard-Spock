from random import randrange

ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"
LIZARD = "lizard"
SPOCK = "spock"

options = [ROCK, PAPER, SCISSORS, LIZARD, SPOCK]

#  Rules:
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors


player = ""

while player != "exit":
    print("Rock, Paper, Scissors, Lizard or Spock? (type exit if you want to leave) ")
    player = input().lower()
    if player == "exit":
        break

    computer = options[randrange(0, 5)]
    print(f"--- I chose {computer} and you chose {player} ---")
    if player == computer:
        print("It's a tie!")
    elif player == SCISSORS:
        if computer == PAPER:
            print("Scissors cuts Paper, you won!")
        elif computer == LIZARD:
            print("Scissors decapitates Lizard, you won!")
        elif computer == SPOCK:
            print("Spock smashes Scissors, you lost...")
        else:
            print("Rock crushes Scissors, you lost...")
    elif player == PAPER:
        if computer == ROCK:
            print("Paper covers Rock, you won!")
        elif computer == SPOCK:
            print("Paper disproves Spock, you won!")
        elif computer == SCISSORS:
            print("Scissors cuts Paper, you lost...")
        else:
            print("Lizard eats Paper, you lost...")
    elif player == ROCK:
        if computer == LIZARD:
            print("Rock crushes Lizard, you won!")
        elif computer == SCISSORS:
            print("Rock crushes Scissors, you won!")
        elif computer == PAPER:
            print("Paper covers Rock, you lost...")
        else:
            print("Spock vaporizes Rock, you lost...")
    elif player == LIZARD:
        if computer == SPOCK:
            print("Lizard poisons Spock, you won!")
        elif computer == PAPER:
            print("Lizard eats Paper, you won!")
        elif computer == SCISSORS:
            print("Scissors decapitates Lizard, you lost...")
        else:
            print("Rock crushes Lizard, you lost...")
    elif player == SPOCK:
        if computer == SCISSORS:
            print("Spock smashes Scissors, you won!")
        elif computer == ROCK:
            print("Spock vaporizes Rock, you won!")
        elif computer == LIZARD:
            print("Lizard poisons Spock, you lost...")
        else:
            print("Paper disproves Spock, you lost...")
