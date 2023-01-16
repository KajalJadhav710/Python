class calculator():
    def __init__(self):
        self.a = 5
        self.b = 8
        
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

x = calculator()
y = calculator ()

x.add()
y.power()
x.sub()
y.mul()
x.div()
