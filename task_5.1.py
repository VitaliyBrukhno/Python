# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

f_obj = open("task_5.1.txt", 'w')
line = input('Введите текст: ')

while line != '':
    f_obj.writelines(line + '\n')
    line = input('Введите текст: ')

f_obj.close()
f_obj = open("task_5.1.txt", 'r')
some_string = f_obj.read()
print(some_string)
f_obj.close()
