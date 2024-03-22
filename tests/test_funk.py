import pytest
from src.vacancy_class import Vacancy
from src.funk import filter_vacancies, get_vacancies_by_salary


@pytest.fixture
def vacancy_test():
    vacancy_lst = []
    vacancy1 = Vacancy("1", 10, 20, "ok", "url", "22-02", "RUS")
    vacancy_lst.append(vacancy1)
    vacancy2 = Vacancy("2", 100, 200, "ok", "url", "22-02", "RUS")
    vacancy_lst.append(vacancy2)
    return vacancy_lst


def test_filter_vacancies(vacancy_test):
    filter_words = "ок"
    filter_vacancy = filter_vacancies(vacancy_test, filter_words)
    assert len(filter_vacancy) == 2


def test_get_vacancies_by_salary(vacancy_test):
    salary = [10, 20]
    ranged_vacancies = get_vacancies_by_salary(vacancy_test, salary)
    assert len(ranged_vacancies) == 1
