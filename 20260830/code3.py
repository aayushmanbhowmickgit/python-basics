#program to find the maximum of three numbers using decision making
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if(a>b and a>c):
    print("maximum is:",a)
elif(b>a and b>c):
    print("maximum is:",b)
else:
    print("maximum is:",c)