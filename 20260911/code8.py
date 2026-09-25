n=int(input("enter the range:"))
def print_diamond(n):
  # Upper half of the diamond (including the middle row)
  for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

  # Lower half of the diamond
  for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half of the diamond
  for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Set the number of rows for the upper half

print_diamond(n)    



# Set the number of rows for the upper half

print_diamond(n)