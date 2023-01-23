"""Importing translator module"""
from googletrans import Translator

translator = Translator()


def get_translation(answer):
    """Getting translation of users respond"""
    trans_answer = translator.translate(answer, src="auto", dest="en").text
    return trans_answer


def get_back_translation(word):
    """Getting correct answer, if user was not right"""
    answers = [translator.translate(word, src="en", dest="uk").text,
               translator.translate(word, src="en", dest="ru").text]
    return answers

#DeFakto
