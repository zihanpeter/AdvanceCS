from collections import deque

s = input()
a = deque()
q = [0] * (len(s) + 5)
ans = 0

for i in range(len(s)):
    if s[i] in '([{':
        a.append((s[i], i))
    elif s[i] == ')' and len(a) > 0 and a[-1][0] == '(':
        q[a[-1][1]] += 1
        q[i + 1] -= 1
        a.pop()
    elif s[i] == ']' and len(a) > 0 and a[-1][0] == '[':
        q[a[-1][1]] += 1
        q[i + 1] -= 1
        a.pop()
    elif s[i] == '}' and len(a) > 0 and a[-1][0] == '{':
        q[a[-1][1]] += 1
        q[i + 1] -= 1
        a.pop()
    else:
        a.append((s[i], i))

for i in range(1, len(q)):
    q[i] += q[i - 1]

cnt = 0
for i in q:
    if i != 0:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)