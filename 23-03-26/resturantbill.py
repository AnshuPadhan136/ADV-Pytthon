menu = {"pizza": 100, "burger": 50, "tea": 20}
total = 0

while True:
    item = input("Enter item (or exit): ")
    if item == "exit":
        break
    if item in menu:
        total += menu[item]

tax = total * 0.1
print("Total:", total + tax)