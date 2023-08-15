from abc import ABC, abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def getter(self):
        pass

    @abstractmethod
    def setter(self, *args):  # I put args for childs to accept different parameter
        pass


class Circle(BaseClass):
    def __init__(self, radius: int):
        self._radius = radius

    def area(self):
        __a = 3.14 * self._radius ** 2
        print(f'area of this Circle: {__a}')

    def getter(self):
        print(f"""
        Getter ....
        radius: {self._radius}
        """)

    def setter(self, new_radius):
        self._radius = new_radius
        print(f"""
        Setter...
        length: {self._radius}
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
