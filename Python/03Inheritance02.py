# TASK: Implement the Animal class and create two child classes called Cat and Dog.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/b4shy/800abadcb17d4546dffe18b89ac1743b

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")
    def sound(self):
        print("Meawww")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
    def sound(self):
        print("ruff")