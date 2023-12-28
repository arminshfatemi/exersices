# Two important things before reading the code .
# 1. make sure you know what is class and functions
# 2. make sure you give a star to repo -_-


# inheritance and polymorphism :

# Inheritance : we have face , body and ... of our father and mother means we inherit it from them
# this is in codes too,  a class can have a child with exact functions like its self

# polymorphism : means like functions that have same name but do it in different way
# in our examples we have a function called description , all three example have it but
# there is a little difference (i have good example for this concept in exercise 3)


class Vehicle:
    # __int__ will execute when a new instance of the class is created.
    # for creating a new instance with this class we need to give the instance 2 variable
    # 1. brand that is string variable , means it prefer to accept string
    # 2. year and that is an integer variable , means it prefer to accept integer
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    # A class method we are using self.brand amd self.year means
    # when an instance is created and two variable is passed to new instance it will use them
    def description(self):
        return f'its a {self.brand}, and its made year {self.year}'

    # getter methods in classes are methods that allow you to access or get the value of class instance
    # for our example we are just printing the variables
    # normally getter methods will return a variable or more of class instance
    def getter(self):
        print(f"""
    Getter ....
    brand: {self.brand}
    year: {self.year}
        """)

    # setter method in classes are methods that allow you to change a variable of the class instance
    # so without changing directly you can change the variable of the class instance in methods
    def setter(self, brand, year):
        self.brand = brand
        self.year = year
        print(f""" 
    Set to... 
    brand: {self.brand}
    year: {self.year}
                """)


# this class is inherited from Vehicle class
# and have method that Vehicle has like __init__ , getter and setter
class Car(Vehicle):

    def description(self):
        return f'A CAR , its a {self.brand}, and its made year {self.year}'


class Motorcycle(Vehicle):

    def description(self):
        return f'A MOTORCYCLE , its a {self.brand}, and its made year {self.year}'


# we created a Vehicle class instance .
# as you can see because we have put two input variable for __init__ method we now must pass these
vehicle = Vehicle('BMW', 1990)
print(vehicle.description())
vehicle.getter()
vehicle.setter('fiat', 1998)

car = Car('Benz', 2020)
print(car.description())
car.getter()
car.setter('bmw', 2023)

motor = Motorcycle('Honda', 2001)
print(motor.description())
motor.getter()
motor.setter('bmw', 2023)
