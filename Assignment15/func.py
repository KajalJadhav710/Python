def demo (a,b=30):
    global c
    c = a+b
    return c

c=50
x = demo(60,10)
print(x+c)
