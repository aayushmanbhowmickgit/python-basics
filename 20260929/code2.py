first = input("Enter first name: ")
last = input("Enter last name: ")

username = first.lower() + last.lower()
initials = first[0].upper() + last[0].upper()

print("Username:", username)
print("Initials:", initials)
