import fib
import hello

print(fib.recur_fib(4))
print(hello.get_hello())

# Ошибки
# SyntaxError
# Exceptions


try:
    2 / 0
    1 + "one"
except ZeroDivisionError:
    print('Error div 0')
except TypeError:
    print('Error type')

# ООП: Классы, объекты, атрибуты и методы

class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    # self- ссылка на объект (экземпляр) класса, через эту переменную осуществляется доступ к атрибутам класса
    # Атрибуты класса объявляются вне любого метожа, а атрибуты экземпляра - внутри метода
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("Заводим автомобиль")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1

    def on_auto_stop(self):
        print("Останавливаем работу")

a = Auto() # объект (экземпляр) класса
print(a)
a.on_auto_start("Lexus", "570", 2022)
print(a.auto_name)
print(a.auto_count)
b = Auto()
b.on_auto_start("BMW", "x6", 2019)
print(b.auto_name)
print(b.auto_count)