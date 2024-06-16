# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით

class Transport:
    mode = "land"
    speed = "150km/h"
    color = "White"
    price = "$50,800"

# 2. დაამატე ერთი სტატიკური მეთოდი.

    @staticmethod
    def moving():
        print("~-~---~-~")

# 3. დაამატე ორი კლასის მეთოდი.
    @classmethod
    def present(cls):
        print(f"Can move on {cls.mode}")

    @classmethod
    def cost(cls):
        print(f"You can purchase some cars approximately for {cls.price}")
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის
# პარამეტრი.

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f"This transport is a car, {self.brand}, {self.model}, launched in {self.year} and moves on {self.mode}."



# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
    def introduction(self):
        print(f"It is a {self.brand}, model {self.model}, launched in {self.year}")

# 6. დაამატე __repr__ magic მეთოდი
# თანმიმდევრულობაში არ ჯდებოდა და __init__-ის ქვეშ დავწერე

# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.

car1 = Transport("BMW", "M8 Competition Convertible", "2025")
car1.price = "$150,000"
car1.color = "Red"
car1.speed = "250km/h"

car2 = Transport("Ford", "Mustang", "1964")
car3 = Transport("Audi", "Quattro", "1980")
car4 = Transport("Mercedes", "AMG GT Black", "2021")
car5 = Transport("Ferrari", "Portofino", "2023")
car6 = Transport("Lamborghini", "Revuelto", "2024")

print(car4)
print(car1)
#აბსტრაქტული მეთოდი
Transport.moving()
#კლასის მეთოდები
Transport.cost()
Transport.present()
#კლასის პარამეტრი
print(Transport.speed)
#ობიექტის პარამეტრები
print(car5.brand)
print(car2.model)
#ობიექტის მეთოდები
print(car6.introduction())