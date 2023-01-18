class Book():
    def __init__(self):
        self.book = "harry potter"
        self.author = "j.k.rowling"
        self.price = 1400
        self.publisher = "bloomsbury"
        self.parts = 8
    def details(self):
        print( self.book, self.author, self.price, self.publisher, self.parts)
    
class book_author(Book):
    def __init__(self):
        self.name = "j.k.rowling"
        self.country = "UK"
        self.age = "53"
        self.DOB = "25/09/1969"
        Book.__init__(self)
        
    def details1(self):
        print(self.name,self.country , self.age , self.DOB )
    
obj = book_author()
obj.details()

