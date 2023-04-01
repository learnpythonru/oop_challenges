"""
Возьмите класс пользователя из предыдущего упражнения и перепешите вычисление возраста.

Раньше это был метод, а теперь это вычисляемое свойство – как метод, но его можно вызывать без скобок.

Пример использования ниже.
"""
import datetime


class User:
    pass  # код писать тут


if __name__ == "__main__":
    jack = User(first_name="Jack", last_name="Dwane", birth_date=datetime.date(1962, 2, 7))
    assert jack.age == 61

    assert isinstance(User.age, property)
