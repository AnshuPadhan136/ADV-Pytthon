s = input("Enter sentence: ")

vowels = "aeiouAEIOU"
v = sum(1 for i in s if i in vowels)
c = sum(1 for i in s if i.isalpha() and i not in vowels)

print("Vowels:", v)
print("Consonants:", c)
print("Reverse:", s[::-1])
print("Underscore:", s.replace(" ", "_"))
print("Capitalized:", s.title())