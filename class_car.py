import random


class Car:

    def __init__(self, name: str, year: int, owner: str):
        self.owner = owner
        self.ip = random.randint(1, 1_000_000)
        self.year = year
        self.times = 0
        self.name = name

    def drive(self, length):
        self.length = length
        print(f'drive for {length} km')


class Gasoline(Car):
    def __init__(self, name: str, year: int, force, owner: str):
        super().__init__(name, year, owner)
        self.cost = 20
        self.force = force

    def refuel(self):
        self.times += 1
        print(f'refueled {self.times} times and you spend {self.cost * self.times} $')


class Electro(Car):
    def __init__(self, name: str, year: int, owner: str):
        super().__init__(name, year, owner)
        self.power = 100

    def refuel(self):
        self.times += 1
        print(f'recharged {self.times} times')

    def battery_level(self):
        self.power = self.power - self.length
        print(f'you have {self.power}%')


car_1 = Gasoline(name='BMW', year=2023, force=523, owner='Lebron James')
car_2 = Electro(name='Tesla', year=2024, owner='Daniel Brown')

'''


---------------------------------------------------------------------


'''

car_1.drive(int(input('How many km do you wanna drive ?: ')))
car_2.drive(int(input('How many km do you wanna drive ?: ')))
print('-' * 100)
car_1.refuel()
car_1.refuel()
car_1.refuel()
print('-' * 100)
car_2.refuel()
print('-' * 100)
print(car_1.year)
print(car_2.year)
print('-' * 100)
print(car_1.ip)
print(car_2.ip)
print('-' * 100)
print(car_1.force)
print('-' * 100)
print(car_1.owner)
print(car_2.owner)
print('-' * 100)
car_2.battery_level()
