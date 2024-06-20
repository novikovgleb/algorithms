"""n = int(input())
x = list(map(int, input().split()))
cnt = 0

def vig(seq):
    d = {}
    for el in seq:
        d[el] = d.get(el, 0) + el
    return max(d.items(), key=lambda x:x[1])
while len(x) > 0:
    k, v = vig(x)
    x = ''.join([str(el) for el in x])
    x.replace(str(k),'')
    x.replace(str(k+1),'')
    x.replace(str(k-1), '')
    x = list(map(int, list(x)))
    print(x)
    cnt += v
print(cnt)


while x != []:
    minvalue = min(x)
    cur = []
    cnt += minvalue
    print(cnt)
    for i in range(len(x)):
        if x[i] != x.index(minvalue) or x[i] != minvalue + 1 or x[i] != minvalue - 1:
            cur.append(x[i])
    print(cur)
    x = cur
print(cnt)
"""
from collections import Counter


def max_burleys(nums):
    count = dict(Counter(nums))
    print(count)
    max_num = max(nums)
    dp = [0] * (max_num + 1)

    for num in range(1, max_num + 1):
        if num in count:
            dp[num] = count[num] * num
        if num > 1:
            dp[num] = max(dp[num] + dp[num - 2], dp[num - 1])
        else:
            dp[num] = max(dp[num], dp[num - 1])

    return dp[max_num]


# Чтение входных данных
n = int(input())
nums = list(map(int, input().split()))

# Вычисление максимального количества бурлей
result = max_burleys(nums)
print(result)