import math

shape = input("Enter shape (rectangle/triangle/circle): ")

if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width

elif shape == "triangle":
    a = float(input("Enter 1st side: "))
    b = float(input("Enter 2nd side: "))
    c = float(input("Enter 3rd side: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

elif shape == "circle":
    radius = float(input("Enter radius: "))
    area = math.pi * radius * radius

else:
    print("Invalid shape")
    area = 0

print("Area =", area)
