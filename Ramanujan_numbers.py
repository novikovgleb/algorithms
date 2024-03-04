'''
Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел.
Когда английский математик Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси,
на котором он приехал, было 1729, такое скучное и заурядное число.
На что Рамануджан ответил: "Нет, нет! Это очень интересное число.
Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами".

Далее приведено решение нахождения таких чисел до некоторого значения
'''
r = int(input())
for i in range(1,r):
    counter = 0
    for j in range(1,int(r**(1/3))+1):
        for k in range(j,int(r**(1/3))+1):
            if k**3+j**3 == i:
                counter+=1
                break
    if counter ==2:
        print(i)