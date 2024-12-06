'''Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.
Вариант 19. Для участия в команде тренер отбирает 5 мальчиков из 10. Вывести все возможные варианты состава команды.
Условие ограничения: Сумма мастерства в команде должна быть нечетной
Функция целевой: Сумма мастерства в команде должна быть максимальной.
'''


from itertools import combinations
import timeit
boys = ["Иван", "Петр", "Сергей", "Алексей", "Дмитрий", "Максим", "Андрей", "Константин", "Виктор", "Никита"]
masteries = [3, 2, 1, 1, 2, 3, 3, 3, 2, 1]
def m1(boys, masteries):
    teams = []
    n = len(boys)
    for i in range(n):
        for j in range(i + 1, n):
            for m in range(j + 1, n):
                for p in range(m + 1, n):
                    for q in range(p + 1, n):
                        team = (boys[i], boys[j], boys[m], boys[p], boys[q])
                        team_masteries = [masteries[boys.index(x)] for x in team]
                        if sum(team_masteries) % 2 == 1:
                            teams.append((team, team_masteries))  
    return teams
def m2(boys, masteries):
    teams = []
    for team in combinations(boys, 5):
        team_masteries = [masteries[boys.index(x)] for x in team]
        if sum(team_masteries) % 2 == 1:
            teams.append((team, team_masteries))
    return teams
def target_function(teams):
    best_team = None
    best_mastery_sum = 0
    for team, team_masteries in teams:
        mastery_sum = sum(team_masteries)
        if mastery_sum > best_mastery_sum:
            best_mastery_sum = mastery_sum
            best_team = (team, team_masteries)
    return best_team

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
    masteries = []
    for i in range(10):
        boys.append(input("Введите имя: "))
        masteries.append(int(input("Введите мастерство: ")))

algorithmic_time = timeit.timeit('m1(boys, masteries)', globals=globals(), number=1000)
itertools_time = timeit.timeit('m2(boys, masteries)', globals=globals(), number=1000)
print("Сумма мастерства в команде должна быть нечетной.")
print("Алгоритмически:")
teams_m1 = m1(boys, masteries)
for team, team_masteries in teams_m1:
    print(f"Команда: {team}, Мастерство: {team_masteries}")
print(f"Время выполнения алгоритмического подхода: {algorithmic_time:.6f} секунд")
print("Функциями питона:")
teams_m2 = m2(boys, masteries)
for team, team_masteries in teams_m2:
    print(f"Команда: {team}, Мастерство: {team_masteries}")
print(f"Время выполнения подхода с itertools: {itertools_time:.6f} секунд")
best_team = target_function(teams_m1)
if best_team:
    team, team_masteries = best_team
    print(f"Оптимальная команда: {team}, Мастерство: {team_masteries}, Сумма мастерства: {sum(team_masteries)}")
else:
    print("Не удалось найти оптимальную команду.")
print(f"Количество возможных команд: {len(teams_m1)}")
