n = int(str(bin(int(input())))[2:])
cnt = 0
while n != 0:
    if n % 2 == 0:
        n //= 10
        cnt += 1
    if n % 2 == 1:
        n -= 1
        cnt += 1
print(cnt)