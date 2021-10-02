import area_function

print("***Welcome***")
print("Your choice is their:-")
print("1.Area of circle")
print("2.Area of tringle")
print("3.Area of square")

choice = int(input("Enter your choice:-"))

if choice == 1:
    r=float(input("Enter Redius:-"))
    print("ans" + area_function.area_circle(r))

elif choice == 2 :
    h=float(input("Enter height:-"))
    b=float(input("Enter base:-"))
    print("Answer is:", area_function.area_tringle(h,b))
    
elif choice == 3 :
    s=float(input("Enter Side:-"))
    print("Answer:", area_function.area_square(s))

else:
    print("Error!!!")
