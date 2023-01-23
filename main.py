"""Importing asyncio, telebot modules
and database.py, translator.py, create_img.py files as modules"""
import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
import database
import translator
import token_bot
import create_img

bot = AsyncTeleBot(token_bot.token)

STATUS = ""


async def main():
    """Function main"""
    @bot.message_handler(commands=["start"])
    async def start(message):
        """Start function, when user sends '/start'"""
        global STATUS
        STATUS = "username"
        if database.check_userid(message.from_user.id):
            await bot.send_message(message.chat.id, "Start game or check your information")
        else:
            await bot.send_message(message.chat.id,
                                   text="To play, you need to register first! Type your Username")

    @bot.message_handler(commands=["startgame"])
    async def game(message):
        """Function to start the game"""
        global STATUS
        try:
            await bot.delete_message(message.chat.id, message.message_id - 1)
        except telebot.apihelper.ApiTelegramException:
            print("We got an error, captain!")
        finally:
            STATUS = "game"
            word = database.get_question()
            database.set_last_word(message.from_user.id, word)
            create_img.img_cr(word.title())
            with open("Images/img_done.png", "rb") as img:
                await bot.send_photo(message.chat.id, img, "Guess translation!")

    @bot.message_handler(commands=["info"])
    async def info(message):
        """Function to send info about user"""
        info_list = database.info(message.from_user.id)
        await bot.send_message(message.chat.id,
                               text=f"Information about you:\n"
                                    f"Username - {info_list[2]}\n"
                                    f"Tasks completed successfully - {info_list[3]} ")

    @bot.message_handler(content_types=["text"])
    async def respond(message):
        """Functions for responses for user messages"""
        global STATUS
        if STATUS == "username":
            if not database.check_userid(message.from_user.id):
                STATUS = ""
                database.registration(message.from_user.id, message.text)
                await bot.send_message(message.chat.id, text="Thank you for the registration")
            else:
                username = database.get_username(message.from_user.id)
                await bot.send_message(message.chat.id,
                                       text=f"You already registered\nYour username --- {username}")
        elif STATUS == "game":
            user_answer = str(translator.get_translation(message.text)).lower()
            right_answer = database.get_last_word(message.from_user.id).lower()
            if right_answer in user_answer:
                database.add_mark(message.from_user.id)
                await bot.send_message(message.chat.id, text="Right!")
            else:
                answers = translator.get_back_translation(right_answer)
                await bot.send_message(message.chat.id,
                                       text=f"Wrong!\n"
                                            f"Right answer is '{answers[0]}' or '{answers[1]}'")
            await game(message)
        else:
            await bot.send_message(message.chat.id, text="Type /start or /info")
    await AsyncTeleBot.infinity_polling(bot)

asyncio.run(main())

#DeFakto
