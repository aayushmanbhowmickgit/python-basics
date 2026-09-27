n=int(input("Enter a number: "))
rev=0
x=n
while(n>0):
    r=n%10
    rev=rev+r**3
    n=n//10
if rev==x: 
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")       