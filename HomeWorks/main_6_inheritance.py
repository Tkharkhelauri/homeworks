# დავალება 6
# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.

from abc import ABC, abstractmethod

class Country(ABC):
    @abstractmethod
    def getname(self):
        pass

    @abstractmethod
    def getpopulation(self):
        pass

    @abstractmethod
    def getflag(self):
        pass

    @abstractmethod
    def getcontinent(self):
        pass


# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (პარამეტრები???)(მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).

class Georgia(Country):
    def __init__(self, name, flag, continent, population):
        self.name = name
        self.flag = flag
        self.continent = continent
        self.population = population
        self.__budget = "29,000"
        self._capital = "Tbilisi"
        self.language = "Georgian"

    def getname(self):
        print(f"This country is {self.name}")

    def getflag(self):
        print(f"It's flag is {self.flag}")

    def getpopulation(self):
        print(f"Population is {self.population}")

    def getcontinent(self):
        print(f"It's located on {self.continent}")

# 3. შექმენი საქართველოს ობიექტი და გამოიყენე
# ზემოხსენებული მეთოდები.


georgia = Georgia("Georgia", "5 red crosses on a white background", "Eurasia", "3,500,000")
print(georgia._capital)
georgia.getpopulation()
georgia.getflag()
# print(georgia.__budget)
georgia.getcontinent()