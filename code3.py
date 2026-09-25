 #PROGRAM TO FIND THE SUM, DIFFERENCE, PRODUCT AND DIVISION OF TWO NUMBERS
a=int(input("enetr 1st no:"))
b=int(input("enetr 2nd no:"))
c=a+b
if a>b:
    d=a-b
    f=a/b
else:
    d=b-a
    f=b/a
e=a*b
print("THEIR SUM IS:",c)
print("THEIR DIFFERENCE IS:",d)
print("THEIR PRODUCT IS",e)
print("THEIR DIVISION IS:",f)
