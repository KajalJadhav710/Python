class company():
    def __init__(self):
        self.name = "Amazon"
        self.country = "US"
        self.owner = "jeff bezos"
        self.No_of_emloyee = "1,544,000"
        
    def details(self):
        print(self.name ,self.country ,self.owner , self.No_of_emloyee)

class Amazon(company):
    def __init__(self):
        self.name = "jeff bezos"
        self.DOB ="12/01/1964"
        self.edu ="princeton University"
        company.__init__(self)
    
    def details1(self):
        print(self.name  ,self.DOB , self.edu)
   
x = Amazon()
x.details()
        
