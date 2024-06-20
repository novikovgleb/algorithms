n, k = map(int, input().split())
s = input()
mydict = {}
ansfirst = 0
anslen = 0
last = 0
for first in range(n):
    while last < n and (s[last] not in mydict or mydict[s[last]] < k):
        if s[last] not in mydict:
            mydict[s[last]] = 1
        else:
            mydict[s[last]] += 1
        last += 1
    if last - first  > anslen:
        anslen = last - first
        ansfirst = first
    mydict[s[first]] -= 1
print(anslen ,ansfirst + 1)