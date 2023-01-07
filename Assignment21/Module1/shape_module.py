def circle ():
    R = input("enter the radius  of circle :")
    a = int(R)
    b = 3.14 * a * a
    return b

def rectangle():
    l = input("enter the length of rectangle :")
    h = input("enter the height of rectangle :")
    x = int(l)
    y = int(h)
    z = x * y
    return z

def square():
    s = input("enter the side of the square :")
    j = int(s)
    squ = j * j
    return squ


   
if(__name__ == "__main__"):

    circle()
    rectangle()
    square()


