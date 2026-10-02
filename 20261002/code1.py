# This program checks if a given number is within a specified range.

number = float(input("Enter a number: "))
lower = float(input("Enter the lower limit: "))
upper = float(input("Enter the upper limit: "))

if lower <= number <= upper:
    print("The number is within the range.")
else:
    print("The number is outside the range.")
