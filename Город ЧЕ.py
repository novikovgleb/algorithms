n, r = map(int, input().split())
d = list(map(int, input().split()))
last = 0
cnt = 0
for first in range(n):
    while last < n and d[last] - d[first] <= r:
        last += 1
    if d[last] - d[first] > r:
        if last == n - 1:
            cnt += 1
        else:
            cnt += n - last
print(cnt)