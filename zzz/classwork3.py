# from random import randint
#
# def guess_number(my_range):
#     num = randint(1, my_range)
#     i = 0
#     while True:
#         i += 1
#         answer = int(input(f"I have chosen one number in range 1-{my_range}. Guess Which: "))
#
#         if answer == num:
#             print(f"Correct! You needed {i} tries to guess!")
#             break
#
#         elif answer < num:
#             print("My number is greater!")
#
#         else:
#             print("My number is less!")
#
#
# guess_number(5)
#
# import math
#
# a = math.floor(2.7)
# print(a)
#
# import math
# from math import pow
#
# a = pow(3,4)
# print(a)

# def say_hi():
#     print("Hi!")
#
# # print(say_hi())
# print(say_hi)

# def say_hi():
#     return "HI"
#
# a = say_hi()
# print(a)

# def say_hi(name):
#     return f"Hi, {name}!"
#
# a = input("Enter name: ")
#
# returned_string = say_hi(a)
# print(returned_string)

# x = 100
#
# def show_x():
#     global x # ეს თუ არ დავამატეთ ლოკალურ სივრცეში გლობალზე წვლომა არ გვექნება
#     x = x + 1
#     print(x)
#
# show_x()
# print(x)

# x = 100
#
# def show_x():
#     y = 11 # enclosing variable
#     def inner():
#         n = 5
#         print(n) #print(y), print(x).
#     return inner
#
# # print(show_x()())
# show_x()()

# x = lambda a, b: a+b
# print(x(2, 3))



# სტრინგიდან სიტყვების სიაში ჩალაგება
# a = "Hi, my name is Nick"
#
# b = a.split()
# print(b)


# სტრინგიდან ყოველი ასოს სიაში ჩალაგება
a = "Hi, my name is Nick"

char_list = [char for char in a]
print(char_list)