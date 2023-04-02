"""
Напишите класс пользователя, который при создании принимает на вход три параметра – имя, фамилию и дату рождения и
сохраняет их в инстанс (объект).

Пример использования можно посмотреть ниже.

Если код написан верно, этот скрипт выполнится без ошибок.
"""
import datetime


class User:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date


if __name__ == "__main__":
    jack = User(first_name="Jack", last_name="Dwane", birth_date=datetime.date(1962, 2, 7))
    assert jack.first_name == "Jack"
    assert jack.last_name == "Dwane"
    assert jack.birth_date == datetime.date(1962, 2, 7)

    jack.last_name = "Lex"
    assert jack.last_name == "Lex"

    # тут мы проверяем, что имя, фамилия и возраст недоступны у самого класса, а есть только у инстанса
    assert not hasattr(User, "first_name")
    assert not hasattr(User, "last_name")
    assert not hasattr(User, "birth_date")
