class Mrk():
    
    def add(self,*k):
        total = []
        for i in k:
            sum=0
            for j in i:
                sum = sum + j
            total.append(sum)

        return total
    
        
            
x = Mrk()
Mrk = x.add((67,89,78,65,89),(45,67,87,98,78),(67,77,88,65,87),(87,76,87,65,77))
print(Mrk)
