# # Get all numbers as a comma-separated string
# numbers_str = input("Enter 5 numbers separated by commas (e.g., 1, 2, 3, 4, 5): ")
#
# # Split the string into a list of numbers (converting to integers)
# try:
#   numbers = [int(num) for num in numbers_str.split(",")]
#   if len(numbers) != 5:
#     raise ValueError("Please enter exactly 5 numbers.")
# except ValueError:
#   print(f"Invalid input. Please enter only numbers.")
#   exit()  # Exit the program if there's an error
#
# # Now you have the numbers in separate variables
# number1 = numbers[0]
# number2 = numbers[1]
# number3 = numbers[2]
# number4 = numbers[3]
# number5 = numbers[4]
# t = number1 + number2 + number3 + number4 + number5
# sd = t / 5
# print(sd)
#
#
#
# num_entries = 5
# numbers = []
# count = 0
# user_input
# number = float(user_input)
#  COUNT INCREASES
# while count < num_entries:
#     user_input = input(f"Enter number {count + 1}: ")  # Prompt with entry number
#     while True:  # Nested loop for validation
#         try:
#             number = float(user_input)  # Attempt conversion
#             numbers.append(number)  # Add to list if valid
#             count += 1  # Increment counter
#             break  # Exit nested loop if successful
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             user_input = input("Try again: ")  # Get new input if invalid
#
# sum = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# answer = sum / num_entries
# print(f"{answer}")


# rows = 5  # Number of rows (adjust for desired height)

# for i in range(1, rows + 1):  # Outer loop for rows (1 to rows)
#   for j in range(1, i + 1):  # Inner loop for stars (1 to current row number)
#     print("*", end="")  # Print a star without a newline
#   print()  # Print a newline after each row
#
# for i in range(rows - 1, 0, -1):  # Outer loop for decreasing rows (rows-1 down to 1)
#   for j in range(1, i + 1):  # Inner loop for decreasing stars (1 to current row number)
#     print("*", end="")  # Print a star without a newline
#   print()  # Print a newline after each row


# number_of_rows = 5  #სიმაღლე
#
# # ზრდადი ფიფქები
# for current_row in range(1, number_of_rows + 1): #1დან 5ის ჩათვლით
#   for number_of_stars in range(1, current_row + 1): #რეინჯი იცვლება იტერაციაში და ჯერ ერთხელ ბეჭდავს ფიფქს, და შიდა end მერე გარე end, მერე ორჯერ ბეჭდავს ფიფქს გარე endამდე
#     print("*", end="")  # ანუ შიდა loopში ახალი ხაზის გარეშე ბეჭდავს ფიფქებს
#   print()  # ახალი ხაზი, როცა გარე for ეშვება
#
# # კლებადი ფიფქები
# for current_row in range(number_of_rows - 1, 0, -1): #უკუსვლა, ჯერ 4ჯერ სრულდება, მერე 3ჯერ და ა.შ
#   for number_of_stars in range(1, current_row + 1):
#     print("*", end="")  # ახალი ხაზის გარეშე
#   print()  # ახალი ხაზით

