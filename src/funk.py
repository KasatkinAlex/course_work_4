from src.api_hh import HeadHunterAPI
from src.vacancy_class import Vacancy
from operator import itemgetter

# api = HeadHunterAPI()

def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    salary_range = input("Введите диапазон зарплат: ").split("-") # Пример: 100000 - 150000

    api = HeadHunterAPI()
    res = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(res)

    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(top_vacancies)


def filter_vacancies(vacancies_list, filter_words):
    filtered_vacancies = []
    for i in vacancies_list:
        if filter_words in i.snippet:
            filtered_vacancies.append(i)
    return vacancies_list  # yflj vtyznm


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    ranged_vacancies = []
    salary_from = int(salary_range[0])
    salary_to = int(salary_range[1])
    print(salary_from, salary_to)
    for vacancy in filtered_vacancies:
        if vacancy.salary_from >= salary_from: #and vacancy.salary_to < salary_to:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    return sorted(ranged_vacancies, key=lambda x: x.name)


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[0:top_n]


if __name__ == "__main__":
    user_interaction()
