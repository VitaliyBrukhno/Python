# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def my_func (*args):
     return " ".join([*args])

user_name = input('Введите имя: ')
user_surname: str = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
current_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_telephone = input('Введите номер телефона: ')
print(my_func(user_name, user_surname, year_of_birth, current_city, user_email, user_telephone))
