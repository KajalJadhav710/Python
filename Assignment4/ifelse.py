age = int(input("Enter your age :"))

if(age>=18):
    x=input("do you have voter id ?( yes/No)")
    if(x == "yes"):
        print("you are eligible for vote...")
    else:
        print("you are not eligible for vote")
else:
    print("Thank you")
