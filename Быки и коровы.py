vasia = input()
petya = input()
biki = 0
korovi = 0
d = {}
clonvasia = vasia
clonpetya = petya
for el in vasia:
    d[el] = d.get(el, 0) + 1
for i in range(len(petya)):
    if vasia[i] == petya[i]:
        biki += 1
        d[petya[i]] -= 1
        clonpetya = clonpetya[:i] + clonpetya[i+1:]
        print(clonpetya)
        clonvasia = clonvasia[:i] + clonvasia[i+1:]
print(clonpetya,clonvasia,petya,vasia)
for i in range(len(clonpetya)):
    if clonpetya[i] in clonvasia and d[petya[i]] != 0:
        korovi += 1
        d[petya[i]] -= 1
print(biki)
print(korovi)