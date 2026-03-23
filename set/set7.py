set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set()

for i in set1:
    if i not in set2:
        result.add(i)

for j in set2:
    if j not in set1:
        result.add(j)

print(result)