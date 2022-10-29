l = input("Enter the length :")
h = input("Enter the height :")

x=int(l)
y=int(h)
rectangle = x * y
print("area of rectangle in cm :", rectangle)

area_of_rect_in_mm = rectangle * 10
print("area of rect in mm :",area_of_rect_in_mm)

area_of_rect_in_meter = rectangle / 100
print("area of rect in meter :",area_of_rect_in_meter)


area_of_rect_in_ft = rectangle / 30.48
print("area of rect in ft :",area_of_rect_in_ft)




