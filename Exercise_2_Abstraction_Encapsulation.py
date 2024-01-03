from abc import ABC, abstractmethod


# Abstraction and Encapsulation

# ** Encapsulation **
# means some of the objects of class are not directly access able, and helps in with
# data hiding
# in overall encapsulation is for bundle data and methods that work on the data into a single a class,
# This helps in organizing and controlling access to the data.

# there are three access modifier -> Public ,Private ,Protected

# Public
# Members (attributes and methods) declared without any access modifier are considered public by default.

# Private
# Members can be marked as private by prefixing them with double underscores (__)
# Accessing private members from outside the class will result in an AttributeError.
# but there is still ways to access them but by convention this must not

# Protected
# Members can be marked as protected by prefixing them with a single underscore (_).
# They can be accessed within the class and its subclasses.
# Though protected members can be accessed from outside the class,
# it's considered good practice to treat them as if they were private.
# Python doesn't have strict access control like some other languages (e.g., Java or C++),
# and it relies on naming conventions to indicate the intended visibility of variables


# ** Abstraction **
# Abstraction involves simplifying complex systems,
# in general abstraction is achieved through the creation of abstract classes and interfaces.
# An abstract class is a class that cannot be instantiated and may have abstract methods.
# while an abstract method is a method that is declared but has no implementation in the abstract class.
# Subclasses must provide concrete implementations for these abstract methods.
# one of the advantages of using abstraction is in code organization, maintenance in big scale

# Base Class for our Abstraction
# we are going to use this abstraction class , for all the shapes
# to calculate area
class BaseClass(ABC):
    # this decorator is used for methods of abstract classes
    # so all the functions that will get inherit this class must implement and have this method
    # and if you don't have it python will raise an error
    @abstractmethod
    def area(self):
        pass

    # a getter function , if you don't know what it is you can easily go and search to learn it
    @abstractmethod
    def getter(self):
        pass

    # a setter function ,  if you don't know what it is you can easily go and search to learn it
    # a setter function with flexible arguments for child classes
    # what is *args ? -> *args is used to allow a function to accept any number of positional arguments
    @abstractmethod
    def setter(self, *args):  # I put args for childs to accept different parameter
        pass


# we inherit from our base abstraction class
class Circle(BaseClass):
    # it's not mandatory to make an init function for our BaseClass , we can just make an init method in child
    # classes and there would be no problem

    # As you can see we have created a self.__radius , this class variable is private variable
    # this means we can access this variable from outside of class
    # try to access it to see with -> print(circle.__radius)
    def __init__(self, radius: int):
        self.__radius = radius

    # area method to calculate the area of circle , as you can see we are creating function as the base class
    # have it, we must put it in our class too

    # __a is a private variable and can't get access from outside of class
    def area(self):
        # using double underscores (__) for private variables in python doesn't make them entirely inaccessible,
        # it's more about signaling that they are intended for internal use.
        __a = 3.14 * self.__radius ** 2
        print(f'area of this Circle: {__a}')

    def getter(self):
        print(f"""
        Getter ....
        radius: {self.__radius}
        """)

    def setter(self, new_radius):
        self.__radius = new_radius
        print(f"""
        Setter...
        length: {self.__radius}
        """)


class Rectangle(BaseClass):
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def area(self):
        __a = self._length * self._width
        print(f'area of this Rectangle: {__a}')

    def getter(self):
        print(f"""
        Getter...
        length: {self._length}
        width: {self._width}
        """)

    def setter(self, length, width):
        self._length = length
        self._width = width
        print(f"""
        Setter...
        length: {self._length}
        width: {self._width}
        """)


class Triangle(BaseClass):
    def __init__(self, base: int, height: int):
        self._base = base
        self._height = height

    def area(self):
        __hb = self._height * self._base
        __a = __hb / 2
        print(f'area of this Triangle: {__a}')

    def getter(self):
        print(f"""
        Getter...
        height: {self._height}
        base: {self._base}
        """)

    def setter(self, height, base):
        self._height = height
        self._base = base
        print(f"""
        Setter...
        height: {self._height}
        base: {self._base}
        """)


circle = Circle(12)
circle.area()
circle.getter()
circle.setter(new_radius=23)

rectangle = Rectangle(22, 33)
rectangle.area()

triangle = Triangle(12, 14)
triangle.area()
