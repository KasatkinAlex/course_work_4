from abc import ABC, abstractmethod
import requests


class ApiAbstractClass(ABC):
    """ Абстрактный класс для работы с API сервиса с вакансиями """
    @abstractmethod
    def get_vacancies(self, vacancies):
        pass


class HeadHunterAPI(ApiAbstractClass):
    """Класс для работы с API сервиса с вакансиями"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    @property
    def url(self):
        return self.__url

    def get_vacancies(self, keyword: str) -> list:
        """Подключается к url,с параметрами принимающими от пользователя поисковый запрос, возвращает список вакансий"""
        if isinstance(keyword, str):
            while self.params.get('page') != 10:
                self.params['text'] = keyword
                response = requests.get(self.__url, headers=self.headers, params=self.params)
                if response.ok:
                    vacancies = response.json()['items']
                    self.vacancies.extend(vacancies)
                    self.params['page'] += 1
                else:
                    raise ValueError("НЕТ ПОДКЛЮЧЕНИЯ К САЙТУ")
            return self.vacancies
        else:
            raise ValueError("Ввели цифренное значение")
