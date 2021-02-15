from sub_main import menu
#  from sub_main.users import user
from sub_main.SQL import sql_sequences

choice = menu.menu_top()
while True:
    if choice == "1":
        sql_sequences.create_insert()
        break
    if choice == "2":
        sql_sequences.get_user()
        break
    if choice in ['q', 'Q']:
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
            menu.menu_top()
            pass
        break
    else:
        choice = menu.menu_top()


def game_choice():
    game_pick = menu.menu_games()
    return game_pick
