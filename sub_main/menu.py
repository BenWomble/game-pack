from sub_main import games


def menu_top():
    print('-'*32)
    print(('-'*14) + 'Menu' + ('-' * 14))
    print('1. Create new user')
    print('2. Use an existing user')
    print('Q. Exit this program')
    print('-'*32)
    return input(': ')


def menu_games():
    print('-'*32)
    print(('-'*14) + 'Games' + ('-' * 13))
    print('1. Rock, Paper, Scissors')
    print('2. Tic Tac Toe')
    print('3. Checkers')
    print('4. Space Invaders')
    print('5. Age Guesser')
    print('Q. Exit this program')
    print('-'*30)
    choice = input(': ')
    while True:
        if choice == '1':
            games.rock_paper_scissors.rps.choose_option()
            break
        if choice == '2':
            games.tic_tac_toe.ttt.coming_soon()
            break
        if choice == '3':
            games.checkers.checkers.coming_soon()
            break
        if choice == '4':
            games.space_invaders.si.coming_soon()
            break
        if choice == '5':
            games.age_guesser.ag.coming_soon()
            break
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
                break
            elif quit_choice in ["n", "N"]:
                print()
                print('-' * 32)
                print('Returning to Main Menu')
                print('-' * 32)
                menu_games()
