n = input("Enter a number: ")

count = {}

for digit in n:
    if digit in count:
        count[digit] += 1
    else:
        count[digit] = 1

for digit in count:
    print(digit, "=", count[digit])
