n, k = map(int, input().split())
d = list(map(int, input().split()))
ansfirst = 0
anslast = 0
lenarr = float('inf')
for first in range(n):
    myset = set()
    last = first
    while last < n  and len(myset) < k:
        myset.add(d[last])
        last+=1
    if len(d[first:last]) < lenarr and len(set(d[first:last])) == k:
        lenarr = len(d[first:last])
        ansfirst = first
        anslast = last
print(ansfirst + 1, anslast)