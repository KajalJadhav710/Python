def max_num(a,b):
    if(a>b):
        return a
    else :
        return b

print(max_num(7945,5567))    
print(max_num(64,78))

max1 = lambda a,b : a if(a>b) else b
print("max_num  is :" ,max1(206,569))

max = lambda a : a*a
print(max(6))
