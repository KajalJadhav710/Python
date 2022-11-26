a = int(input("take the number : "))
i=2
while(i < a):
    if(a%i==0):
        print("not prime")
        break
    i = i + 1
