'''PROGRAM TO FIND THE LARGEST NUMBER AND
 THE SUM OF ALL NUMBERS EXCEPT THE LARGEST NUMBER 
 FROM A GIVEN ARRAY OF NUMBERS'''

n = int(input("Please enter a number: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
maxNumber = max(numbers)
numbers.remove(maxNumber)
print(numbers)
sum = sum( ) 