from abc import ABC, abstractmethod
from pprint import pprint
import json

import requests

url = "https://api.hh.ru/vacancies"


class ApiAbstractClass(ABC):
    """ Абстрактный класс для работы с API сервиса с вакансиями """
    @abstractmethod
    def get_vacancies(self, vacancies):
        pass

    @abstractmethod
    def save_vacancies_in_fail(self, qwerty):
        pass


class HeadHunterAPI(ApiAbstractClass):
    """Класс для работы с API сервиса с вакансиями"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 1}
        self.vacancies = []

    def get_vacancies(self, keyword):
        if isinstance(keyword, str):
            self.params['text'] = keyword
            while self.params.get('page') != 20:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                if response.ok:
                    vacancies = response.json()['items']
                    self.vacancies.extend(vacancies)
                    self.params['page'] += 1
                else:
                    raise ValueError("НЕТ ПОДКЛЮЧЕНИЯ К САЙТУ")
            return self.vacancies
        else:
            raise ValueError("Ввели цифренное значение")

    # def get_vacancies(self, vacancies):
    #     if isinstance(vacancies, str):
    #         response = requests.request("Get", url, params={'text': {vacancies}, "per_page": 100, "salary": 100000})
    #         if response.ok:
    #             return response.json()["items"]
    #         else:
    #             raise ValueError("НЕТ ПОДКЛЮЧЕНИЯ К САЙТУ")
    #     else:
    #         raise ValueError("Ввели цифренное значение")

    def save_vacancies_in_fail(self, vacancies_lst):
        with open("hh.json", "w", encoding="utf-8") as fail:
            fail.write(json.dumps(vacancies_lst))


class Vacancy:
    name: str  # название вакансии
    salary_from: int  # зарплата от
    salary_to: int  # зарплата до
    snippet: str  # описание
    alternate_url: int  # ссылка на вакансию
    published_dat: str  # дата публикации
    city: str  # город

    def __init__(self, name, salary_from, salary_to, snippet, alternate_url, published_dat, city ):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.snippet = snippet
        self.alternate_url = alternate_url
        self.published_dat = published_dat
        self.city = city

    @classmethod
    def cast_to_object_list(cls, vacancy: list):
        vacancy_object_lst = []
        for info in vacancy:
            name = info["name"]
            try:
                salary_from = info["salary"]["from"]
            except TypeError:
                salary_from = 0

            try:
                salary_to = info["salary"]["to"]
            except TypeError:
                salary_to = 0
            snippet = info["snippet"]["requirement"]
            published_dat = info["published_at"]
            alternate_url = info["alternate_url"]
            city = info["area"]["name"]
            vacancy_object = cls(name, salary_from, salary_to, snippet, alternate_url, published_dat, city)
            vacancy_object_lst.append(vacancy_object)
        return vacancy_object_lst

    def __str__(self):
        if self.salary_from == 0 or self.salary_from == None:
            self.salary_from = "З/п не указана"
        if self.salary_to == 0 or self.salary_to == None:
            self.salary_to = "З/п не указана"
        return (f"Вакансия: {self.name}\n"
                f"Зарплата от: {self.salary_from} до: {self.salary_to}\n"
                f"Описание: {self.snippet}\n"
                f"ссылка на вакансию: {self.alternate_url}\n"
                f"дата публикации: {self.published_dat}\n"
                f"город: {self.city}\n\n")

    def __gt__(self, other):
        return self.salary_from > other.salary_from



if __name__ == "__main__":
    api = HeadHunterAPI()
    res = api.get_vacancies("Python")
    api.save_vacancies_in_fail(res)

    vacancies = Vacancy.cast_to_object_list(res)
    print(vacancies[0] > vacancies[1])
    # for i in vacancies:
    #     print(i)
    # print(res)
    # api.save_vacancies_in_fail(res)
    # pprint(res)

    # with open("hh.json", encoding="utf-8") as fail:
    #     res1 = json.load(fail)
    # for i in res1:
    #     print(i["published_at"])

