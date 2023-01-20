class computer_science():
    def Result(self):
        print("1st year marks of student is 70%")
        print("2nd year marks of student is 80%")
        print("3rd year marks of student is 75%")
        print("B-tech of the marks is 85%")

class Electronics():
    def Result(self):
        print("1st year marks of student is 72%")
        print("2nd year marks of student is 75%")
        print("3rd year marks of student is 85%")
        print("B-tech of the marks is 87%")

class Department():
    def percentage(self,p):
        p.Result()

d = Department()
E = Electronics()
d.percentage(E)
print("......")
C = computer_science()
d.percentage(C)
