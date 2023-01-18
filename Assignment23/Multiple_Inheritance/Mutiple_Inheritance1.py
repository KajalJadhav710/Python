class college():
    def __init__(self):
        self.Founder = "Adv.Sadashivrao patil"
        self.name = "AITRC"
        self.Branches ="CSE","Electronics","Mechanical","civil","Electrical"
        self.Pincode = 415311
        self.Pri_Name = "D.K.Mahadik"
    def details(self):
        print(self.Founder, self.name , self.Branches , self.Pincode , self.Pri_Name)

class Department():
    def __init__(self):
        self.Name = "CSE"
        self.HOD = "Mahadik D.K"
        self.Class = "FY,SY,TY,B-Tech"
        
    def details1(self):
        print(self.Name , self.HOD, self.Class)


class student(college,Department):
    def __init__(self):
        self.name = "Gayatri"
        self.RollNo = 57
        self.Email_id = "abc34@gmail.com"
        self.address = "pune"
        self.age = 20
        college.__init__(self)
        Department.__init__(self)
        
    def details2(self):
        print(self.name,self.RollNo , self.Email_id , self.address , self.age)
    
T = student()
T.details()
T.details1()
