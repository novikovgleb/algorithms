n = int(input())
ai = list(map(int, input().split()))
m = int(input())
cond = []
for i in range(m):
    cond.append(list(map(int, input().split())))
ai.sort()
cond.sort()
print(ai,cond)
first = 0
totalcost = 0
for i in range(n):
    while first < m and ai[i] >= cond[first][0]:
        first += 1
    print(first-1)
    totalcost += cond[first-1][1]
print(totalcost)
