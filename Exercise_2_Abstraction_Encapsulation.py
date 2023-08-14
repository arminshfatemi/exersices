from abc import ABC, abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(BaseClass):
    def __init__(self, radius: int):
        self._radius = radius

    def area(self):
        __a = 3.14 * self._radius ** 2
        print(f'area of this Circle: {__a}')


class Rectangle(BaseClass):
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def area(self):
        __a = self._length * self._width
        print(f'area of this Rectangle: {__a}')


class Triangle(BaseClass):
    def __init__(self, base: int, height: int):
        self._base = base
        self._height = height

    def area(self):
        __hb = self._height * self._base
        __a = __hb / 2
        print(f'area of this Triangle: {__a}')


circle = Circle(12)
circle.area()


rectangle = Rectangle(22,33)
rectangle.area()


triangle = Triangle(12, 14)
triangle.area()
