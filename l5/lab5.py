'''Задана рекуррентная функция. 
Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции 
рекурсивно и итерационно. Определить границы применимости 
рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной форме. 
Обязательное требование – минимизация времени выполнения и объема памяти.
19.	F(0) = 1, F(1) = 1, F(n) = (-1)n*(F(n–1) /(2n)!*F(n-2)+2), при n > 1
'''
import math
import timeit

def factorial(n, last_value=None):
    if n == 0 or n == 1:
        return 1
    else:
        current_value = n * factorial(n - 1, last_value)
        last_value = current_value
        return current_value
    
def recursion(n,sign=1,last_value=None):
    if n == 0 or n == 1:
        return 1
    else:
        current_value = sign * (recursion(n-1,-sign, last_value) / (factorial(2*n) * recursion(n-2,-sign, last_value) + 2))
        last_value = current_value
        return current_value

def iteration(n):
    if n == 0 or n == 1:
        return 1
    else:
        prev1 = 1
        prev2 = 1  
        last_value = 1  
        sign = 1
        for i in range(2, n + 1):
            last_value = sign * (prev1 / (math.factorial(2 * i) * prev2 + 2))
            prev2 = prev1
            prev1 = last_value
            sign *= -1
        return last_value
n = int(input("Введите n: "))
recursion_time = timeit.timeit(lambda: recursion(n), number=1000)
iteration_time = timeit.timeit(lambda: iteration(n), number=1000)
print(f"Результат рекурсии для n={n}: {recursion(n)}")
print(f"Результат итерации для n={n}: {iteration(n)}")
print(f"Время выполнения рекурсии: {recursion_time:.6f} секунд")
print(f"Время выполнения итерации: {iteration_time:.6f} секунд")    
