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


# a function that accept class instances to use the speak method of them
# for better understanding go and search about how *args and **kwargs work
def animal_speak(*args):
    for spk in args:
        spk.speak()


# created an instance for all the classes
cow = Cow()
dog = Dog()
cat = Cat()
# put them in this function and function will call the speak method of them
animal_speak(cow, dog, cat)
