class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def hello(self):
        print("hello!")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}")


class Agent(Person): ## HEREDAMOS DE PERSONA

    def __init__(self, first_name, last_name, code_name): ## NUEVO CONSTRUCTOR
        Person.__init__(self, first_name, last_name) ##HEREDAMOS DEL PADRE
        self.code_name = code_name

    def report(self): ## SOBREESCRIBIMOS ESTE METODO
        print("I am here")

    def reveal(self, password):
        if password == 123:
            print("I am a secret agent")
        else:
            self.report()

x = Person("John", "Smith")
x.report()

y = Agent("Luis", "Martin", "birdy")
y.reveal(123)