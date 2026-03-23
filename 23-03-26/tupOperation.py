t = (1, "a", 5, 10, "hello")

nums = [i for i in t if isinstance(i, int)]
print("Numbers:", nums)

try:
    t[0] = 100
except:
    print("Tuple is immutable")

t2 = (20, 30)
print("Concatenated:", t + t2)