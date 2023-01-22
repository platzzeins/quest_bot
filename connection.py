import mysql.connector

mydb = mysql.connector.connect(
        host="sql11.freesqldatabase.com",
        user="sql11591858",
        password="29TRNkP3gD",
        port=3306
    )

mycursor = mydb.cursor()

mycursor.execute("USE sql11591858")

mycursor.execute("SELECT TelegramUserId FROM Users")


def check_userid(user_id):
    # mycursor.execute("SELECT TelegramUserId FROM Users")
    mycursor.execute(f"SELECT TRUE From Users WHERE TelegramUserId = {user_id} LIMIT 1;")
    if mycursor.fetchone() is None:
        return False
    else:
        return True
    # print(mycursor.fetchone())
    # if not user_id:
    #     return True
    # else:
    #     return False
    # return mycursor


def get_username(user_id):
    mycursor.execute(f"SELECT * FROM `Users` WHERE TelegramUserId={user_id}")
    myresult = mycursor.fetchall()
    # print(myresult)
    return list(myresult[0])[2]


def registration(user_id, username):
    print(user_id)
    mycursor.execute(f"INSERT INTO Users (TelegramUserId, UserName) VALUES ({user_id}, '{username}')")
    mydb.commit()
    mycursor.execute(f"SELECT * FROM Users")
    for x in mycursor:
        print(x)


for x in mycursor:
    print(x)

print(mydb)