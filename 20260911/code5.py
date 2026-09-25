n = int(input("Please enter a number: "))
numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
maxNumber = max(numbers)
minNumber = min(numbers)
print(f"The maximum number is: {maxNumber}")
print(f"The minimum number is: {minNumber}")