n = int(input("Enter odd line no.: "))

if n % 2 == 0:
    print("Please enter odd line no:")
else:
    a = (n + 1) // 2
    b = n - a

    # Upper half
    for i in range(1, a + 1):
        for j in range(a - i):
            print("   ", end=" ")
        
        for k in range(2 * i - 1):
            print(" * ", end=" ")
        
        print()

    # Lower half
    for i in range(b, 0, -1):
        for j in range(a - i):
            print("   ", end=" ")
        
        for k in range(2 * i - 1):
            print(" * ", end=" ")
        
        print()