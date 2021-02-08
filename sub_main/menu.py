def menu_top():
    print('-'*30)
    print(('-'*13) + 'Menu' + ('-' * 13))
    print('1. Create new user')
    print('2. Use an existing user')
    print('Q. Exit this program')
    print('-'*30)
    return input(': ')


def menu_games():
    print('-'*30)
    print(('-'*13) + 'Games' + ('-' * 13))
    print('1. Rock, Paper, Scissors')
    print('2. Tic Tac Toe')
    print('3. Checkers')
    print('4. Space Invaders')
    print('5. Age Guesser')
    print('Q. Exit this program')
    print('-'*30)
    return input(': ')
