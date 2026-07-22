class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def eat(self):
        print(f"{self.name} is eating")
class Cat(Animal):
    def meow(self):
        print(f"MY cat's name is {self.name} and its color is {self.color}")
c1 = Cat("Rony","Orange")
c2 = Cat("Nick","White")
c1.eat()
c2.eat()
c1.meow()
c2.meow()
