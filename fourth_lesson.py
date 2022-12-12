#Конструктор - специальный метод, вызываемый при создании экземпляра класса
# class Auto:
#     auto_count = 0
#
#     #конструктор
#     def __init__(self):
#         Auto.auto_count += 1
#         print(Auto.auto_count)
#
# a = Auto()
# b = Auto()
# c = Auto()
#
#
# локальные переменные
# class Auto:
#     info_1 = "Aвтомобиль заведен"
#
#     def on_start(self):
#         info_2 = "Автомобиль заведен"
#         return info_2
#
# a = Auto()
# print(a.info_1)

# Модефикаторы доступа
# Public
# Protected
# Private

# class Auto:
#     def __init__(self):
#         print("Автомобиль заведён")
#         self.auto_name = "Mazda" #Публичная
#         self._auto_year = 2019 #Защищенная
#         self.__auto_model = "CX9" #Приватная
#
# a = Auto()
# print(a.auto_name)
# print(a._auto_year)
# print(a.__auto_model)

# Инкапсуляция
#
# class MyClass:
#     __attr = "значение"
#     def __method(self):
#         print("Это защищенный метод")
#
# mc = MyClass()
# mc.__method()
# print(mc.__attr)

#Наследование
# class Transport:
#     def transport_method(self):
#         print("Это родительский метод из класса Транспорт")
#
# class Auto(Transport):
#     def auto_method(self):
#         print("Это дочерний метод дочернего класса Авто")
#
# # Множественное наследование
# class Bus(Transport):
#     def bus_method(self):
#         print("Это дочерний метод дочернего класса Автобус")

# a = Auto()
# a.auto_method()
# b = Bus()
# b.bus_method()

class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2

class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p

class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p

r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())
