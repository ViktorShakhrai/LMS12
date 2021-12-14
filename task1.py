# Task 1
# School
#
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

# Завдання 1
# Школа
#
# Створіть структуру класу на python, що представляє людей у школі.
# Створіть базовий клас під назвою Person, клас під назвою Student і інший під назвою Teacher.
# Спробуйте знайти якомога більше методів і атрибутів, які належать до різних класів, і пам’ятайте,
# які є загальними, а які ні. Наприклад, ім’я має бути атрибутом Person, а зарплата повинна бути доступна лише викладачу.

class Person:
    def __init__(self,name: str,surname: str,age: int):
        self.name = name
        self.surname = surname
        self.age = age


class Teacher(Person):
    def __init__(self,salary: int,what_subject_teachers: str):
        self.salary = salary
        self.what_subject_teacher = what_subject_teachers


class Student(Person):
    def __init__(self,what_class: int,favorite_subject: str,):
        self.what_class = what_class