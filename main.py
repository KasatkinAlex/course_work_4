import json

from src.api_hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy_class import Vacancy

vacancy = Vacancy("1", 22, 23, "qwer", "qwe", 21, "qwe")
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)
# with open("file_vacancy.json", "rt", encoding="utf-8") as fail:
#     q = json.load(fail)
#     print(type(q))
#     print(q)