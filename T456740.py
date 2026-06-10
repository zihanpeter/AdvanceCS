a = input().split()
a = list(map(int, a))
for i in range(len(a) - 2, -1, -1):
    if i == 0:
        print(a[i])
    else:
        print(a[i], end=' ')