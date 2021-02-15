from sub_main.users import user
from sub_main.SQL import sql_database_connect
from sub_main import menu
#  from main import game_choice

mydb = sql_database_connect.sql_connect_local()

SQL_CONNECT = sql_database_connect.sql_connect_local()
mycursor = SQL_CONNECT.cursor()

#  SQL Database SELECT

#  SQL_FORMULA_FIND = f"SELECT name FROM users WHERE name=''"
#  mycursor.execute(SQL_FORMULA_FIND)
#  myresult = mycursor.fetchall()


def find_id():
    sql_formula_find_id = "SELECT ID FROM Users WHERE id=(SELECT max(id) FROM Users)"
    mycursor.execute(sql_formula_find_id)
    myresult = mycursor.fetchone()
    for last_id in myresult:
        return last_id


a_id = find_id()
n_id = int(a_id) + int(1)
n_id = str(n_id)

#  for last_id in myresult:
#      a_id: int = last_id
#  n_id = int(a_id) + int(1)
#  n_id = str(n_id)


def create_insert():
    global n_id
    n_username = user.username()
    n_password = user.password()
    f_name = user.f_name()
    l_name = user.l_name()

    #  SQL Database INSERT

    sql_formula_insert = f"INSERT INTO Users (ID, Username, Password, F_Name, L_Name) VALUES (%s, %s, %s, %s, %s)"
    user_data = (str(n_id),
                 str(n_username),
                 str(n_password),
                 str(f_name),
                 str(l_name))
    mycursor.execute(sql_formula_insert, user_data)
    SQL_CONNECT.commit()


def find_user():
    sql_formula_find_username = f"SELECT Username FROM Users WHERE Username=" + "'" + str(user.get_username() + "'")
    mycursor.execute(sql_formula_find_username)
    myresult = mycursor.fetchone()
    for user_id in myresult:
        return user_id


def pull_pass():
    sql_formula_find_password = f"SELECT Password FROM Users WHERE Username=" + "'" + str(user.get_username() + "'")
    mycursor.execute(sql_formula_find_password)
    myresult = mycursor.fetchone()
    for user_pass in myresult:
        return user_pass


def check_pass():
    print()
    print('-' * 32)
    print('|        Enter Password        |')
    print('-' * 32)
    print()
    password = input(':  ')
    return password


def get_user():
    while True:
        if find_user() == user.get_username():

            #  Password

            while True:
                pass_input = check_pass()
                if pass_input == pull_pass():
                    menu.menu_games()
                    break
                else:
                    print()
                    print('The password you entered was not correct. Try again.')
                    exit()

        else:
            print()
            print('That user does not exist.')
            get_user()
            pass
