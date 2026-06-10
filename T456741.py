n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    cnt = 0
    for j in range(i):
        if a[j] < a[i]:
            cnt += 1
    print(cnt, end=' ')