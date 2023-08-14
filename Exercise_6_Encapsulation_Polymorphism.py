class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Manager(Employee):
    def __init__(self, name, __salary, role):
        self.__salary = __salary
        Employee.__init__(self, name, role)

    def get_bones(self):
        self.__salary += 1000
        print(f'salary of ({self.name}) as a ({self.role}) now is ({self.__salary})')


class Developer(Employee):
    def __init__(self, name, __salary, role):
        self.__salary = __salary
        Employee.__init__(self, name, role)

    def get_bones(self):
        self.__salary += 500
        print(f'salary of ({self.name}) as a ({self.role}) now is ({self.__salary})')


manager = Manager('armin', 1000, 'back-end')
manager.get_bones()


dev = Developer('reza', 500, 'Intern')
dev.get_bones()
