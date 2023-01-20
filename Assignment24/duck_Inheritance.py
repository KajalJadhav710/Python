class circle():
    def area(self):
        print("area of circle")
        print("Radius of circle is 14")
        print("3.14*r*r")
        
class Rectangle():
    def area(self):
        print("Area of rectangle ")
        print("Base of rectangle is 10cm")
        print("height of rectangle is 5cm")

class square():
    def shapes(self ,a):
        a.area()

s = square()
r = Rectangle()
c = circle()
s.shapes(r)
print("...")
s.shapes(c)
        
        
