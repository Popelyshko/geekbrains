class Car:
    speed: int
    color: str
    name: str
    is_police: str
    speed_limit: int

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print (f'{self.name} поехала')

    def stop(self):
        print (f'{self.name} остановилась')

    def turn(self, direction):
        print (f'{self.name} повернула {direction}')

    def show_speed(self):
        print (f'Текущая скорость равна {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print (f'Текущая скорость равна {self.speed}')
        if self.speed > 40:
            print (f'Внимание, привышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость равна {self.speed}')
        if self.speed > 60:
            print(f'Внимание, привышение скорости!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car = WorkCar(70, 'Red', 'BMW', False)
car.show_speed()

car2 = SportCar(70, 'Green', 'Жигули', False)
car2.turn("left")
car2.stop()
