import abc

class LifeForm:
    health = 100
    
    @abc.abstractmethod
    def produce_energy(self):
        pass

    def breath(self):
        print("hehuhehu")

class Animal(LifeForm):
    @abc.abstractmethod
    def speak():
        pass

    def eat(self):
        print("nom nom")

    def drink(self):
        print("shlerp")

    def move(self):
        print("movin'")
    
    def produce_energy(self):
        self.eat()
        self.drink()

class Mammal(Animal):
    def produce_milk(self):
        print("milk")

class Human(Mammal):
    def __init__(self, name: str):
        super().__init__()

        self.name = name

    def speak(self):
        print(f"Jam jest {self.name}")

hum = Human("Ciapok")
hum.produce_energy()
hum.speak()