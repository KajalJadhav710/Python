num = input("enter the value of keyboard :")
sum = 0
sum1 = 0
sum3 = 0
for i in num:
    sum = sum + int(i)
print(sum)

s = str(sum)
if(len(s)>1):
    for j in s:
        sum1=sum1+ int(j)
print(sum1)
s = str(sum1)
if(len(s)>=1):
    for p in s:
        sum3 = sum3+int (p)
    print(sum3)    
