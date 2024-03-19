class Vacancy:
    name: str  # название вакансии
    salary_from: int  # зарплата от
    salary_to: int  # зарплата до
    snippet: str  # описание
    alternate_url: int  # ссылка на вакансию
    published_dat: str  # дата публикации
    city: str  #  город

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
                if salary_from == None:
                    salary_from = 0
            except TypeError:
                salary_from = 0

            try:
                salary_to = info["salary"]["to"]
                if salary_to == None:
                    salary_to = 0
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
        if self.salary_from == 0:
            self.salary_from = "З/п не указана"
        if self.salary_to == 0:
            self.salary_to = "З/п не указана"
        return (f"Вакансия: {self.name}\n"
                f"Зарплата от: {self.salary_from} до: {self.salary_to}\n"
                f"Описание: {self.snippet}\n"
                f"ссылка на вакансию: {self.alternate_url}\n"
                f"дата публикации: {self.published_dat}\n"
                f"город: {self.city}\n\n")

    def __gt__(self, other):
        return self.salary_from > other.salary_from


