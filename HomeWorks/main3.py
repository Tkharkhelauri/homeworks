# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:
# input: “word”
# Output: „Tripled: wordwordword“

# word = input("Please enter any word: ")
# def tripling():
#     print(f"Tripled: {word}{word}{word}")
#
# tripling()
# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

# def weight_on_the_moon():
#     x = int(input("PLease enter your weight in kilograms: "))
#     y = x / 6
#     print(f"Your weight on the moon is {y} kilograms")
#
#
# weight_on_the_moon()

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)


# def calculator():
#     expression = input("Please enter the math expression (number operator number): ")
#     parts = expression.split()
#
#     if len(parts) != 3:
#         raise ValueError("Invalid expression. Please enter a valid format (number operator number).")
#     try:
#         num1 = float(parts[0])
#         operator = parts[1]
#         num2 = float(parts[2])
#     except ValueError:
#         return "Use numbers only. Please avoid characters."
#
#     # define operator
#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             return "Division by zero is not allowed."
#         else:
#             result = num1 / num2
#     else:
#         return "Invalid operator. Please use +, -, *, or /"
#
#     return result
#
#
# answer = calculator()
# print(answer)


# გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური
# სიმბოლოებით დაწერილ სიტყვას, დაშიფრავს მორზეს ანბანით და დააბრუნებს შედეგს.
def encrypt_in_morse():
    sentence = input("Please enter any sentence and it will get encrypted into Morse's code: ")
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
             '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
             '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
             '-.--', '--..', ' ']
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z', ' ']
    encrypted = []

    for char in sentence.lower():
        if char in abc:
            index = abc.index(char)
            encrypted.append(morse[index])
        else:
            pass
    return encrypted


morse_sentence = encrypt_in_morse()
print(morse_sentence)
# ძალიან გაამარტივებდა აქ dictionary არა?