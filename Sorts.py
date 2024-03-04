#https://ru.wikipedia.org/wiki/Алгоритм_сортировки
#Пузырьковая сортировка
'''
Алгоритм сортировки пузырьком состоит из повторяющихся проходов по сортируемому списку.
За каждый проход элементы последовательно сравниваются попарно и, если порядок в паре неверный,
выполняется обмен элементов. Проходы по списку повторяются n−1 раз, где n – длина списка.
При каждом проходе алгоритма по внутреннему циклу, очередной наибольший элемент списка ставится на
свое место в конце списка рядом с предыдущим «наибольшим элементом».
'''
a=[]
n = len(a)

for i in range(n - 1):
    exchanges = 0
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            exchanges += 1
            a[j], a[j + 1] = a[j + 1], a[j]

    if exchanges == 0:
        break

print(a)


#Сортировка выбором
'''
Сортировка выбором улучшает пузырьковую сортировку, совершая всего один обмен за каждый проход по списку. 
Для этого алгоритм ищет максимальный элемент и помещает его на соответствующую позицию. 
Как и для пузырьковой сортировки, после первого прохода самый большой элемент находится на 
правильном месте. После второго прохода на своё место становится следующий максимальный элемент. 
Проходы по списку повторяются n−1 раз, где n – длина списка, поскольку последний из них автоматически 
оказывается на своем месте.
'''
a=[]
n = len(a)

for i in range(n):
    mx_ind = n - 1 - i
    for j in range(n - i):
        if a[j] > a[mx_ind]:
            mx_ind = j

    a[n - 1 - i], a[mx_ind] = a[mx_ind], a[n - 1 - i]

print(a)

#Сортировка простыми вставками
'''
Алгоритм сортировки простыми вставками делит список на 2 части — отсортированную и неотсортированную. 
Из неотсортированной части извлекается очередной элемент и вставляется на нужную позицию в отсортированной
 части, в результате чего отсортированная часть списка увеличивается, а неотсортированная уменьшается. 
 Так происходит, пока не исчерпан набор входных данных  и не отсортированы все элементы.
'''

a = []
n = len(a)

for i in range(1, n):
    elem = a[i]  # берем первый элемент из неотсортированной части списка
    j = i

    # пока элемент слева существует и больше нашего текущего элемента
    while j >= 1 and a[j - 1] > elem:
        # смещаем j-й элемент отсортированной части вправо
        a[j] = a[j - 1]
        # сами идём влево, дальше ищем место для нашего текущего элемента
        j -= 1

    # нашли место для нащего текущего элемента из неотсортированной части
    # и вставляем его на индекс j в отсортированной части
    a[j] = elem

print(a)

#Быстрая сортировка
'''
Во многом идея быстрой сортировки такая же, как у алгоритма сортировки слиянием. 
Выберем некоторый элемент q, называемый барьерным элементом. Разобьем массив на две части,
переупорядочив его элементы. В первой части соберем элементы, меньшие или равные q, 
а во второй части — большие или равные q. Теперь достаточно отсортировать обе части, 
после чего выполнить их конкатенацию безо всякого дополнительного слияния.
'''
import random
b = []
def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return quicksort(L) + M + quicksort(R)
print(quicksort(b))
