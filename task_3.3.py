# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    if num1 > num2 and num3 > num2:
        result = num1 + num3
        return result
    elif num1 < num2 and num1 < num3:
        result = num2 + num3
        return result
    else:
        result = num1 + num2
        return result

first_arg = int(input("Введите первый аргумент: "))
second_arg = int(input("Введите второй аргумент: "))
third_arg = int(input("Введите третий аргумент: "))
print(f'Сумма наибольших двух аргументов: {my_func(first_arg, second_arg, third_arg)}')
