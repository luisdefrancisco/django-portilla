# TASK: Define the Students class with its special methods.
# MAKE SURE TO READ THE FULL INSTRUCTIONS ABOVE CAREFULLY, AS THE EVALUATION SCRIPT IS VERY STRICT.
# Link to Solution: https://gist.github.com/b4shy/2b4b866e68b5f402c9bdcbfcfedde5b7
class Students():
    def __init__(self, names):
        self.names = names
    def __len__(self):
        return len(self.names)
        
    def __str__(self):
        return f"{self.names}"

students = Students(["A", "B", "C"])
print(students)
print(len(students))