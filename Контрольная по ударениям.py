n = int(input())
slovar = set()
for i in range(n):
    sl = input()
    slovar.add(sl)
    slovar.add(sl.lower())
text = input().split()
counter = 0
for word in text:
    if (word.lower() in slovar and word not in slovar):
        counter += 1
    elif word == word.lower():
        counter += 1
    elif (word not in slovar and len([l for l in word if l.isupper()]) != 1):
        slovar.add(word.lower())
        counter += 1
print(counter)