"""
Возьмите класс из предыдущего упражнения и добавьте к нему метод is_relatve_to.

Этот метод инстанса, который принимает на вход другого пользователя и проверяет,
являются ли эти пользователя родственниками. Возвращает True/False.

Пользователи считаются родственниками, если у них одинаковые фамилии.
"""
import datetime


class User:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        
    def is_relatve_to(self, other_user):
        if self.last_name == other_user.last_name:
            return True
        else:
            return False


if __name__ == "__main__":
    son = User(first_name="Jr. Robert", last_name="Downey", birth_date=datetime.date(1965, 4, 4))
    father = User(first_name="Sr. Robert", last_name="Downey", birth_date=datetime.date(1936, 6, 24))
    some_other_guy = User(first_name="Josh", last_name="Brolin", birth_date=datetime.date(1968, 2, 12))

    assert father.is_relatve_to(son)
    assert son.is_relatve_to(father)
    assert not son.is_relatve_to(some_other_guy)
    assert not father.is_relatve_to(some_other_guy)
