marks = float(input("Enter your marks :"))

if(marks>=35 and marks < 50):
    print("pass")
elif(marks > 50 and marks < 60):
    print("second class")
elif(marks > 60 and marks < 75):
    print("first class")
elif(marks > 75 and marks < 100):
    print("you are first class distiction")
elif(marks<35):
    print("fail")
else:
    print("fail")
