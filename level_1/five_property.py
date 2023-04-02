"""
Возьмите класс пользователя из предыдущего упражнения и перепишите вычисление возраста.

Раньше это был метод, а теперь это вычисляемое свойство – как метод, но его можно вызывать без скобок.

Пример использования ниже.
"""
import datetime


class User:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    @property
    def age(self):
        return datetime.date.today().year - self.birth_date.year


if __name__ == "__main__":
    jack = User(first_name="Jack", last_name="Dwane", birth_date=datetime.date(1962, 2, 7))
    assert jack.age == 61

    assert isinstance(User.age, property)
