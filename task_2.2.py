# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

user_list = []
el_count = int(input('Введите количество элементов списка: '))
i = 0
el = 0
while i < el_count:
    user_list.append(input("Введите элемент списка: "))
    i += 1

for elem in range(int(len(user_list))):
        user_list[el], user_list[el + 1] = user_list [el + 1], user_list[el]
        el += 2
        if el_count % 2 == 1 and  el + 1 == el_count:
            break
print(user_list)
