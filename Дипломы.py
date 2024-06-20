w, h, n = list(map(int, input().split()))
def lbinsearch(l, r, check, w, h, n):
    while l < r:
        m = (l + r) // 2
        if check(m, w, h, n):
            r = m
        else:
            l = m + 1
    return l


def check(m, w, h, n):
    return (m // w) * (m // h) >= n

print(lbinsearch(0, max(h,w) * n, check, w, h, n))