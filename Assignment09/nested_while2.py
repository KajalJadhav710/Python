a = [90, 78, 45 ,[567,78,95,89,77,87],32,67,56,10,(456,879,44),67,45]
i=0
sum = 0
while(i<len(a)):
    if(type(a[i]) == list or type(a[i])== tuple):
        j=0
        while(j < len(a[i])):
            sum = sum + a[i][j]

            j=j+1
    else :
        sum = sum + a[i]
    i = i+1
print(sum)    
