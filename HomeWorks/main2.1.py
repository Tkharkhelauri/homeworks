# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი
# იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს
# დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი.
# შეცდომის შემთხვევაში იბეჭდება:
# „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება:
# „სწორია!“
#

# x = input(f"რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც? "
#           f"\n სავარაუდო პასუხები: \n 1. შუმერთა \n 2. სელჩუკთა \n 3. რომის \n 4. მონღოლთა \n თქვენი პასუხი:  ")
# if x == "3" or x == "რომის":
#     print("სწორია!")
# else:
#     print("არა! სწორი პასუხია რომის!")
#


# 2. გამრავლების ტაბულა
# ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან
# მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.
#

num = int(input("Please enter a number:  "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        product = i * j
        print(f" {i:2} * {j:2} = {product:4}", end=" ")

    print(" .")

# 3. თუთიყუშის პროგრამა
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ
# შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”
#
#
# while True:
#     say = input("say: ")
#     print(f"User Said Whaaat!? \n User Said '{say}'")
#     if say == "quit":
#         break