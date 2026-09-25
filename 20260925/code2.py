n=int(input("enter a no.:"))
x=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if (rev==x):
    print("The number is pallindrom")
else:
    print("The number is not pallindrom")        
