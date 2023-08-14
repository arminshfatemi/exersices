class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        self.student_id = student_id
        Person.__init__(self, name, age)

    def get_all_info(self):
        print(f"""
        student name: {self.name}
        student age:{self.age}
        student id: {self.student_id}
        """)

    def name_age_change(self, name: str, age: int, student_id: int):
        self.name = name
        self.age = age
        self.student_id = student_id
        print(f"""
        student name: {self.name}
        student age:{self.age}
        student id: {self.student_id}
        """)


student1 = Student('armin', 22, 2123)
student1.get_all_info()
print('------------------')
student1.name_age_change('vargha', 22, 12334)
