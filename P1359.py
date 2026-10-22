n = int(input().strip())

r = []

for i in range(n - 1):
    inp = list(map(int, input().strip().split()))
    tmp = ([0] * i) + inp
    r.append(tmp)

dp = [1e9] * n
dp[0] = 0

for i in range(1, n):
    for j in range(0, i):
        dp[i] = min(dp[i], dp[j] + r[j][i - 1])

print(dp[n - 1])

