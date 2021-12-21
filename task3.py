# Завдання 3
# Магазин продуктів
# Напишіть клас Product, який має три атрибути:
# типу
# ім'я
# ціна
# Потім створіть клас ProductStore, який матиме деякі продукти і працюватиме з усіма продуктами в магазині.
# Усі методи, якщо вони не можуть виконати свою дію, повинні викликати ValueError з відповідною інформацією про помилку.
# Поради. Використовуйте концепції агрегації/композиції під час реалізації класу ProductStore.
# Ви також можете реалізувати додаткові класи для роботи з певним типом продукту тощо.

# Крім того, клас ProductStore повинен мати такі методи:

# add(product, amount) - додає певну кількість одного товару з попередньо визначеною надбавкою до ціни для вашого магазину (30 відсотків)
# set_discount(identifier, percent, identifier_type=’name’) - додає знижку на всі товари, визначені введеними ідентифікаторами (тип або назва).
# Знижка повинна бути вказана у відсотках
# sell_product(product_name, amount) - видаляє певну кількість товарів з магазину, якщо вони доступні, в іншому випадку викликає помилку.
# Він також збільшує прибуток, якщо метод sell_product успішний.
# get_income() - повертає кількість багатьох, зароблених екземпляром ProductStore.
# get_all_products() - повертає інформацію про всі наявні продукти в магазині.
# get_product_inf o(product_name) - повертає кортеж із назвою продукту та кількістю товарів у магазині.

class Product:
    def __init__(self, type: str, name: str, price: int):
        self.type = type
        self.name = name
        self.price = price


class Product_in_shop:
    def __init__(self, prod: "Product", nac=1):
        self.prod = prod
        self.amount = 0
        self.price = prod.price * nac


class ProductStore:
    K_NACENKI = 10

    def __init__(self, nacenka=10):
        self.K_NACENKI = nacenka
        self.all_products = []

    def add(self, product, amount):  # що за продукт, і його кідькість
        if amount < 0:
            raise ValueError
        for p in self.all_products:
            p: Product_in_shop
            if p.prod == product:
                p.amount += amount
            else:
                p = Product_in_shop(product)
                p.amount = amount
                self.all_products.append(p)

    def set_discount(self, identifier, percent):
        for p in self.all_products:
            if p.prod.name == identifier or p.prod.type == identifier:
                if p.prod.prise < (
                        p.prise * percent / 100):  # перевіряє що кінцева ціна товару зі знижкою не може бути мена ніж початкова ціна
                    p.prise = (p.prise * percent / 100)

    def sell_product(self, product_name, amount):
        pass

    def get_income(self):
        pass

    def get_all_products(self):
        pass

    def get_product_inf(self, product_name):
        pass


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product("Food", "Ramen", 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell("Ramen", 10)
assert s.get_product_info("Ramen") == ("Ramen", 290)
