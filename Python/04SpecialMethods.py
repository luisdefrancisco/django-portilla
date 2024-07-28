class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): ## Imprime el contenido y no dirección memoria
        return f"{self.title} written by {self.author}"
    
    def __len__(self):
        return self.pages
    
book1 = Book("Juego de tronos", "G.R.R.Martin", 1100)
print(book1)
print(str(len(book1))+ " pages")
    
