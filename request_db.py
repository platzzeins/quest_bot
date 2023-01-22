import connection

mydb = connection.mydb


def connect():
    mycursor = mydb.cursor()

    mycursor.execute("USE sql11591858; SHOW TABLES", multi=True)

    for x in mycursor:
        print(x)


