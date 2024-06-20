s = input()
glas = 'aeiouy'
d = {}
cnt = 0
for i in range(len(s)):
    if s[i] not in glas:
        d['sogl'] = d.get('sogl', 0) + 1
        if d['sogl'] == 3:
            cnt += 1
            d['sogl'] = 1
        d['glas'] = 0
    else:
        d['glas'] = d.get('glas', 0) + 1
        if d['glas'] == 3:
            cnt += 1
            d['glas'] = 1
        d['sogl'] = 0
print(cnt)