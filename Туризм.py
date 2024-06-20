n = int(input())
x, y = map(int, input().split())
prefixsum = [0]
prefixsumobr = [0]
for i in range(1, n):
    x, y1 =map(int, input().split())
    if y < y1:
        prefixsum.append( y1 - y)
        prefixsumobr.append(0)
    elif y > y1:
        prefixsumobr.append( y - y1)
        prefixsum.append(0)
    else:
        prefixsumobr.append(0)
        prefixsum.append(0)
    y = y1

for i in range(int(input())):
    x, y = map(int, input().split())
    if x <= y:
        print(sum(prefixsum[x:y]))
    else:
        print(sum(prefixsumobr[y:x]))
