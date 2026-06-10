a = [0] * (10 ** 6 + 5)
a[1] = 0
n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    if x[0] == 1:
        t = a[x[1]]
        a[x[1]] = x[2]
        a[x[2]] = t
    elif x[0] == 2:
        print(a[x[1]])
    else:
        a[x[1]] = a[a[x[1]]]