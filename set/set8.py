s1 = "hello"
s2 = "world"

common = set(s1) & set(s2)

s1_new = "".join([c for c in s1 if c not in common])
s2_new = "".join([c for c in s2 if c not in common])

print(s1_new)
print(s2_new)