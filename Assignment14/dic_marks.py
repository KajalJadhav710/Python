#dictionary marks

marks = {"Sarvesha":[67,76,89,87,88],"Divya" : [56,76,85,78,73],"Raj":[67,87,73,86,87],"pratik":[83,64,53,78,75]}

for i in marks :
    print(i,marks[i] )
    s = 0
    for j in marks[i]:
        print(j)
        s = s+j
        


mrk = {"ishika":[52,85,65,95,78],"Sakshi":[96,45,56,59,45],"Avntika":[67,87,57,85,78],"Suprabha":[83,64,53,78,75]}
lst1 = []
lst2 = []
for i in mrk:
    s = 0
    lst1.append(i)
    for j in mrk[i]:
        s = s+j
        lst2.append(s/5)
        
    
print(lst1,lst2)
d = dict(zip(lst1,lst2))
m = max(lst2)

for p in d:
    if(m == d[p]):
        print("topper is :",p ,"with", d[p])
        print("max per :",m,d)      
