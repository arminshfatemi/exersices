class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def description(self):
        return f'its a {self.brand}, and its made year {self.year}'

    def getter(self):
        print(f"""
    Getter ....
    brand: {self.brand}
    year: {self.year}
        """)

    def setter(self, brand, year):
        self.brand = brand
        self.year = year
        print(f""" 
        
    Set to... 
    brand: {self.brand}
    year: {self.year}
                """)


class Car(Vehicle):
    def __init__(self, brand, year):
        Vehicle.__init__(self, brand, year)

    def description(self):
        return f'A CAR , its a {self.brand}, and its made year {self.year}'


class Motorcycle(Vehicle):
    def __init__(self, brand, year):
        Vehicle.__init__(self, brand, year)

    def description(self):
        return f'A MOTORCYCLE , its a {self.brand}, and its made year {self.year}'


vehicle = Vehicle('BMW', 1990)
print(vehicle.description())
vehicle.getter()
vehicle.setter('fiat', 1998)

car = Car('Bnz', 2020)
print(car.description())
car.getter()
car.setter('bmw', 2023)

motor = Motorcycle('Honda', 2001)
print(motor.description())
motor.getter()
motor.setter('bmw', 2023)
