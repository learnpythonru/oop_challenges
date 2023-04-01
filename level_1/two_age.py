"""
Возьмите класс пользователя из предыдущего упражнения и добавьте ему метод,
который будет вычислять возраст конкретного пользователя.
"""
import datetime


class User:
    pass  # код писать тут


if __name__ == "__main__":
    jack = User(first_name="Jack", last_name="Dwane", birth_date=datetime.date(1962, 2, 7))
    assert jack.get_age() == 61

    # тут мы проверяем, что у метода для подсчёта возраста нет аргументов
    assert User.get_age.__code__.co_argcount == 1
