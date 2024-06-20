s = input()
def delete(s):
    last = len(s) - 1
    curfirst = 0
    for first in range(len(s)-1):
        while last > 0 and s[last] == s[last - 1]:
            last -= 1
        if s[first] == s[first + 1]:
            curfirst += 1
    return curfirst, last

fl = True
while s[0] == s[-1]:
    print(len(set(s)))
    if len(set(s)) == 1:
        print('drugoians',0)
        fl = False
        break
    l, r = delete(s)
    print(l,r)
    if l == 0:
        s = s[1:r]
    else:
        s = s[l:r]
    if s == '' or len(s) == 1 or set(s) == 1:
        break
if fl:
    print('ans',len(s))