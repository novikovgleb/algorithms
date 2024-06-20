n, k = map(int, input().split())
s = input()
first, last = 0, 0
d = {}
maxcnt = 0
for el in s:
    d[el] = d.get(el, 0) + 1
while last < n:
    if d[s[last]] >= k:
        newd = {}
        while last < n and d[s[last]] >= k:
            newd[s[last]] = newd.get(s[last], 0) + 1
            last += 1
        if min(newd.values()) >= k:
            maxcnt = max(last - first, maxcnt)
    else:
        last += 1
        first = last

print(maxcnt)