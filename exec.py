import mysql.connector
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
# from google_trans_new import google_translator

# translator = google_translator()


translator = Translator()

result = []

mydb = mysql.connector.connect(
        host="sql11.freesqldatabase.com",
        user="sql11591858",
        password="29TRNkP3gD",
        port=3306
    )

mycursor = mydb.cursor()

mycursor.execute("USE sql11591858")

#
# def request_page():
#     """Function to request web page"""
#     with open("parsed_page.html", 'w', encoding="utf-8") as file:
#         url = "https://www.englishdom.com/skills/glossary/wordset/top-100-slov-urovnya-elementary/"
#         request = requests.get(url, timeout=10)
#         file.write(request.text)
#
#
# def parse_questions():
#     """Function to parse page and get questions with answers"""
#     global result
#     request_page()
#     with open("parsed_page.html", 'r', encoding="utf-8") as file:
#         item = BeautifulSoup(file, "html.parser")
#         question_all = item.find_all("p", {"class": "word"})
#         answers_all = item.find_all("p", {"class": "translate"})
#         questions = [question.text for question in question_all]
#         answers = [answer.text.lower() for answer in answers_all]
#         result = list(zip(questions, answers))
#         print(result)
#
#
# def fun():
#     parse_questions()
#     for _, val in enumerate(result):
#         mycursor.execute(f"INSERT INTO Questions (question) VALUES ('{val[0]}')")
#         mydb.commit()


def get_question():
    global mycursor
    # mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Questions order by RAND() LIMIT 1;")
    word = list(mycursor.fetchone())[0]
    print(word)
    # mydb.close()
    return word


def get_translation(answer):
    trans_answer = translator.translate(answer, src="auto", dest="en").text
    print(trans_answer)
    return trans_answer


def add_mark(id):
    mycursor.execute(f"UPDATE Users SET Level = Level + 1 WHERE TelegramUserId = {id}")
    mydb.commit()
