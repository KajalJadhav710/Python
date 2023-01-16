class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        c = self.a + self.b
        print(c)
    def sub(self):
        c = self.a - self.b
        print(c)
    def mul(self):
        c = self.a * self.b
        print(c)
    def div(self):
        c = self.a / self.b
        print(c)
    def power(self):
        c = self.a ** self.b
        print(c)

y = calculator(34,12)
z = calculator(14,738)

y.add()
z.power()
y.mul()
y.div()
z.sub()

