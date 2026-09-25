# This program checks if a person is eligible for a driving license based on their age.

name = input("Enter your name: ")
age = int(input("Enter your age: "))        
  
print(f"Name: {name}")
print(f"Age: {age}")

if age >= 18:
    print("You are eligible to have a driving license.")
else:
    print("You are not eligible to have a driving license.")  
 