password = input("enter your password from keyboard :")
i = 0
capital = 0
small = 0
number = 0
symbol = 0

if(len(password)>=8):
    i=0

while(i<len(password)):
    
        if(ord(password[i])>= 65 and ord(password[i])<=90):
            capital=1
        elif(ord(password[i])>= 97 and ord(password[i])<=122):
            small=1
        elif (ord(password[i])>= 48 and ord(password[i])<=57):
            number=1
        elif(password[i]=="@" or password[i]== "#" or password[i]=="$" or password[i]=="&" or password[i]=="%" or password[i]=="*"):
            symbol=1
        i= i+1

        if(capital==1 and small==1 and number==1 and symbol==1):
            print("password is valid")
        elif(capital==0 and small==1 and number==1 and symbol==1):
            print("one capital letter require")
        elif(capital==1 and small==0 and number==1 and symbol==1):
            print("one smalll letter require")
        elif(capital==1 and small==1 and number==1 and symbol==0):
            print("one special symbol require (@,#,$,*,&,%,*)")
        else :
            print("invalid password")
   
else:
    print("minimum 8 character password require")
