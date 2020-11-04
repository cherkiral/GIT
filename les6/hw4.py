class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car started')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(f"Your current speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Attention! Your speed is more than 60")
        else:
            print(f"Your current speed is {self.speed}")

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Attention! Your speed is more than 40")
        else:
            print(f"Your current speed is {self.speed}")
a = Car(45, "green", 'lada', False)
b = WorkCar(45, "green", 'lada', False)
b.show_speed()


