# import random
import telebot
import exec
from telebot import types

import connection
import parse_ua
import token_bot
import request_db
import create_img

bot = telebot.TeleBot(token_bot.token)

status = ""
question_number = 0
questions_list = []
# word = exec.get_question()
word = ""
id_to_del = 0


@bot.message_handler(commands=["start"])
def start(message):
    """Start function, when user sends '/start'"""
    global status
    # request_db.connect()
    status = "username"
    if connection.check_userid(message.from_user.id):
        bot.send_message(message.chat.id, "Start game or check your information")
    else:
        bot.send_message(message.chat.id, text="To play, you need to register first! Type your Username")
    # bot.send_message(message.chat.id, text="Hello, enter your Username")


def create_card(message):
    global status, word
    try:
        bot.delete_message(message.chat.id, message.message_id - 1)
    except telebot.apihelper.ApiTelegramException:
        print("Smth")
    finally:
        status = "game"
        word = exec.get_question()
        create_img.img_cr(word.title())
        bot.send_photo(message.chat.id, open("img_done.png", "rb"), "Guess translation!")
    # bot.send_message(message.chat.id, text=word)


@bot.message_handler(commands=["startgame"])
def start_game(message):
    global status
    create_card(message)


@bot.message_handler(content_types=["text"])
def respond(message):
    """Functions for responses for user messages"""
    global status
    if status == "username":
        if not connection.check_userid(message.from_user.id):
            status = ""
            print(message.from_user.id)
            connection.registration(message.from_user.id, message.text)
            bot.send_message(message.chat.id, text="Thank you for the registration")
        else:
            username = connection.get_username(message.from_user.id)
            bot.send_message(message.chat.id, text=f"You already registered\nYour username --- {username}")
        # name = message.from_user.id
    elif status == "game":
        trans_answer = str(exec.get_translation(message.text))
        if word.lower() in trans_answer.lower():
            exec.add_mark(message.from_user.id)
            bot.send_message(message.chat.id, text="Right!")
        else:
            bot.send_message(message.chat.id, text="Wrong!")
        create_card(message)


bot.polling()


