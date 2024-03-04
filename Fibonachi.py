'''
Вычисление n-го числа ряда Фибоначчи
'''
from math import sqrt
fib_dict = {0: 0, 1: 1}
n = int(input())
def fibonacci1(n):
    """
    Итерационный подход нахождения чисел Фибоначчи
    """
    if n not in fib_dict:
        fib_dict[n] = fibonacci1(n-1) + fibonacci1(n-2)
    return fib_dict[n]

def fibonacci2(n):
    """
    Использование формулы Бине для нахождения чисел Фибоначчи
    """
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return int((phi**n - psi**n) / sqrt(5))


print(fibonacci2(n))
print(fibonacci1(n))




