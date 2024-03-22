import json
from src.vacancy_class import Vacancy


class JSONSaver:
    """ Сохранение вакансий в json файл """

    def __init__(self):
        self.dict = {}

    def object_in_json(self, vacancy: Vacancy):
        """ Создает json для записи его в файл"""
        self.dict["name"] = vacancy.name
        self.dict["salary_from"] = vacancy.salary_from
        self.dict["salary_to"] = vacancy.salary_to
        self.dict["snippet"] = vacancy.snippet
        self.dict["alternate_url"] = vacancy.alternate_url
        self.dict["published_dat"] = vacancy.published_dat
        self.dict["city"] = vacancy.city

    @staticmethod
    def read_json() -> list:
        """ Чтение файла и перевод из json"""
        with open("file_vacancy.json", "r", encoding="utf-8") as file:
            try:
                file_json = json.load(file)
            except json.decoder.JSONDecodeError:
                file_json = []
        return file_json

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в файл"""
        self.object_in_json(vacancy)
        try:
            file_json = self.read_json()
        except FileNotFoundError:
            with open("file_vacancy.json", "w", encoding="utf-8"):
                file_json = []
        file_json.append(self.dict)
        with open("file_vacancy.json", "w", encoding="utf-8") as file:
            json.dump(file_json, file)

    def delete_vacancy(self, vacancy):
        """Удаление вакансии из файла"""
        self.object_in_json(vacancy)
        file_json = self.read_json()
        for i in file_json:
            if i == self.dict:
                file_json.remove(self.dict)
        with open("file_vacancy.json", "w", encoding="utf-8") as f:
            json.dump(file_json, f)
