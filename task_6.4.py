# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Cars:

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print(f"Машина {self.name} поехала ")
    def stop(self):
        print(f'Машина {self.name} остановилась')
    def turn(self, direction):
        if direction == 'left':
            print(f'Машина {self.name} повернула на лево')
        else:
            print(f'Машина {self.name} повернула на право')

class TownCar(Cars):
    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Машина {self.name} едет с превышением скорости!')
        else:
            print(f'Внимание! Машина {self.name} едет с допустимой скоростью!')

class SportCar(Cars):
        pass

class WorkCar(Cars):
    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Машина {self.name} едет с превышением скорости!')
        else:
            print(f'Машина {self.name} едет с допустимой скоростью!')

class PoliceCar(Cars):
    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)

town_car = TownCar('Hundai', 70, 'Синий')
print(town_car.name, town_car.color, town_car.speed, town_car.is_police)
town_car.show_speed()
sport_car = SportCar('Maclaren', 120, 'Красный')
print(sport_car.name, sport_car.color, sport_car.speed, sport_car.is_police)
sport_car.turn('right')
work_car = WorkCar('Dacia', 40, 'Черный')
print(work_car.name, work_car.color, work_car.speed, work_car.is_police)
work_car.show_speed()
work_car.stop()
police_car = PoliceCar('Volkswagen', 90, 'Белый')
print(police_car.name, police_car.color, police_car.speed, police_car.is_police)
police_car.go()
