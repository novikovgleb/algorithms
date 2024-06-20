n, x, y = map(int, input().split())
l, r = 0, (n - 1) * max(x, y)
while l < r:
    m = (r + l) // 2
    if (m // x + m // y) >= n - 1:
        r = m
    else:
        l = m + 1
print(l + min(x, y))
