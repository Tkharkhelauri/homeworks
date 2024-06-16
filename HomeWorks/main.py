# თამარ ხარხელაური

# 1. დაწერე პროგრამა რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის მიღების
# შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით.

# George Abramia

# name = input("Please enter your preferred name: ")
# lastname = input("Please enter your family name: ")
#
# print(name, lastname)
# print("This is your full name: ", name, lastname) - it's just prettier :D
# 2. დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის ხარისხში
# და შედეგი იბეჭდება ტერმინალში.

# num1 = int(input("Please enter any number: "))
# num2 = int(input("Please enter some number once again: "))
#
# print(num1 ** num2)

# 3. დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს
# ინფორმაციას შემდეგი სახით:
# Name: Lia
# Surname: Kebadze
# Age: 20
# City: Tbilisi

# name = input("Please enter your preferred name: ")
# lastname = input("Please enter your family name: ")
# age = (input("Please enter your age: "))
# city = input("Please enter the name of the city where you live currently: ")
#
# print("Name: "+name, "Surname: "+lastname, "Age: "+age, "City: "+city, sep="\n")

# 4. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
# დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:
# Apple//Peach%%Orange

# fruit1 = input("Please enter any fruit name: ")
# fruit2 = input("Please enter any fruit name again: ")
# fruit3 = input("Please enter another fruit name: ")
#
# print(fruit1+"//"+fruit2+"%%"+fruit3)

# 5. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული
# სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:
# Number of symbols: 50

# text = input("Please enter any text and I will count the characters in it: ")
#
# print("Number of symbols: ", len(text))