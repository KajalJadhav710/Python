amount = float(input("Take the amount :"))

if(amount > 1000 and amount < 1500):
    dis = amount * 0.02
    pay = amount - dis
    print("Discount of this product :", dis)
    print("Totally amount of the product :",pay)

elif(amount >= 1500 and amount < 2000):
    dis = amount * 0.03
    pay = amount - dis
    print("discount :",dis)
    print("Net pay :",pay)

elif(amount >= 2000 and amount < 1000000):
    dis = amount * 0.05
    pay = amount - dis
    print("discount :",dis)
    print("Net pay :",pay)
else :
    print("Thank you ....!!!")
