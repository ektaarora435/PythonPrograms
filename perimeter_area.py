def areaperimeter():
 side1=int(input("Enter side 1: "))
 side2=int(input("Enter side 2: "))
 side3=int(input("Enter side 3: "))
 assert((side1+side2)>side3)and((side2+side3)>side1)and((side1+side3)>side2)
 perimeter = side1+side2+side3;
 s = perimeter/2;
 area = (s*(s-side1)*(s-side2)*(s-side3))**(1/2)
 return (area,perimeter)
#Calling Function
ap = areaperimeter()
print("Area and Perimeter: ",ap)