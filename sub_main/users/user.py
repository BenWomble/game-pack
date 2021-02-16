#  Create a new user

def username():
    print()
    print('-' * 32)
    print('|        Create New User       |')
    print('-' * 32)
    print()
    print('-' * 32)
    print('Please input your new username.')
    print('-' * 32)
    n_username = input(':  ')
    return n_username


def password():
    print()
    print('-' * 32)
    print('|        Enter Password        |')
    print('-' * 32)
    print()
    n_password = input(':  ')
    return n_password


def f_name():
    print()
    print('-' * 32)
    print('|       Enter First Name       |')
    print('-' * 32)
    print()
    n_firstname = input(':  ')
    return n_firstname


def l_name():
    print()
    print('-' * 32)
    print('|        Enter Last Name       |')
    print('-' * 32)
    print()
    n_lastname = input(':  ')
    return n_lastname


#  Find an existing user

def get_username():
    print()
    print('-' * 32)
    print('|        Enter Username        |')
    print('-' * 32)
    print()
    g_username = input(':  ')
    return g_username


user_name = get_username()
