def add():
    a = 20
    b = 40
    c = a + b
    d = a*b
    e = b - a

    return c,d,e


ad ,f,s = add()
print("return values ",ad ,f,s)
print(add())
    
def sub():
    a = 30
    b = 20
    return a-b

print("sub is :", sub())
