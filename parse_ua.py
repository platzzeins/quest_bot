# """Importing modules - requests and BeautifulSoup"""
# import requests
# from bs4 import BeautifulSoup
#
#
# def request_page():
#     """Function to request web page"""
#     with open("parsed_page.html", 'w', encoding="utf-8") as file:
#         url = "https://www.mindyourlogic.com/riddles-with-answers/100-riddles-with-answer-for-kids-and-adults?page=1"
#         request = requests.get(url, timeout=10)
#         file.write(request.text)
#
#
# def parse_questions():
#     """Function to parse page and get questions with answers"""
#     request_page()
#     with open("parsed_page.html", 'r', encoding="utf-8") as file:
#         item = BeautifulSoup(file, "html.parser")
#         question_all = item.find_all("div", {"class": "col-sm-10"})
#         answers_all = item.find_all("ul",
#                                     {"class": "-toggle-nav list-unstyled fw-normal pb-1 small"})
#         questions = [question.find('p', {"class" : "para"}).text for question in question_all]
#         answers = [answer.find("pre").text.lower() for answer in answers_all]
#         result = dict(zip(questions, answers))
#         print(result)
#         return result
