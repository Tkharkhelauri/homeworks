#მემკვიდრეობითობა

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def introduction(self):
#         print(f"Hi, my name is {self.firstname}")
#
# class Georgian:
#     def __init__(self, location):
#         self.location = location
#
#     @staticmethod
#     def say_hi():
#         print("გამარჯობა!")
#
#
# class Student(Person, Georgian):
#     def __init__(self, firstname, lastname, subject, location):
#         # super().__init__(firstname, lastname)
#         Person.__init__(self, firstname, lastname)
#         Georgian.__init__(self, location)
#         self.subject = subject
#
#
#     def show_profession(self):
#         print(f"I study {self.subject}")
#
#
# student1 = Student("Nino", "Bregvadze", "Biology", "Tbilisi")
# student1.show_profession()
# student1.introduction()
# student1.say_hi()
# print(student1.location)

#შვილიშვილი კლასი
# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def introduction(self):
#         print(f"Hi, my name is {self.firstname}")
#
# class Georgian(Person):
#     def __init__(self, location, firstname, lastname):
#         super().__init__(firstname, lastname)
#         self.location = location
#
#     @staticmethod
#     def say_hi():
#         print("გამარჯობა!")
#
#
# class Student(Georgian):
#     def __init__(self, firstname, lastname, subject, location):
#         super().__init__(location, firstname, lastname)
#         self.subject = subject
#
#
#     def show_profession(self):
#         print(f"I study {self.subject}")
#
#
# student1 = Student("Nino", "Bregvadze", "Biology", "Tbilisi")
# student1.show_profession()
# student1.introduction()
# student1.say_hi()
# print(student1.location)


#პოლიმორფიზმი

# class Base:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("General Movement...")
#
# class Car(Base):
#     def move(self): - # თუ შვილობილი კლასის მეთოდს იგივე სახელი ერქმევა, რაც მშობლის მეთოდს,
# #ზემოდან გადააწერს მოქმედებას
#         print("Drive")
#
#
# class Boat(Base):
#     def move(self):
#         print("Sail")
#
#
# class Plane(Base):
#     def move(self):
#         print("Fly")
#
#
# car = Car("BMW", "x5")
# boat = Boat("Yacht", "7343")
# plane = Plane("Boing", "Ah15")
#
# car.move()
# boat.move()
# plane.move()


#ინკაფსულაცია  public, protected, private

class Colors:
    def __init__(self):
        self.__color1 = "Green" # - private
        self._color2 = "Red" # - protected
        self.color3 = "Blue" # - public

    def __say_something1(self):
        print("Something1")

    def _say_something2(self):
        print("Something2")

    def say_something3(self):
        print("Something3")


color = Colors()
# print(color.__color1)
print(color._color2)
print(color.color3)

color.say_something3()
color._say_something2()
color.__say_something1()


#
#
# #აბსტრაქტული კლასები
# from abc import ABC, abstractmethod
#
# class Polygon(ABC):
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @staticmethod
#     def introduction():
#         print("I am geometric figure!")
#
#
#
# class Triangle(Polygon):
#
#     def perimeter(self):
#         print("Calculate Triangle Perimeter: a+b+c")
#
#     def area(self):
#         print("Calculate Triangle Area: h*a/2")
#
#
# class Rectangle(Polygon):
#
#     def perimeter(self):
#         print("Calculate Rectangle Perimeter: 2*(a+b)")
#
#     def area(self):
#         print("Calculate Rectangle Area: a*b")
#
#
# class Circle(Polygon):
#
#     def perimeter(self):
#         print("Calculate Circle Perimeter: 2*pi*r")
#
#     def area(self):
#         print("Calculate Circle Area: p*r**2")
#
#
#
#
#
# triangle = Triangle()
# triangle.perimeter()
# triangle.area()
# triangle.introduction()
#
# rect = Rectangle()
# rect.perimeter()
# rect.area()
# rect.introduction()
#
# circle = Circle()
# circle.perimeter()
# circle.area()
# circle.introduction()