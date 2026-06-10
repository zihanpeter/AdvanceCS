n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())

cx = [0, 0, 1, -1, 1, -1, 1, -1]
cy = [1, -1, 0, 0, 1, -1, -1, 1]

for i in range(n):
    for j in range(m):
        if a[i][j] == '?':
            cnt = 0
            for t in range(8):
                ti = cx[t] + i
                tj = cy[t] + j
                if ti < 0 or tj < 0 or ti >= n or tj >= m:
                    continue
                if a[ti][tj] == '*':
                    cnt += 1
            print(cnt, end='')
        else:
            print('*', end='')
    print()