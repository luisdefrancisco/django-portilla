# TASK: Implement the dog class with age translation.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/b4shy/6f1ff905b2d42eb4e8d7cc51091e2407

class Dog():
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def calculate_human_age(self):
        return self.age*7

dog1 = Dog("Hans", "German Shepherd", 7)
print(dog1.calculate_human_age())