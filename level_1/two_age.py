"""
Возьмите класс пользователя из предыдущего упражнения и добавьте ему метод,
который будет вычислять возраст конкретного пользователя.
"""
import datetime


class User:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_age(self):
        return datetime.date.today().year - self.birth_date.year


if __name__ == "__main__":
    jack = User(first_name="Jack", last_name="Dwane", birth_date=datetime.date(1962, 2, 7))
    assert jack.get_age() == 61

    # тут мы проверяем, что у метода для подсчёта возраста нет аргументов
    assert User.get_age.__code__.co_argcount == 1
