"""Importing connection module"""
import connection

mydb = connection.mydb

mycursor = mydb.cursor()

mycursor.execute("USE sql11591858")


def check_userid(user_id):
    """Function to check if user is already registered or not"""
    mycursor.execute(f"SELECT TRUE From Users WHERE TelegramUserId = {user_id} LIMIT 1;")
    if mycursor.fetchone() is None:
        return False
    else:
        return True


def get_username(user_id):
    """Function to get username"""
    mycursor.execute(f"SELECT * FROM `Users` WHERE TelegramUserId={user_id}")
    myresult = mycursor.fetchall()
    return list(myresult[0])[2]


def registration(user_id, username):
    """Function to register new user"""
    mycursor.execute(f"INSERT INTO Users (TelegramUserId, UserName)"
                     f" VALUES ({user_id}, '{username}')")
    mydb.commit()


def get_question():
    """Function to get random word from DataBase"""
    mycursor.execute("SELECT * FROM Questions order by RAND() LIMIT 1;")
    word = list(mycursor.fetchone())[0]
    return word


def add_mark(user_id):
    """Function to add mark, if user responds properly"""
    mycursor.execute(f"UPDATE Users SET Level = Level + 1 WHERE TelegramUserId = '{user_id}'")
    mydb.commit()


def set_last_word(user_id, word):
    """Function to set last word that was asked to user"""
    mycursor.execute(f"UPDATE Users SET Last_word = '{word}' WHERE TelegramUserId = '{user_id}'")
    mydb.commit()


def get_last_word(user_id):
    """Function to get last word that was asked to user"""
    mycursor.execute(f"SELECT Last_word FROM Users WHERE TelegramUserId = '{user_id}'")
    last_word = list(mycursor.fetchone())[0]
    return last_word


def info(user_id):
    """Function to get information about user"""
    mycursor.execute(f"SELECT * FROM Users WHERE TelegramUserId = '{user_id}'")
    res = list(mycursor.fetchall())[0]
    res_list = [x for x in res]
    return res_list

#DeFakto
