# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите продолжительность времени в секундах: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
if seconds < 10:
    seconds = '0' + str(seconds)
    hours = '0' + str(hours)
    minutes = '0' + str(minutes)
elif minutes < 10:
        hours = '0' + str(hours)
        minutes =  '0' + str(minutes)
else:
    hours = '0' + str(hours)
print("Время в формате чч:мм:сс   {}:{}:{}" .format(hours, minutes, seconds))
