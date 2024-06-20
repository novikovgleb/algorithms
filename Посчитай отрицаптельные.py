n, m = map(int, input().split())
cnt = 0
array = []
for i in range(n):
   array.append(input())
   cnt += array[i].count('-')
print(cnt)
