#  გამრავლების ტაბულა ცხრილში - ვისწავლე გათანაბრება ({product:3})-----------------------------------------------

# for i in range(1, 11):
#     for j in range(1, 11):
#         product = i * j
#         # დაფორმატებულია თანაბარი დაშორებისთვის
#
#         print(f" . {product:3}", end=" ")
#     print(" .")

# N5 -- დადებითია თუ უარყოფითი? ------------------------------------------------------

# a = int(input("შეიყვანე ნებისმიერი რიცხვი:  "))
# if a > 0:
#     print(f"{a} დადებითი რიცხვია.")
# elif a < 0:
#     print(f"{a} უარყოფითი რიცხვია.")
# else:
#     print(f"{a} არც დადებითია, არც უარყოფითი")

# N6 -- არის თუ არა 2-ის და 3-ის ჯერადი? ------------------------------------------------------

# a = int(input("Please enter any whole number: "))
# if a % 6 == 0:
#     print(f"{a} იყოფა 2-ზეც და 3-ზეც.")
# else:
#     print(f"{a} არ არის 2-ის და 3-ის ჯერადი.")

# N7 --Is it even? ------------------------------------------------------------------------

# a = int(input("შეიყვანე რაიმე მთელი რიცხვი: "))
# if a % 2 == 0 and a != 0:
#     print(f"{a} ლუწი რიცხვია.")
# elif a == 0:
#     print(f"{a} არც ლუწია, არც კენტი")
# else:
#     print(f"{a} კენტი რიცხვია.")


# N8 -- Check the grade --------------------------------------------------------------------

# while True:
#     a = int(input("Please input a grade from 1 to 100: "))
#     if a in range(1, 101):
#         break
#     else:
#         print("Not valid! ")
# if a > 90:
#     print("Grade: A")
# elif 80 < a <= 90:
#     print("Grade: B")
# elif 60 < a <= 80:
#     print("Grade: C")
# else:
#     print("Grade: D")

# N9 -- Registration -------მინდოდა while-ით გამეკეთებინა----------------------------------------------------------------
# is_logged_in = False
# while True:
#     user = input("Please enter a username to register on site: ")
#     while True:
#         password = input("Please choose password which contains at least 8 characters: ")
#         if len(password) >= 8:
#             break
#         else:
#             print("Password should be at least 8 characters long!")
#     print("Registration successful!")
#     break
#
# while not is_logged_in:
#     user1 = input("Please enter a username to sign in: ")
#     password1 = input("Please enter your password: ")
#
#     if user == user1 and password == password1:
#         print(f"You have signed in as '{user}'")
#         is_logged_in = True
#     else:
#         print("Invalid username or password")
#
# print("Welcome! You're now logged in.")

# N10 -- Days of the week ------------------------------------------------------------------------

# while True:
#     x = int(input("Please input the natural number between 1 and 7:  "))
#     if 1 <= x <= 7 and x % 1 == 0:
#         break
#     else:
#         print("Please enter the valid number!")
# if x == 1:
#     print("It's a Monday!")
# elif x == 2:
#     print("It's a Tuesday")
# elif x == 3:
#     print("It's a Wednesday")
# elif x == 4:
#     print("It's a Thursday")
# elif x == 5:
#     print("It's a Friday")
# elif x == 6:
#     print("It's a Saturday")
# elif x == 7:
#     print("It's a Sunday")

# N11 -- სამნიშნაა თუ არა--------------------------------------------------------------------------------

# num =  int(input("Please enter the number:  "))
#
# if len(str(num)) == 3:
#     print("ეს რიცხვი სამნიშნაა.")
# else:
#     print("ეს რიცხვი არაა სამნიშნა")

#  N12 -- ანტიდოტი --------------------------------------------------------------------------------

# population = int(input("Please enter the number of people: "))
# vaccine = int(input("Please enter the number of antidote: "))
#
# division = vaccine / population
# add_antidotes = population * 2 - vaccine
# if division < 2:
#     print(f"We need {add_antidotes} more antidotes")
# else:
#     give_antidotes = add_antidotes * -1
#     print(f"We can give {give_antidotes} units to our partners. ")

#  N13 -- Playing accountant --------------------------------------------------------------------------------

# salary = int(input("Please enter your yearly Gross salary: "))
# years = int(input("Please enter how many years you have worked: "))
#
# taxes = salary / 100 * 26 * years
# pure_income = salary * years - taxes
# print(f"You have paid ${taxes} in taxes and earned ${pure_income} during those {years} years. ")

# N14 --  Plane in Trouble ------------------------------------------------------------------------

# s = int(input("number: "))
# if s >= 600:
#     print("Zaragoza (50km)")
# if s >= 900:
#     print("Valencia (75km)")
# if s >= 1200:
#     print("Madrid (100km)")
# elif s < 600:
#     print("Emergency landing!")

#  N2 -- ყველა რიცხვი 1დან 10მდე გარდა 3-ისა და 5-ისა ------------------------------------------------------------------

# for num in range(1, 11):
#     if num != 3 and num != 5:
#         print(num)


# N3 -- საშუალო არითმეტიკული --  აქ ვისწავლე  try ბლოკი
# -----------------------------------------------------------------------------------------------------
# numbers_str = input("Enter 5 numbers separated by commas (e.g., 1, 2, 3, 4, 5): ")
#
# try:
#     numbers = [int(num) for num in numbers_str.split(",")]
#     if len(numbers) != 5:
#         raise ValueError("Please enter exactly 5 numbers.")
# except ValueError:
#     print(f"Invalid input. Please enter numbers separated by commas.")
#     exit()
#
# num1 = numbers[0]
# num2 = numbers[1]
# num3 = numbers[2]
# num4 = numbers[3]
# num5 = numbers[4]
#
# sum = num1 + num2 + num3 + num4 + num5
# average = sum / 5
# print(f"{average}")


#  N3 -- საშუალო არითმეტიკული while loop-ით-------ვისწავლე როგორ დავამატო რიცხვი Array-ში (append)-----------------------------------------------------------------

# num_entries = 5
# numbers = []
# count = 0
#
# while count < num_entries:
#     user_input = input(f"Enter number {count + 1}: ")  # Prompt with entry number
#     while True:  # validation
#         try:
#             number = float(user_input)  # converting
#             numbers.append(number)  # adds num to list if converted
#             count += 1  # counts which number should be entered
#             break
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             user_input = input("Try again: ")  # Get new input if invalid
# sum = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# answer = sum / num_entries
# print(f"{answer}")

# N4 -- ყველა ლუწი რიცხვის ჯამი - ვისწავლე sum და for-ის გამოყენება array-ში--------
#
# ran = int(input("Please enter the number: "))
# # for num in range(0, ran):
# even_array = [num for num in range(0, ran) if num % 2 == 0]
# print(f"{sum(even_array)}")


# N5 -- I WILL ANNOY YOU UNTIL THE "END"--------------------------------------------------------
# while True:
#     name = input("What is your name? ").lower()
#     if name == "end":
#         break


#  N6 ყველა რიცხვის ჯამი------------------------------------------------------------------------
# ran = int(input("Please enter the number: "))
# arr = [num for num in range(0, ran)]
# print(f"{sum(arr)}")
#


# N7 -- snowflakes
# number_of_rows = 5 #სიმაღლე
#
# # ზრდადი ფიფქები
# for current_row in range (1, number_of_rows + 1):  #1დან 5ის ჩათვლით
#     for number_of_snowflakes in range (1, current_row + 1):#რეინჯი იცვლება იტერაციაში და
#         # ჯერ ერთხელ ბეჭდავს ფიფქს, და შიდა end მერე გარე end,
#         # მერე ორჯერ ბეჭდავს ფიფქს გარე endამდე
#         print("*", end="") # ანუ შიდა loopში ახალი ხაზის გარეშე ბეჭდავს ფიფქებს
#     print("")  # ახალი ხაზი, როცა გარე for ეშვება
#
# # კლებადი ფიფქები
# for current_row in range (number_of_rows - 1, 0, -1):  #უკუსვლა, ჯერ 4ჯერ სრულდება, მერე 3ჯერ და ა.შ
#     for number_of_snowflakes in range (1, current_row + 1): # იგივე
#         print("*", end="") # ახალი ხაზის გარეშე
#     print("")  # ახალი ხაზით
#
#
# N8 -- Same with the number.

# number = 5
#
# for i in range(1, number +1):
#     for p in range(1, i + 1):
#         print(f"{p}", end="")
#     print()

