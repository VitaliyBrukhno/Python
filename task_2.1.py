# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_list = [True, 36, None, 17.18, 'Sam']
for el in range(len(some_list)):
    print(type(some_list[el]))
