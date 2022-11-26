marks = [[56,78,65,90,52],[67,78,89,82,67],[77,78,59,54,45],[77,67,58,78,63]]
i=0
total=[]
while(i < len(marks)):
    print(marks[i])
    sum=0
    j=0
    while(j<len(marks[i])):
        sum = sum + marks[i][j]
        j = j+1
    total.append(sum/4)
    i=i+1
print(total)    
    
