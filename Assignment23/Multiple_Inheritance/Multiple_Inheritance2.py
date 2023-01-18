class Google():
    def __init__(self):
        self.Name = "Google"
        self.CEO = "Sunder pichai"
        self.Founder = "Larry Page"
        self.Employee = "135,301..."
        self.Founded = "september 4 ,1998"
    def details(self):
        print(self.Name , self.CEO, self.Founder , self.Employee , self.Founded)

class CEO():
    def __init__(self):
        self.name = "Sunder pichai"
        self.country = "US"
        self.DOB = "10 June 1972"
        self.age = "52"
        
    def details1(self):
        print(self.name ,self.country  ,self.DOB,self.age )

class Founder(Google ,CEO):
    def __init__(self):
        self.name = "Larry Page"
        self.DOB ="26 March 1973"
        self.edu ="princeton University"
        self.age = "51"
        Google.__init__(self)
        CEO.__init__(self)
    
    def details2(self):
        print(self.name  ,self.DOB , self.edu , self.age)
   
y = Founder()
y.details()
y.details1()        
