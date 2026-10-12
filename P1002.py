n, m, x, y = map(int, input().strip().split())
n += 1
m += 1
x += 1
y += 1

cx = [0, 1, 1, 2, 2, -1, -1, -2, -2]
cy = [0, 2, -2, 1, -1, 2, -2, 1, -1]

dp = [[0] * (m + 1) for _ in range(n + 1)]
vis = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(9):
    if x + cx[i] < 1 or x + cx[i] > n or y + cy[i] < 1 or y + cy[i] > m:
        continue
    vis[x + cx[i]][y + cy[i]] = True

dp[0][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if vis[i][j]:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[n][m])