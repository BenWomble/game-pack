import mysql.connector


#  Local SQL Database Connection:

def sql_connect_local():
    mydb = mysql.connector.connect(
        host='192.168.10.76',
        user='sql-wombo',
        passwd='COMMD0m@!n',
        database='game_pack'
    )
    return mydb

#  Global SQL Database Connection:


def sql_connect_global():
    mydb = mysql.connector.connect(
        host='65.184.83.159',
        user='sql-wombo',
        passwd='COMMD0m@!n',
        database='game_pack'
    )
    return mydb
