a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)

print("Even/Odd:")
print(a, "Even" if a % 2 == 0 else "Odd")
print(b, "Even" if b % 2 == 0 else "Odd")

print("Float conversion:", float(a))