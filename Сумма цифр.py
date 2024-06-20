x = int(input())
def sumcifr(x):
    cnt = 0
    while x != 0:
        cnt += x % 10
        x //= 10
    return cnt

while x > 9:
    x = sumcifr(x)
print(x)