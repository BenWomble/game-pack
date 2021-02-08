from sub_main import menu
from sub_main.users import user

menu.menu_top()

choice = menu.menu_top()
while choice != 'Q':
    if choice == "1":
        user.new()
    elif choice == "2":
        user.get()
    else:
        choice = menu.menu_top()
exit()
