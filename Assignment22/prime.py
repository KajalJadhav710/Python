def prime(a):
    flag = 0
    for i in range(2,a):
        if(a%i == 0):
            flag = 1
            break
    if(flag == 1):
        return "No is Not prime"
    else:
        return "prime"


#x,y =(prime(13))
#print(x)

def super_prime(x):    
    if (x == True):
        z = len (str(b))
    if (z>=2):
        s = 0
        for j in str (b):
            s = s + int(j)
        print(s)
        p,q = prime(s)
        if(x == True):
            print(" number is super prime ")
        else :
            print("number is not super prime ")
            
a,b
