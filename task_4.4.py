# Представлен список чисел. Определить элементы списка,
# не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

from random import randint
some_vars = [randint(0, 30) for i in range(15)]
print(f'Исходный список: {some_vars}\nСписок без повторений: {[el for el in some_vars if some_vars.count(el) == 1]}')
