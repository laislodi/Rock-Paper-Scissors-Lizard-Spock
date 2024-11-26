from random import randrange
from enum import StrEnum

class Options(StrEnum):
    ROCK = "rock"
    SCISSORS = "scissors"
    PAPER = "paper"
    LIZARD = "lizard"
    SPOCK = "spock"

options = [Options.ROCK, Options.PAPER, Options.SCISSORS, Options.LIZARD, Options.SPOCK]

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

ROCK_LIZARD = "Rock crushes Lizard"
ROCK_SCISSORS = "Rock crushes Scissors"
PAPER_ROCK = "Paper covers Rock"
PAPER_SPOCK = "Paper disproves Spock"
SCISSORS_PAPER = "Scissors cuts Paper"
SCISSORS_LIZARD = "Scissors decapitates Lizard"
LIZARD_PAPER = "Lizard eats Paper"
LIZARD_SPOCK = "Lizard poisons Spock"
SPOCK_SCISSORS = "Spock smashes Scissors"
SPOCK_ROCK = "Spock vaporizes Rock"
TIE = "It's a Tie!"


def whoAreYou(player: str) -> Options:
    match player:
        case "o" | "rock":
            role = Options.ROCK
        case "p" | "paper":
            role = Options.PAPER
        case "x" | "scissors":
            role = Options.SCISSORS
        case "l" | "lizard":
            role = Options.LIZARD
        case "w" | "spock":
            role = Options.SPOCK
        case "exit":
            role = "exit"
        case _:
            role = "invalid"
            
    return role


# Wheh the player is Rock
def resultForRock(computer: Options) -> str:
    match computer:
        case Options.ROCK:
            result = TIE
        case Options.SCISSORS:
            result = "Congratulations! {}".format(ROCK_SCISSORS)
        case Options.LIZARD:
            result = "Congratulations! {}".format(ROCK_LIZARD)
        case Options.PAPER:
            result = "Oh no... You lost. {}".format(PAPER_ROCK)
        case Options.SPOCK:
            result = "Oh no... You lost. {}".format(SPOCK_ROCK)
    return result


# Wheh the player is Paper 
def resultForPaper(computer: Options) -> str:
    match computer:
        case Options.ROCK:
            result = "Congratulations! {}".format(PAPER_ROCK)
        case Options.PAPER:
            result = TIE
        case Options.SCISSORS:
            result = "Oh no... You lost. {}".format(SCISSORS_PAPER)
        case Options.LIZARD:
            result = "Congratulations! {}".format(LIZARD_PAPER)
        case Options.SPOCK:
            result = "Oh no... You lost. {}".format(PAPER_SPOCK)
    return result


# Wheh the player is Scissors 
def resultForScissors(computer: Options) -> str:
    match computer:
        case Options.ROCK:
            result = "Oh no... You lost. {}".format(ROCK_SCISSORS)
        case Options.PAPER:
            result = "Congratulations! {}".format(SCISSORS_PAPER)
        case Options.SCISSORS:
            result = TIE
        case Options.LIZARD:
            result = "Congratulations! {}".format(SCISSORS_LIZARD)
        case Options.SPOCK:
            result = "Oh no... You lost. {}".format(SPOCK_SCISSORS)
    return result


# Wheh the player is Lizard 
def resultForLizard(computer: Options) -> str:
    match computer:
        case Options.ROCK:
            result = "Oh no... You lost. {}".format(ROCK_LIZARD)
        case Options.PAPER:
            result = "Congratulations! {}".format(LIZARD_PAPER)
        case Options.SCISSORS:
            result = "Oh no... You lost. {}".format(SCISSORS_LIZARD)
        case Options.LIZARD:
            result = TIE
        case Options.SPOCK:
            result = "Congratulations! {}".format(LIZARD_SPOCK)
    return result


# Wheh the player is Spock 
def resultForSpock(computer: Options) -> str:
    match computer:
        case Options.ROCK:
            result = "Congratulations! {}".format(SPOCK_ROCK)
        case Options.PAPER:
            result = "Oh no... You lost. {}".format(PAPER_SPOCK)
        case Options.SCISSORS:
            result = "Congratulations! {}".format(SPOCK_SCISSORS)
        case Options.LIZARD:
            result = "Oh no... You lost. {}".format(LIZARD_SPOCK)
        case Options.SPOCK:
            result = TIE
    return result


player = ""

while player != "exit":
    print("Rock(O), Paper(P), Scissors(X), Lizard(L) or Spock(W)? (type exit if you want to leave) ")
    player = whoAreYou(input().lower())
    if player == "exit":
        break

    if player != "invalid":
        computer = options[randrange(0, 5)]
        print(f"--- I chose {computer} and you chose {player} ---")
        
        match player:
            case Options.ROCK:
                result = resultForRock(computer)
            case Options.PAPER:
                result = resultForPaper(computer)
            case Options.SCISSORS:
                result = resultForScissors(computer)
            case Options.LIZARD:
                result = resultForLizard(computer)
            case Options.SPOCK:
                result = resultForSpock(computer)
        
        print(result)
    else:
        print("Invalid option, please try again")
