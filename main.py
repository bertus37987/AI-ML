class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

class Predator(Animal):
    def Hunt(self):
        print("Hunting")

class Peacfull():
    def Chill(self):
        print("Just chilling")
        