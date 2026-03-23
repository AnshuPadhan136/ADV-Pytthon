s = input("Enter: ")
from collections import Counter

c = Counter(s)

for i in s:
    if c[i] == 1 and i.isalnum():
        print(i, end=" ")