from abc import ABC, abstractmethod
import json
import requests


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

    def save_vacancies_in_fail(self, vacancies_lst):
        """ Сохранение вакансий в файл """
        with open("hh.json", "w", encoding="utf-8") as fail:
            fail.write(json.dumps(vacancies_lst))

