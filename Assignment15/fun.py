def demo(a,b=20):
    c = a+b
    return c

x=demo(32)
print(x)
print("--------")


def demo(a,b=20):
    global c
    c = a + b
    return c

y = 200
x = demo (22,100)
print(c)
    
