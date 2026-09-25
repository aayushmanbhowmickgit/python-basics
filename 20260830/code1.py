#program to find area of triangle using decision making
a=int(input("enter 1st side:"))
b=int(input("enter 2nd side:"))
c=int(input("enter 3rd side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
if (a+b>c and a+c>b and b+c>a):
    print("area of triangle is:",area)
else:
    print(" ERROR........... triangle is not possible")    