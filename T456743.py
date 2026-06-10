a = [1, 1, 2]
for i in range(3, 31):
    a.append(a[i - 1] + a[i - 2])
n = int(input())
for i in range(n):
    x = int(input())
    print(a[x - 1])