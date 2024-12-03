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

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    
def recursion(n):
    if n == 0 or n == 1:
        return 1
    else: return ((-1)**n)*(recursion(n-1)/(factorial(2*n)*recursion(n-2)+2))

def iteration(n):
    if n == 0 or n == 1:
        return 1
    else:
        results = [1, 1]
        for i in range(2, n + 1):
            F_i = ((-1) ** i) * (results[i - 1] / (math.factorial(2 * i) * results[i - 2] + 2))
            results.append(F_i)  
        return results[n]
n = int(input("Введите n: "))
recursion_time = timeit.timeit(lambda: recursion(n), number=1000)
iteration_time = timeit.timeit(lambda: iteration(n), number=1000)
print(f"Результат рекурсии для n={n}: {recursion(n)}")
print(f"Результат итерации для n={n}: {iteration(n)}")
print(f"Время выполнения рекурсии: {recursion_time:.6f} секунд")
print(f"Время выполнения итерации: {iteration_time:.6f} секунд")