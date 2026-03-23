t = (5, 15, 3, 20, "a")

l = list(t)
l = [i for i in l if not (isinstance(i, int) and i < 10)]

t = tuple(l)
print(t)