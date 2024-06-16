# Class: A blueprint that defines the properties (data) and behaviors (functions) of objects.
# Imagine a class like a cookie cutter – it defines the shape of cookies you can create.
#
# Object (Instance): An individual creation based on a class. It's like a single cookie made from
# the cookie cutter. Each object has its own set of properties and can perform the behaviors defined
# in the class.
#
# Variable: A named storage location within a class or object that holds data of a specific type.
# It's like a label on a container holding ingredients for the cookie (e.g., sugar, flour).
# Data types define what kind of information the variable can store (e.g., numbers, text).
#
# Data Types:  These specify the kind of data a variable can hold. Common data types include:
#
# Numbers: Integers (whole numbers) like 10, -5 or floating-point numbers (decimals) like 3.14.
# Text: Strings of characters like "Hello" or "This is a sentence".
# Booleans: True or False values to represent logical conditions.
# Lists: Ordered collections of items, like [1, 2, "apple"].
# Dictionaries: Unordered collections of key-value pairs, like {"name": "Alice", "age": 30}.
# Method: A function defined within a class that describes an action the object can perform.
# It can access and potentially modify the object's variables. Think of methods as the instructions
# for making the cookie – they involve mixing ingredients, baking, etc. Methods often take input
# through parameters.
#
# Parameter: A named variable used within a method's definition to receive data when the
# method is called. Imagine parameters as the specific ingredients (amounts) needed for a
# single cookie batch within the method (instruction).
#
# Property: A special method that controls how an object's variable (data) can be accessed
# and potentially modified. It can act like a gatekeeper, ensuring data is retrieved or
# changed in a controlled way. Properties are often created using decorators or getter/setter methods.
#
# Relationship Summary:
#
# Class: Defines the structure (variables, methods) for objects.
# Object (Instance): An individual creation based on the class, holding its own variables
#       and using methods.
# Variable: Stores data within a class or object, with a specific data type.
# Method: A function within a class that performs actions on the object's data (variables).
# Parameter: Input data received by a method when it's called.
# Property: Controls access and modification of an object's data.
# These elements work together to create powerful and reusable code. A class defines the general concept, while objects are the specific instances with their own data and behaviors.

class Human:
    height = 170
    weight = 60

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @staticmethod
    def sleeping():
        print("ZZzzZZZZzzzzzzzzzzzz...")

    @classmethod
    def show_height(cls):
        print(f"Human Height is: {cls.height}")

    def say_hi(self):
        print(f"Hi, my name is {self.name}")

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


human1 = Human("Nika", 19)
human2 = Human("Levani", 15)

# print(human1)
# print(human2)

# human1.name = "Nika"
# human2.name = "Elene"
# human1.say_hi()
# human2.say_hi()



# human1.show_height()
# human2.show_height()
# print(human1.name)
# print(human2.name)

# Human.show_height()


# Human.hands_number = 2
#
# print(Human.hands_number)
#
Human.sleeping()