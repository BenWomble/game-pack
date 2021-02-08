#  Standard library import
import random

#  Username Input
#  from sub_main import username

#  Victory/Defeat Messages
from sub_main.outcomes import player_win
from sub_main.outcomes import comp_win

comp_wins = 0
player_wins = 0


def choose_option():
    user_pick = input("Choose [R]ock, [P]aper, [S]cissors:     ")
    if user_pick in ["r", "R"]:
        user_pick = "R"
    elif user_pick in ["p", "P"]:
        user_pick = "P"
    elif user_pick in ["s", "S"]:
        user_pick = "S"
    else:
        print("Nice Try! That is breaking the rules, try again.")
        choose_option()
    return user_pick


def computer_option():
    comp_pick = random.randint(1, 3)
    if comp_pick == 1:
        comp_pick = "R"
    elif comp_pick == 2:
        comp_pick = "P"
    else:
        comp_pick = "S"
    return comp_pick


def user():

    return user


while True:
    print("")
    quit_choice: str = choose_option()
    comp_choice = computer_option()
    print("")

    if quit_choice == "R":
        if comp_choice == "R":
            print("You chose rock. The computer chose rock. You tied.")
        elif comp_choice == "P":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
        elif comp_choice == "S":
            print("You chose rock. The computer chose scissors. You win!")
            player_wins += 1

    elif quit_choice == "P":
        if comp_choice == "P":
            print("You chose paper. The computer chose paper. You tied.")
        elif comp_choice == "S":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1
        elif comp_choice == "R":
            print("You chose paper. The computer chose rock. You win!")
            player_wins += 1

    elif quit_choice == "S":
        if comp_choice == "S":
            print("You chose scissors. The computer chose scissors. You tied.")
        elif comp_choice == "R":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
        elif comp_choice == "P":
            print("You chose scissors. The computer chose paper. You win!")
            player_wins += 1

    print("")
    print(str(user), "wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    quit_choice = input("Do you want to play again? (y/n):     ")
    if quit_choice in ["y", "Y"]:
        pass
    elif quit_choice in ["n", "N"]:
        if str(player_wins) > str(comp_wins):
            print(player_win.message())
        else:
            print(comp_win.message())
        break
    else:
        if str(player_wins) > str(comp_wins):
            print(player_win.message())
        else:
            print(comp_win.message())
    break
