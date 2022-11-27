password = input("enter your password from keyboard :")
i = 0
Flag1 = 0
Flag2 = 0
Flag3 = 0
Flag4 = 0

while(i<len(password)):
    if(len(password)>=8):

        if(ord(password[i]) >= 65 and ord(password[i])<= 90):
            Flag1=1
            
        elif(ord(password[i])>= 97 and ord(password[i])<= 122):
            Flag2=1
        
        elif(ord(password[i])>= 48 and ord(password[i])<= 57):
            Flag3=1
            
        elif (ord(password[i])>= 58 and ord(password[i])<= 64):
            Flag4=1
       
    else:
        print("minimum 8 character password require")
        break
    
    i= i+1

if(Flag1 == 1 and Flag2 == 1 and Flag3== 1 and Flag4== 1):
    print("Password is Valid ")

else:
    print("Password is Invalid")
        
