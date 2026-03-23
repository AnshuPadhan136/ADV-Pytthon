list1 = [1, 2, 3, 2, 4, 1, 5]

seen = set()
repeated = set()

for i in list1:
    if i in seen:
        repeated.add(i)
    else:
        seen.add(i)

print(repeated)