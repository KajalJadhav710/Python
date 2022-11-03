mrk = float(input("enter your marks :"))

if(mrk>35):
    print("you are pass")
    if(mrk>50):
        print("you are second class")
        if(mrk > 60):
            print("you are first class")
            if(mrk > 75):
                print("you are first class distinction")
else:
    print("Fail")
