class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def setter(self, new_name, new_role, new_salary):
        self.name = new_name
        self.role = new_role

    def getter(self):
        print(f"""
        name: {self.name}
        role: {self.role}
        """)


class Manager(Employee):
    def __init__(self, name, __salary, role):
        self.__salary = __salary
        Employee.__init__(self, name, role)

    def get_bones(self):
        self.__salary += 1000
        print(f'salary of ({self.name}) as a ({self.role}) now is ({self.__salary})')

    def getter(self):
        print(f"""
        name: {self.name}
        role: {self.role}
        salary: {self.__salary}
        """)

    def setter(self, new_name, new_role, new_salary):
        self.name = new_name
        self.role = new_role
        self.__salary = new_salary
        print(f"""
        setter... 
        name: {self.name}
        role: {self.role}
        salary: {self.__salary}
        """)



class Developer(Employee):
    def __init__(self, name, __salary, role):
        self.__salary = __salary
        Employee.__init__(self, name, role)

    def get_bones(self):
        self.__salary += 500
        print(f'salary of ({self.name}) as a ({self.role}) now is ({self.__salary})')

    def getter(self):
        print(f"""
        name: {self.name}
        role: {self.role}
        salary: {self.__salary}
        """)

    def setter(self, new_name, new_role, new_salary):
        self.name = new_name
        self.role = new_role
        self.__salary = new_salary
        print(f"""
        setter... 
        name: {self.name}
        role: {self.role}
        salary: {self.__salary}
        """)


manager = Manager('armin', 1000, 'back-end')
manager.get_bones()
manager.getter()


dev = Developer('reza', 500, 'Intern')
dev.get_bones()
