#Функциональное про-е

t  = (1, 2, 3, 4, "abc")
print(8 in t)
print(8 in t)
print("key" in {"key": "value", "key_2": "value_2"})

#elif

a = 5
if a > 5:
    print("a > 5")
elif a < 5:
    print("a < 5")
else:
    print("a = 5")

#for

l = [0, 1, 2, 3, 4]
for item in l:
    print(item)


dct = {"Name": "Maxim",
       "Age": "23"}
for key in dct:
    print(key, dct[key])


for value in dct.values():
    print(value)

for key in dct.keys():
    print(key)

results = []
values = [1, 2, 3, 4, 5]
for value in values:
    results.append(value ** 2)
print(results)

#cлияние в 1 строку
string = ""
strings = ["Петров", "Иван", "Сергеевич"]
for s in strings:
    string += s
print(string)

#join
print(" ".join(strings))
list = [val ** 2 for val in values]
print(list)
set_1 = {val ** 2 for val in values}
print(set_1)
map_1 = {val: val ** 2 for val in values}
print(map_1)

values = [1, 2, 3, 4, 5]

#Генератор (можем прочитать данные только 1 раз)

gen = (val ** 2 for val in values)
print(type(gen)) # <class 'generator'>
print(next(gen))
print(next(gen))
print(list(gen))
print(list(gen))

#list comprehension
gen = [val ** 2 for val in values]

print(list(range(1, 90, 5))) # диапазон от 1 до 11

# Индексы
for i in range(len(values)):
    print(i, values[i])

a = 16
b = 42
a, b # (16, 42)


values = [1, 2, 3, 4, 5]
print(enumerate(range(10)))
e = enumerate(values)
print(list(e))

for i, val in enumerate(values, 1):
    print(i, val)

# while

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("ELSE")

for i in range(1, 5):
    print(i, end=" is ")
    if i % 2 == 0:
        print("even")
    else:
        print('odd')

# функции
def some_func(q):
    return q, "Пока"
a = some_func("Привет")
print(a)

def out_fun():
    def inner():
        return "inner text"
    return inner
print(out_fun()())

def gen():
    yield 42
g = gen()
print(next(g))

def gen_2():
    for i in range(3):
        return i
print(gen_2())

from decorator import decorator
#
# #Рекурсия
values = [1, 2, 3, 4, 5]
def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)
print(recur_fib(10))

#Лямбда функция
def exp(x):
    return lambda y: y**x

exp_2 = exp(4)
print(exp_2)

#Map

mapped = map(lambda x: x+3, values)
print(list(mapped))

# #Filter
my_nums = range(-10, 20, 3)
a = filter(lambda x: -7 < x < 10, my_nums)
print(list(a))

#reduce
from functools import reduce

to_mul = range(1, 7)
product = reduce(lambda x, y: x*y, to_mul, 10)
print(product)

# #Декоратор
def a_func():
    print("Hello from a_func!")
a_func()

def decorator(func):
    def wrapper():
        print("some text")
        func()
    return wrapper()
a_func = decorator(a_func)

@decorator
def another_func():
    print("another func")
another_func()


# 2)
def my_func(x, y=2):
    return x+y
result = my_func(5)
print(result)

def gen_dec(x):
    print("In a gen dec")
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        print("Generated a wrapper")
        return wrapper
    print("Generated a decorator")
    return decorator

@gen_dec(42)
def mul(a, b):
    return a*b

print(mul(3, 4))