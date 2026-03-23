def power(b, e):
    res = 1
    for _ in range(e):
        res *= b
    return res

print(power(2, 3))