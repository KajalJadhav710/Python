a = "hello i am kajal jadhav from vita."
print(a)
for i in a :

    x=ord(i)
    if(i == " "):
        print(" " , end = "")
    elif(x >= 97 and x <= 122):

        c = x - 32
        print(chr(c),end = "")

        print()

b = "HELLO I AM KAJAL JADHAV FROM VITA.."
print(b)
for i in b :

    x=ord(i)
    if(i == " "):
        print(" " , end = "")
    elif(x >= 65 and x <= 90):

        c = x + 32
        print(chr(c),end = "")
