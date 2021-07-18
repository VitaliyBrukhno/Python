# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('task_5.4r.txt', 'r', encoding="utf-8") as read_f:
    #content = file_obj.read().split('\n')
    for i in read_f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('task_5.4w.txt', 'w', encoding="utf-8") as write_f:
    write_f.writelines(new_file)
