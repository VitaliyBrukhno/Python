# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число n: "))
str_n = str(n)
num_nn = str_n + str_n
num_nnn = str_n + str_n + str_n
sum = n + int(num_nn) + int(num_nnn)
print("Сумма чисел n + nn + nnn = ", sum)
