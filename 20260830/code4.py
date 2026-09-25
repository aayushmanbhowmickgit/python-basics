#program to find the maximum of three numbers using decision making(another method)
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
max=a
if(b>max):
    max=b           
if(c>max):
    max=c
print("maximum is:",max)