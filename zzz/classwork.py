# IF CONDITIONS

# name = input("Please enter your name: ").lower()
#
# if name == "bond" or name == "Bond":
#     print("Welcome on board 007")
#
# else:
#     print(f"Good Morning {name}!")


# ITERATION : WHILE AND FOR
# WHILE:

# i = 1
# while i <= 10:
#     print(i)
#     i = i+1
#     # i += 1
# print("Finished!")

# WHILE - - BREAK - go outside of while loop
# i = 1
# while i <= 10:
#     print(i)
#     if i == 7:
#         break
#     i = i+1
#     # i += 1
#
# print("Finished!")
# i = 1
# while i <= 10:
#     print(i)
#     i = i+1
#     # i += 1
#     if i == 7:
#         break
# print("Finished!")

# WHILE - - CONTINUE - skip next step
# i = 1
# while i <= 10:
#     i = i+1
#     # i += 1
#     if i == 7:
#         continue
#     print(i)
#
# print("Finished!")

#  FOR :

# a = "How are you?"
# for i in a:
#     print(i)

# a = "How are you?"
# for i in a:
#     if i != " ":
#         print(i)

# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 101, 2):
#     print(i)

# for i in range(100, 11, -1):
#     print(i)

# a = "Hallucination"
# print(a[:5])
# print(a[3:7])
# print(a[:20:2])
# print(a[0], a[4], a[9], sep="")

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} =", i * j)
#     print()


# a = int(input("enter number: "))
# b = int(input("enter another number: "))
#
# if a < b:
#     print(a)
# else:
#     print(b)

# სამი რიცხვიდან უდიდესი
# a = int(input("enter some number: "))
# b = int(input("enter another number: "))
# c = int(input("enter one more number: "))
#
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)


# a = int(input("enter number: "))
# b = int(input("enter another number: "))
#
# if a % 6 == 0:
#     print()
#

# i = 0
# x = []
# while i < 5:
#
#     y = input("Please enter the number: ")
#     i += 1
#     x.append(y)
# x[0], x[-1] = x[-1], x[0]
# print(x)

x = {1, 2, 3, "a"}


x.add(555)

# x.pop()

print(x)
