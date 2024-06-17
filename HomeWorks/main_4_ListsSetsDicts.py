# LIST - [] - can access member by index. can be modified
# SET - {} - duplicates ignored, no indexing. can add member and search for member.
# TUPLE - () - can't be charged, indexing.
# DICTIONARY - {} - Key: Value - access value by key. dict[key]0

# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად:
# Name: Elene
# Lastname: Khardava
# Age: 21

# i = 0
# consumer_info = []
# while i < 3:
#     name = input("Enter your name: ")
#     lastname = input("Enter your lastname: ")
#     age = int(input("enter your age: "))
#     i += 1
#     person = [name, lastname, age]
#     consumer_info.append(person)
#     # print(person, consumer_info)
#
# x = int(input("Enter your index to get an info (from 1 to 3): "))
#
# print(f"""Name : {consumer_info[x-1][0]}
# Lastname : {consumer_info[x-1][1]}
# Age : {consumer_info[x-1][2]}""")


# 2. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახულიცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდე მის შესახებ
# არსებული ინფორმაცია რეზიუმეს სახით.
#
#
# celebrities = [
#     {
#         "name": "Tom",
#         "surname": "Hanks",
#         "age": 67,
#         "popular_movies": ["Forrest Gump", "Cast Away", "Saving Private Ryan"]
#     },
#     {
#         "name": "Meryl",
#         "surname": "Streep",
#         "age": 74,
#         "popular_movies": ["The Devil Wears Prada", "Kramer vs. Kramer", "Sophie's Choice"]
#     },
#     {
#         "name": "Leonardo",
#         "surname": "DiCaprio",
#         "age": 49,
#         "popular_movies": ["Titanic", "Inception", "The Revenant"]
#     },
#     {
#         "name": "Scarlett",
#         "surname": "Johansson",
#         "age": 39,
#         "popular_movies": ["Black Widow", "Lost in Translation", "Lucy"]
#     },
#     {
#         "name": "Denzel",
#         "surname": "Washington",
#         "age": 69,
#         "popular_movies": ["Training Day", "Glory", "Fences"]
#     },
#     {
#         "name": "Ryan",
#         "surname": "Reynolds",
#         "age": 47,
#         "popular_movies": ["Deadpool", "The Adam Project", "Free Guy"]
#     },
#     {
#         "name": "Scarlett",
#         "surname": "Johansson",
#         "age": 39,
#         "popular_movies": ["Black Widow", "Lost in Translation", "Lucy"]
#     },
#     {
#         "name": "Leonardo",
#         "surname": "DiCaprio",
#         "age": 49,
#         "popular_movies": ["Titanic", "Inception", "The Revenant"]
#     },
#     {
#         "name": "Brad",
#         "surname": "Pitt",
#         "age": 60,
#         "popular_movies": ["Fight Club", "Once Upon a Time in Hollywood", "12 Monkeys"]
#     },
#     {
#         "name": "Sandra",
#         "surname": "Bullock",
#         "age": 59,
#         "popular_movies": ["The Blind Side", "Gravity", "Miss Congeniality"]
#     },
#     {
#         "name": "Jennifer",
#         "surname": "Lawrence",
#         "age": 33,
#         "popular_movies": ["The Hunger Games series", "Silver Linings Playbook", "American Hustle"]
#     },
#     {
#         "name": "Emma",
#         "surname": "Watson",
#         "age": 33,
#         "popular_movies": ["Harry Potter series", "Beauty and the Beast", "Little Women"]
#     }
# ]
#
# found = False  # tracking if a name is in the list
#
# i = input("Enter actor's name or lastname: ").capitalize()
# for celebrity in celebrities:
#     if celebrity["name"] == i or celebrity["surname"] == i:
#         found = True  # name is in the list
#         # Printing data
#         for key, value in celebrity.items(): #HARDLY FOUND "ITEMS" TO MAKE OUTCOME PRETTY! :D
#             print(f"{key}: {value}")
#         break  # exit "for"
#
# if not found:
#     print("Celebrity not found in this list!")


# 3. შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

# # N1
# def unique_list():
#     list1 = list(input("Enter comma-separated items for the list: ").split(","))
#     # print(list1)
#     _set_from_list = set(list1)
#     list2 = list(_set_from_list)
#     print(list2)
#     return list2
#
# unique_list()
#
# # N2
#
# def unique_list():
#   return list(set(input("Enter comma-separated items for the list: ").split(",")))
#
# unique_list()


# 4. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

# def set_to_tuple():
#
#
#     set1 = set(input("Enter different kinds of data, separated by comma: ").split(","))
#     set2 = set(input("Enter different kinds of data, separated by comma: ").split(","))
#     listed = list(set1) + list(set2)
#     tupled = tuple(listed)
#     print(tupled)
#
#     return tupled
# set_to_tuple()
# #
# 5. შექმენი ფუნქცია, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.


# dict_ = {"name": "Leonardo",
#         "surname": "DiCaprio",
#         "age": 49,
#         "popular_movies": ["Titanic", "Inception", "The Revenant"]}
#
#
# def dict_is_empty():
#     if len(dict_) == 0:
#         print("The dictionary is empty.")
#     else:
#         print("The dictionary is not empty.")
#
#
# dict_is_empty()

# N2

# def is_dict_empty(dictio):
#     return not bool(dictio)
#
#
# dict_ = {"Name": "Leonardo",
#         "Surname": "DiCaprio",
#         "Age": 49,
#         "Popular_movies": ["Titanic", "Inception", "The Revenant"]}
#
# dict_io = {}
# print(is_dict_empty(dict_))
# print(is_dict_empty(dict_io))


# 6.დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა. მაგალითად პროგრამას გადავეცით
# სტრიქონი: ''w3schools''; უნდა დააბრუნოს ლექსიკონი:
#
# {'w': 1, '3': 1, ‘s': 2, ‘c': 1, ‘h': 1, 'o': 2, ‘l': 1}

# def char_count(text):
#   char_dict = {}
#   for char in text:
#     if char in char_dict:
#       char_dict[char] += 1
#     else:
#       char_dict[char] = 1
#   return char_dict
#
#
# text = "w3schools"
# char_dict = char_count(text)
# print(char_dict)

#
# არასავალდებულო
#
# 7. შექმენი while ციკლი, რომელიც მომხმარებელს ხუთჯერ
# შემოატანინებს ინფორმაციას და ჩაამატებს ცარიელ
# სიაში. შედეგი დაბეჭდე. (append მეთოდი)
#
# x = 0
# input_list = []
# while x < 5:
#     z = input("Enter any info: ")
#     input_list.append(z)
#     x += 1
#
# print(input_list)
# # 8. მიღებული სიის პირველ და ბოლო ელემენტებს ადგილი
# # შეუცვალე და დაბეჭდე შედეგი.
# # წაშალე სიაში მომხმარებლის მიერ მოთხოვნილი
# # ელემენტი. (remove მეთოდი)
# #
# input_list[0], input_list[-1] = input_list[-1], input_list[0]
# print(input_list)
# 9. იპოვე სიის სიგრძე მინიმუმ ორი მეთოდით.

# furniture = ["Tables", "Chairs", "Beds", "Desks", "Dressers", "Cabinets", "Cupboards"]
# f_length = len(furniture)
#
# print(f"The list of furniture contains {f_length} items.")


# furniture = ["Tables", "Chairs", "Beds", "Desks", "Dressers", "Cabinets", "Cupboards", "Mirror"]
# f_length = 0
#
# for i in furniture:
#     f_length += 1
#
# print(f"The list of furniture contains {f_length} items.")


# 10. ამობეჭდე სიის ყოველი ელემენტი მის ინდექსთან
# ერთად მინიმუმ ორი მეთოდით.
# furniture = ["Tables", "Chairs", "Beds", "Desks", "Dressers", "Cabinets", "Cupboards", "Mirror", "Wardrobe"]
# # N1
# # for i in furniture:
# #     print(f"{i}, {furniture.index(i) + 1}")
# # N2
# item_index_dict = {item: furniture.index(item) + 1 for item in furniture}
#
# for item, index in item_index_dict.items():
#   print(f"{item}: [{index}]")
# 11. შეკრიბე ორი სია და დაბეჭდე შედეგი.

# list1 = ["Tables", "Chairs", "Beds", "Desks", "Dressers", "Cabinets", "Cupboards", "Mirror", "Wardrobe"]
# list2 = ["Titanic", "Inception", "The Revenant", "Harry Potter series", "Beauty and the Beast", "Little Women"]
#
# list3 = list1 + list2
#
# print(list3)

# 12. შეასრულე იგივე ოპერაცია extend მეთოდის
# დახმარებით.
#
# list1 = ["Tables", "Chairs", "Beds", "Desks", "Dressers", "Cabinets", "Cupboards", "Mirror", "Wardrobe"]
# list2 = ["Titanic", "Inception", "The Revenant", "Harry Potter series", "Beauty and the Beast", "Little Women"]
#
# list1.extend(list2)
# print(list1)
# 13. გაამრავლე სია რიცხვზე და დაბეჭდე შედეგი.
#
# list2 = ["Titanic", "Inception", "The Revenant", "Harry Potter series"]
# x = list2 * 2
#
# print(x)
#
# 14. Slicing _ ის გამოყენებით შეაბრუნე სია და დაბეჭდე
# შედეგი.
# list_a = ["a", "b", "c", "d", "e", "f", "g", "h"]
# list_reversed = list_a[8:0:-1]
#
# print(f" Original list: {list_a}\n Reversed list: {list_reversed}")


# 15. გააკეთე იგივე reverse მეთოდის გამოყენებით.
# list_a = ["a", "b", "c", "d", "e", "f", "g", "h"]
# list_a.reverse()
#
# print(f"There is no original list anymore.\nReversed list is:  {list_a}")

# 16. მომხმარებელს შემოაყვანინე წინადადება და
# გადააქციე სიტყვების სიად.
# sentence = input("Please enter any sentence: ")
# sentence_list = sentence.split(" ")
#
# print(sentence_list)

# 17. დაწერე პროგრამა, რომელიც ცარიელ სიაში
# ჩაამატებს 10 შემთხვევითად შერჩეულ რიცხვს,
# რიცხვების დიაპაზონი შემოჰყავს მომხმარებელს.


# import random
#
# ran_nums = []
# x = int(input("enter the min value: "))
# y = int(input("enter the max value: "))
# for _ in range(10):
#   # Generate random number between min_value and max_value (inclusive)
#   ran_nums.append(random.randint(x, y))
#
# print(ran_nums)
# 18. მოცემულია სია:
#
# [“apple”, “orange”, “banana”, “strawberry”]
# მომხმარებელს შეაყვანინე სიტყვა, და თუ ეს სიტყვა
# მოიძებნა მოცემულ სიაში, ამობეჭდე მისი ინდექსი.
#
# 19. შემთხვევითი რიცხვებით შექმენი სია, იპოვე
# მინიმალური და მაქსიმალური ელემენტი და დაბეჭდე. (min
# max ფუნქციები)
# 20. წაშალე სიის ბოლო ელემენტი, ამავე დროს ამოპრინტე
# წაშლილი ელემენტი და მიღებული სია. (pop მეთოდის
# გამოყენებით)
#
# 21.დაითვალე სიაში არსებული კონკრეტული ერთნაირი
# ელემენტების რაოდენობა. (count მეთოდი)
#
# 22. მომხმარებლის მიერ შემოყვანილი წინადადება გადააქციე
# სიად. შემდეგ ეს სია ელემენტებისგან გაასუფთავე და
# დაბეჭდე შედეგი. (clear მეთოდი)
# 23. არსებულ სიაში ჩაამატე „third indexed“ ელემენტი მესამე
# ინდექსის ადგილას. (insert მეთოდი)
