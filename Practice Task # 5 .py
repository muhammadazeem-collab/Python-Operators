# Example of Identity Operators

# Ask user to enter input values
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print(a is b)
print(a is not b)
print(id(a))
print(id(b))