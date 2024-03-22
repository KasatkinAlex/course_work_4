import pytest
from src.vacancy_class import Vacancy


@pytest.fixture
def vacancy_test():
    vacancy_lst = [{
                    "id": "94912480",
                    "premium": "false",
                    "name": "Frontend Web \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a",
                    "department": 'null',
                    "has_test": 'false',
                    "response_letter_required": 'false',
                    "area": {
                      "id": "2759",
                      "name": "\u0422\u0430\u0448\u043a\u0435\u043d\u0442",
                      "url": "https://api.hh.ru/areas/2759"
                    },
                    "salary": 'null',
                    "type": {
                      "id": "open",
                      "name": "\u041e\u0442\u043a\u0440\u044b\u0442\u0430\u044f"
                    },
                    "address": 'null',
                    "response_url": 'null',
                    "sort_point_distance": 'null',
                    "published_at": "2024-03-18T08:11:52+0300",
                    "created_at": "2024-03-18T08:11:52+0300",
                    "archived": 'false',
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=94912480",
                    "show_logo_in_search": 'null',
                    "insider_interview": 'null',
                    "url": "https://api.hh.ru/vacancies/94912480?host=hh.ru",
                    "alternate_url": "https://hh.ru/vacancy/94912480",
                    "relations": [],
                    "employer": {
                      "id": "1863460",
                      "name": "COSCOM \u0422\u041c Ucell",
                      "url": "https://api.hh.ru/employers/1863460",
                      "alternate_url": "https://hh.ru/employer/1863460",
                      "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/715320.png",
                        "90": "https://img.hhcdn.ru/employer-logo/3302396.png",
                        "240": "https://img.hhcdn.ru/employer-logo/3302397.png"
                      },
                      "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1863460",
                      "accredited_it_employer": 'false',
                      "trusted": 'true'
                    },
                    "snippet": {
                      "requirement": "JS.",
                      "responsibility": "qwe"
                    },
                    "contacts": 'null',
                    "schedule": {
                      "id": "fullDay",
                      "name": "\u041f\u043e\u043b\u043d\u044b\u0439 \u0434\u0435\u043d\u044c"
                    },
                    "working_days": [],
                    "working_time_intervals": [],
                    "working_time_modes": [],
                    "accept_temporary": 'false',
                    "professional_roles": [
                      {
                        "id": "96",
                        "name": "qwe"
                      }
                    ],
                    "accept_incomplete_resumes": 'false',
                    "experience": {
                      "id": "between1And3",
                      "name": "\u041e\u0442 1 \u0433\u043e\u0434\u0430 \u0434\u043e 3 \u043b\u0435\u0442"
                    },
                    "employment": {
                      "id": "full",
                      "name": "qwe"
                    },
                    "adv_response_url": 'null',
                    "is_adv_vacancy": 'false',
                    "adv_context": 'null'
                  }]
    return vacancy_lst


def test_cast_to_object_list(vacancy_test):
    # vacancy = Vacancy("1", 10, 20, "ok", "url", "22-02", "RUS")
    vacancy_lst = Vacancy.cast_to_object_list(vacancy_test)
    assert len(vacancy_lst) == 1


def test_gt():
    """Тест на сравнение"""
    vacancy1 = Vacancy("1", 10, 20, "ok", "url", "22-02", "RUS")
    vacancy2 = Vacancy("2", 100, 200, "ok", "url", "22-02", "RUS")
    assert (vacancy1 < vacancy2) == 1
