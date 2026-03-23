s = input("Enter: ")

print("Palindrome:", s == s[::-1])

vowels = "aeiouAEIOU"
v = c = d = sp = 0

for i in s:
    if i in vowels:
        v += 1
    elif i.isalpha():
        c += 1
    elif i.isdigit():
        d += 1
    else:
        sp += 1

print(v, c, d, sp)