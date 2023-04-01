"""
Возьмите класс из предыдущего упражнения и добавьте ему метод should_be_banned.
Он проверяет, должен ли быть пользователь забанен.

Пользователя стоит забанить, если его фамилия находится в last_names_to_ban.
"""
import datetime


class User:
    last_names_to_ban = {"Vaughn", "Wilhelm", "Santaros", "Porter", "Smith"}
    # код писать тут


if __name__ == "__main__":
    ok_user = User(first_name="Jack", last_name="Dwane", birth_date=datetime.date(1962, 2, 7))
    assert not ok_user.should_be_banned()

    weird_user = User(first_name="Rick", last_name="Smith", birth_date=datetime.date(2007, 19, 4))
    assert weird_user.should_be_banned()

    # проверяем, что last_names_to_ban доступны и у класса и у инстанса
    assert hasattr(User, "last_names_to_ban")
    assert hasattr(ok_user, "last_names_to_ban")

    # проверяем, что можно поменять last_names_to_ban у конкретного инстанса
    # и тогда они поменяются только у него, а не у класса
    user = User(first_name="Rick", last_name="Smith", birth_date=datetime.date(2007, 19, 4))
    user.last_names_to_ban = {}
    assert not user.should_be_banned()
    assert len(User.last_names_to_ban) == 5
