# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

some_str = input('Пользователь вводит строку из нескольких слов ')
some_list = some_str.split()
num = 1
for el in range(len(some_list)):
        print(num, some_list[el][:10])
        num += 1
