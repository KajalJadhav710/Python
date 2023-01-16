class student():
    def mrk(self,*a):
        global s
        i = 0
        s = 0
        while(i < len(a)):
            s = s + a [i]
            i = i + 1
        return s

class abc():
    def info(self):
        print("info" , s)

x = student()
z = abc()


mrk = x.mrk(58,45,87,78,68)
print(mrk)


print('--------------------------------------')

class student1():
    def marks1(self,*a):
        i = 0
        j = 0
        for i in marks:
            s = 0
            s = s + i
            print(s)
            
            for j in marks:
                s = s + j
            print(s)

            
a = student1()
b = a.marks1('kajal' == [45,78,87,98,89],'tejal'== [67,98,78,76,74])
print(s)
