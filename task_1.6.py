# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Пройденное растояние в первый день в км : '))
b = int(input('Растояние которое нужно пройти в км : '))
day = 1
result = a
while result < b:
    print(f'{day}-й день: {result:.2f} км')
    result = result * 1.1
    day += 1
print(f'на {day} день спортсмен достиг результата {result:.2f} — не менее {b}  км')
