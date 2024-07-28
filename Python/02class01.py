class Student():

    def __init__(self, name, gpa):
        
        self.name = name
        self.gpa = gpa

stu1 = Student("Jose", 4.0)
stu2 = Student("Mimi", 3.5)

print(stu1.name)
print(stu2.gpa)