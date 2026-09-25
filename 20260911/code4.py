# This program prints the first x multiples of 5, where x is a user-defined number. If the multiple is even, it prints the multiple; if it is odd, it prints the negative of the multiple.

x=int(input("Enter a number: "))
for i in range(x):
    a=i*5
    if a % 2 == 0:
        print(a)
    else:
        print(-a)    