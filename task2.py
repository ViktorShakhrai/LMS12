# Завдання 2
# математик
# Реалізуйте клас Mathematician, який є допоміжним класом для виконання математичних операцій зі списками
# Клас не приймає жодних атрибутів і має лише методи:
# square_nums (бере список цілих чисел і повертає список квадратів)
# remove_positives (бере список цілих чисел і повертає його без додатних чисел
# filter_leaps (бере список дат (цілих) і видаляє ті, які не є "високосними роками"


class Mathematician:
    def square_nums(self, numbers: list):
        """Бере список цілих чисел і повертає список квадратів"""
        numbers = [i ** 2 for i in numbers]
        return numbers

    def remove_positives(self, numbers: list):
        """Бере список цілих чисел і повертає його без додатних чисел"""
        numbers = [i for i in numbers if i < 0]
        return numbers

    def filter_leaps(self, years: list):
        years = [i for i in years if i % 4 == 0]
        return years


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
