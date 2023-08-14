class Animal:

    def speak(self):
        print('animals speak in different ways')


class Cat(Animal):
    def speak(self):
        print('- cat says Meow')


class Dog(Animal):
    def speak(self):
        print('- dog says Bark')


class Cow(Animal):
    def speak(self):
        print('- cow says Moo')


def animal_speak(*args):
    class_list = [*args]
    for spk in class_list:
        spk.speak()


cow = Cow()
dog = Dog()
cat = Cat()
animal_speak(cow, dog, cat)
