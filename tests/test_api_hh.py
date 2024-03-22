from src.api_hh import HeadHunterAPI


def test_get_vacancies():
    api = HeadHunterAPI()
    res = api.get_vacancies("Python")
    assert isinstance(res, list)
