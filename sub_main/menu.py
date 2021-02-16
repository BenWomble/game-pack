from sub_main.games.age_guesser import ag
from sub_main.games.checkers import checkers

from sub_main.games.space_invaders import si
from sub_main.games.tic_tac_toe import ttt


def menu_top():
    print('-'*32)
    print(('-'*14) + 'Menu' + ('-' * 14))
    print('1. Create new user')
    print('2. Use an existing user')
    print('Q. Exit this program')
    print('-'*32)
    return input(': ')


def menu_games():
    print('-' * 32)
    print(('-' * 14) + 'Games' + ('-' * 13))
    print('1. Rock, Paper, Scissors')
    print('2. Tic Tac Toe')
    print('3. Checkers')
    print('4. Space Invaders')
    print('5. Age Guesser')
    print('Q. Exit this program')
    print('-' * 30)
    choice = input(': ')
    run = True
    while run:
        if choice == '1':
            from sub_main.games.rock_paper_scissors import rps
            rps
        if choice == '2':
            ttt.coming_soon()
        if choice == '3':
            checkers.coming_soon()
        if choice == '4':
            si.coming_soon()
        if choice == '5':
            ag.coming_soon()
        if choice in ['q', 'Q', 'quit', 'Quit']:
            choice = 'Q'
            print()
            print('-' * 32)
            print("Do you want to quit? (y/n)")
            print('-' * 32)
            quit_choice = input(":")
            if quit_choice in ["y", "Y"]:
                print()
                print('-' * 32)
                print('Goodbye. Have A Nice Day!')
                print('-' * 32)
                run = False
            elif quit_choice in ["n", "N"]:
                print()
                print('-' * 32)
                print('Returning to Main Menu')
                print('-' * 32)
                menu_games()
            pass
