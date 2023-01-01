def add(a,b):
    c = a + b
    return c

print(add(10,38))
d = add(87, 4)
print(d)

k = lambda a = 39, b= 27 : a + b
print(k())

power = lambda a = 8, b = 7 : a**b
print("lambda with  power function " , power(2,3))
print("lambda with power function " , power (8,6))
