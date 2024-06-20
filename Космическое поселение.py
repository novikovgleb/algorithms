def rbinsearch(l, r, check, n , a, b, w ,h):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, n, a, b, w ,h):
            l = m
        else:
             r = m - 1
    return l


def check1(m, n, a, b, w ,h):
    return (w // (m * 2 + a)) * (h // (m * 2 + b)) >= n or (h // (m * 2 + a)) * (w // (m * 2 + b)) >= n

"""
def check2(m, n, a, b, w, h):
    return (h // (m * 2 + a)) * (w // (m * 2 + b)) <= n
"""


n, a, b, w, h = map(int,input().split())
print(rbinsearch(0, max(h, w) * n , check1, n, a, b, w, h))
#print(lbinsearch(0, max(h, w) * n , check2, n, a, b, w, h))