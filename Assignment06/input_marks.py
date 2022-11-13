marks = []
i = 0

while(i < 5):
   c = int(input(" Enter your marks :"))
   marks.append(c)
   i = i + 1

print("List of marks is :",marks)


i = 0
sum = 0


while(i < len(marks)):
    sum = sum + marks[i]
    i = i + 1

print("sum of the total marks :" , sum)
  
per = sum / 5
print("per of the marks is :",sum )

if(per < 100 and per > 75):
    print("distinction ")
elif(per < 75 and per > 50):
    print("1st class ")
elif(per < 50 and per > 40):
    print("second class ")
elif(per < 40 and per >35 ) :
    print("pass")
elif(per < 35 and per > 0):
    print(" Fail ")
    
else :
    print("Thanks")
