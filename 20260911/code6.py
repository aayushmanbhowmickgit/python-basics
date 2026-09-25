sum=0
n=int(input("Please enter a number: "))
for i in range(1, n+1):
    a=1/(i**3)
    sum+=a
print(f"The sum of the series is: {sum}")
