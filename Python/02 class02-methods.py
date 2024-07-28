class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
    
    def perimeter(self):
        return self.radius*2*self.pi

    def double_radius(self):
        self.radius = self.raius*2

mycircle = Circle(radius = 4)
print(mycircle.perimeter())