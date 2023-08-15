class Person:
    def __init__(self, __name, __age):
        self._name = __name
        self._age = __age


class Student(Person):
    def __init__(self, __name: str, __age: int, __student_id: int):
        self.__student_id = __student_id
        Person.__init__(self, __name, __age)

    def get_all_info(self):
        print(f"""
        student name: {self._name}
        student age:{self._age}
        student id: {self.__student_id}
        """)

    def name_age_change(self, name: str, age: int, __student_id: int):
        self._name = name
        self._age = age
        self.__student_id = __student_id
        print(f"""
        student name: {self._name}
        student age:{self._age}
        student id: {self.__student_id}
        """)


student1 = Student('armin', 22, 2123)
student1.get_all_info()
print('------------------')
student1.name_age_change('vargha', 22, 12334)
