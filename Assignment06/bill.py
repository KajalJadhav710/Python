

a = 0
total = 0
while(a < 100):
      amount = int(input("enter your amount is:"))
      total = total + amount
      b = input("do you want to continue (yes/no)")

      if(b == "no"):
          break
      a = a + 1
      print(total)

if( total > 5000 and total < 7000):
    dis = total * 0.02
    print("totally 2% discount is: ", dis)  
    result = total + dis
    print("paying the amount of :", total)

elif( total > 7000 and total < 10000):
    dis = total * 0.03
    print("totally 3% discount is: ", dis)  
    result = total + dis
    print("paying the amount of :", total)

elif( total > 10000 and total < 100000):
    dis = total * 0.05
    print("totally 5% discount is: ", dis)  
    result = total + dis
    print("paying the amount of :", total)

else:
    print("Something went wrong")
