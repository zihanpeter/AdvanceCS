def f(x, last):
    if x == 0:
        return 1
    if x < 0:
        return 0
    if last - x == 1:
        return f(x - 2, x)
    else:
        return f(x - 1, x) + f(x - 2, x)
print(f(20, 20))