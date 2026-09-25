# This program prints the multiplication table of a given number.

x=int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{x} x {i} = {x*i}")