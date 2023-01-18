class Book():
    def __init__(self):
        self.book = "Harry Potter"
        self.author = "J.K.Rowling"
        self.price = 1300
        self.parts = 8
        
        
    def details(self):
        print(self.book , self.author,self.price , self.parts)

class publisher(Book):
    def __init__(self):
        self.name = "Bloomsburry"
        self.country = "Uk"
        self.age = " age is 53"
        Book.__init__(self)
    def details1(self):
        print(self.name , self.country , self.age)


class Author(Book):
    def __init__(self):
        self.name = "j.k.Rowling"
        self.age = " age is 52"
        self.DOB = "25/98/1969"
        Book.__init__(self)
        
    def details2(self):
        print(self.name , self.age, self.DOB)

b = Author()
c = publisher()
b.details()
c.details()

    
