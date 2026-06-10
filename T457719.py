n = int(input())
a, b, c, s = [], [], [], []
for i in range(n):
    t = list(map(int, input().split()))
    a.append(t[0])
    b.append(t[1])
    c.append(t[2])
    s.append(t[0] + t[1] + t[2])
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if (abs(a[i] - a[j]) <= 5 and abs(b[i] - b[j]) <= 5 and abs(c[i] - c[j]) <= 5 and abs(s[i] - s[j]) <= 10):
            cnt += 1
print(cnt)