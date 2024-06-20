n = int(input())
seq = []
d = {}
for i in range(n):
    x = input().split()
    if x[0] == 'add':
        seq.append([int(x[1]), x[2]])
        d[x[2]] = d.get(x[2], 0) + int(x[1])
    elif x[0] == 'delete':
        for j in range(len(seq) - int(x[1]), len(seq)):
            d[seq[j][1]] -= seq[j][0]
        seq = seq[:len(seq) - int(x[1])]
    elif x[0] == 'get':
        print(d[x[1]])