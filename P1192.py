n, k = map(int, input().strip().split())
dp = [0] * (n + 1)
dp[0] = 1

MOD = 100003

for i in range(1, n + 1):
    if i <= k:
        for j in range(1, i + 1):
            dp[i] = (dp[i] + dp[i - j]) % MOD
    else:
        for j in range(1, k + 1):
            dp[i] = (dp[i] + dp[i - j]) % MOD

print(dp[n])
