class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduction(self):
        print(f"Hi, my name is {self.firstname}")


class Student(Person):
    subject = "Biology"

    def show_profession(self):
        print(f"I study {self.subject}")


student1 = Student("Nino", "Khorguani")
student1.show_profession()
student1.introduction()
wcode backend
7:17 PM
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def introduction(self):
        print(f"Hi, my name is {self.firstname}")


class Student(Person):
    def __init__(self, firstname, lastname, subject):
        # super().__init__(firstname, lastname)
        Person.__init__(self, firstname, lastname)
        self.subject = subject


    def show_profession(self):
        print(f"I study {self.subject}")


student1