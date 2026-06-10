m, n = map(int, input().split())
a = [0] * 10
for i in range(m, n + 1):
    # s = str(i)
    # for j in s:
    #     a[ord(j) - ord('0')] += 1
    while i > 0:
        a[i % 10] += 1
        i //= 10
for i in a:
    print(i, end=' ')