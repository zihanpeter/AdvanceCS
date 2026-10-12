n, w = map(int, input().split())
a = list(map(int, input().split()))
dp = [1e5] * int(1e5)
for i in a:
    dp[i] = 1
for i in range(1, w + 1):
    for j in range(len(a)):
        if i - a[j] < 1:
            continue
        dp[i] = min(dp[i], dp[i - a[j]] + 1)
print(dp[w])