n, k = list(map(int, input().split()))
narr = list(map(int, input().split()))
karr = list(map(int, input().split()))
def lbinsearch(l,r,check,seq, x):
    while r - l > 1:
         m = (l + r) // 2
         if check(m, seq, x, r):
             r = m
         else:
             l = m
    return l, r
def check(m, seq, x, r):
    return seq[m] > x
for el in karr:
    ansl, ansr = lbinsearch(0, n - 1, check, narr, el)
    if abs(narr[ansl] - el) <= abs(narr[ansr] - el):
        print(narr[ansl])
    else:
        print(narr[ansr])
