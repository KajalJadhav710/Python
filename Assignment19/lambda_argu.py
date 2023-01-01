def add(x,y):
    z = x+y
    return z

print(add(30,46))
a = add(20,49)
print(a)


b = lambda x = 70,y = 58 : x+y
print(b())

c = lambda x = 30, y = 47 : x-y
print(c())


#lambda with arguments


add1 = lambda a,b : a+b
print("lambda with argument :" , add1(10,20))
print("lambda with argument :", add1 (30,40))
print("lambda with argument :" , add1(50,45))

