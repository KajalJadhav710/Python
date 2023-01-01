def mrk():
    a = [[35,67,85,47,76],[76,55,65,88,89],[87,88,67,76,77],[76,87,98,89,86]]
    lst = []

    for i in a:
        s = 0
        for j in i:
            s = s + j
        lst.append(s)
    return lst

b = mrk()
print("sum of number is :",b)

lst1 = []

for b in mrk():

    per = b/5
    lst1.append(per)

print("percentage list :",lst1)
