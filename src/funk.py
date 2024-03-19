from src.api_hh import HeadHunterAPI
from src.vacancy_class import Vacancy


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий в описании: ")
    salary_range = input("Введите диапазон зарплат через '-' пример: 10000-15000: ").split("-") # Пример: 100000 - 150000

    api = HeadHunterAPI()
    res = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(res)

    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


def filter_vacancies(vacancies_list, filter_words):
    """Фильрация по ключевым словам в описании принимет, список обьектов Vacanncy и фильтруемое слово"""
    filtered_vacancies = []
    for i in vacancies_list:
        if filter_words.lower() in i.snippet.lower():
            filtered_vacancies.append(i)
    if len(filtered_vacancies) == 0:
        print("Вакансии по фильтрации по ключевым словам не найдена, мы упустили этот критерий \n")
        return vacancies_list
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
    Фильтрация списка обьектов Vacancy
    :param filtered_vacancies: список обьектов
    :param salary_range: str пример 10000-200000
    :return:
    """
    ranged_vacancies = []
    try:
        salary_from = int(salary_range[0])
    except ValueError:
        print("Ввели не правильный диапазон зарплат")
        salary_from = int(input("Введите нижний порог зарплат"))
    try:
        salary_to = int(salary_range[1])
    except Exception:
        salary_to = int(input("Введите вверхнйзг порог зарплат"))
    print(f"зарплаты от {salary_from}, до {salary_to} \n")
    for vacancy in filtered_vacancies:
        if vacancy.salary_from >= salary_from and vacancy.salary_to <= salary_to:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    return sorted(ranged_vacancies, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[0:top_n]


def print_vacancies(top_vacancies):
    if len(top_vacancies) == 0:
        print("НИЧЕГО НЕ НАЙДЕНО")
    else:
        for i in top_vacancies:
            print(i)
    print("ПОИСК ЗАКОНЧЕН")
