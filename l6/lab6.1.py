'''Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.
Вариант 19. Для участия в команде тренер отбирает 5 мальчиков из 10. Вывести все возможные варианты состава команды.'''
from itertools import combinations
import timeit
boys = ["Иван", "Петр", "Сергей", "Алексей", "Дмитрий", "Максим", "Андрей", "Константин", "Виктор", "Никита"]
def m1(boys):
    teams = []
    n = len(boys)
    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                for p in range(m + 1, n):
                    for q in range(p + 1, n):
                        team = (boys[i], boys[j], boys[m], boys[p], boys[q])
                        teams.append(team)
    return teams

def m2(boys):
    teams = list(combinations(boys,5))
    return teams
ch = 0
while True:
    print("С чем работаем\n1-Заранее сгенерированный список\n2-Заполнить самому")
    ch = int(input("Ваш выбор: "))
    if ch == 1 or ch == 2:
        break
    else:
        print("Неверный выбор")

if ch == 2:
    boys = []
    for i in range(10):
        boys.append(input("Введите имя: "))
algorithmic_time = timeit.timeit('m1(boys)', globals=globals(), number=1000)
itertools_time = timeit.timeit('m2(boys)', globals=globals(), number=1000)
print(f"Алгоритмически\n{m1(boys)}")
print(f"Время выполнения алгоритмического подхода: {algorithmic_time:.6f} секунд")
print(f"Функциями питона\n{m2(boys)}")
print(f"Время выполнения подхода с itertools: {itertools_time:.6f} секунд")