from src.api_hh import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy_class import Vacancy


def user_interaction():
    """ Взаимодействие с пользователем """
    search_query = str(input("Введите поисковый запрос: "))
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        top_n = int(input("Введите цифренное значение: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий в описании: ")
    salary_range = input("Введите диапазон зарплат через '-' пример: 10000-15000: ").split("-")

    api = HeadHunterAPI()
    res = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(res)

    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    save_file_user(input("Сохранить данные в файл - W |"
                         " Удалить эти данные из файла - N |"
                         " Ничего не делать любая клавиша\n"), top_vacancies)


def save_file_user(save_file: str, top_vacancies: list) -> None:
    """ Проверяет ответ пользователя и отправляет команду на запись, удаление найденных вакансий или ничего не делать
    принимает ответ пользователя и список вакансий"""
    save_json = JSONSaver()
    if save_file.lower() == "w":
        for vacancy in top_vacancies:
            save_json.add_vacancy(vacancy)
        print(f"Сохранены вакансии в файл в количестве {len(top_vacancies)}")
    elif save_file.lower() == "n":
        for vacancy in top_vacancies:
            save_json.delete_vacancy(vacancy)
        print("Вакансии удалены")
    else:
        print("Всего доброго")
    print(f"В файле сейчас {len(save_json.read_json())} выкансий")


def filter_vacancies(vacancies_list: list, filter_words: str) -> list:
    """ Фильрация по ключевым словам в описании примет список обьектов Vacancy и фильтруемое слово """
    filtered_vacancies = []
    for i in vacancies_list:
        if filter_words in str(i.snippet):
            filtered_vacancies.append(i)
    if len(filtered_vacancies) == 0:
        print(f"Вакансии по фильтрации по ключевым словам '{filter_words}' не найдена, мы упустили этот критерий \n")
        return vacancies_list
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list, salary_range: list) -> list:
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
        salary_from = int(input("Введите нижний порог зарплат "))
    try:
        salary_to = int(salary_range[1])
    except Exception:
        salary_to = int(input("Введите вверхнй порог зарплат "))
    print(f"зарплаты от {salary_from}, до {salary_to} \n")
    for vacancy in filtered_vacancies:
        if vacancy.salary_from >= salary_from and vacancy.salary_to <= salary_to:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies: list) -> list:
    """ Сортировка списка вакансий по зарплате """
    return sorted(ranged_vacancies, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(sorted_vacancies: list, top_n: int) -> list:
    """ Вывод первых отсортированных вакансий """
    return sorted_vacancies[0:top_n]


def print_vacancies(top_vacancies: list) -> None:
    """ Печать вакансий в терминал """
    if len(top_vacancies) == 0:
        print("НИЧЕГО НЕ НАЙДЕНО")
    else:
        for i in top_vacancies:
            print(i)
    print("ПОИСК ЗАКОНЧЕН")
