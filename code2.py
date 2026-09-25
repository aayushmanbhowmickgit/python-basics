 #PROGRAM TO FIND THE TOTAL DAYS TAKEN BY THE WORKERS, IF THEY DO WORK TOGETHER
x=int(input("enter the no. of days taken by the 1st worker to do the work alone:"))
y=int(input("enter the no. of days taken by the 2nd worker to do the work alone:"))
z=int(input("enter the no. of days taken by the 3rd worker to do the work alone:"))
a=round((x*y*z)/((x*y)+(y*z)+(z*x)),2)
print("THE TOTAL DAYS TAKEN BY THE WORKERS, IF THEY DO WORK TOGETHER:",a)