from collections import deque

a = list(map(int, input().split()))
s = deque()
for i in a:
    if i != 0:
        s.append(i)
while len(s) > 0:
    print(s[-1], end = ' ')
    s.pop()