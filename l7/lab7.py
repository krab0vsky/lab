'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса. 
Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.
Вариант 19. Для участия в команде тренер отбирает 5 мальчиков из 10. Вывести все возможные варианты состава команды.
Условие ограничения: Сумма мастерства в команде должна быть нечетной
Функция целевой: Сумма мастерства в команде должна быть максимальной.
'''
import tkinter as tk
from tkinter import scrolledtext
from itertools import combinations

def m2(boys, masteries):
    teams = []
    for team in combinations(boys, 5):
        team_masteries = [masteries[boys.index(x)] for x in team]
        if sum(team_masteries) % 2 == 1:
            teams.append((team, team_masteries))
    return teams

def generate_teams():
    try:
        boys = entry_boys.get().split(',')
        masteries = list(map(int, entry_masteries.get().split(',')))
        
        if len(boys) != 10 or len(masteries) != 10:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Ошибка: должно быть 10 мальчиков и 10 значений мастерства.")
            return
        
        teams = m2(boys, masteries)
        
        output_text.delete(1.0, tk.END)
        if not teams:
            output_text.insert(tk.END, "Нет команд с нечетной суммой мастерства.")
        else:
            max_team = max(teams, key=lambda x: sum(x[1])) 
            for team, team_masteries in teams:
                output_text.insert(tk.END, f"Команда: {team}, Мастерство: {team_masteries}, Сумма: {sum(team_masteries)}\n")
            output_text.insert(tk.END, "\nКоманда с максимальной суммой мастерства:\n")
            output_text.insert(tk.END, f"Команда: {max_team[0]}, Мастерство: {max_team[1]}, Сумма: {sum(max_team[1])}\n")
    except:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Ошибка: неверный формат ввода.")
        return

root = tk.Tk()
root.title("Отбор команды")

tk.Label(root, text="Введите 10 мальчиков (через запятую):").pack()
entry_boys = tk.Entry(root, width=50)
entry_boys.pack()

tk.Label(root, text="Введите мастерство для каждого мальчика (через запятую):").pack()
entry_masteries = tk.Entry(root, width=50)
entry_masteries.pack()

btn_generate = tk.Button(root, text="Сгенерировать команды", command=generate_teams)
btn_generate.pack()

output_text = scrolledtext.ScrolledText(root, width=60, height=20)
output_text.pack()

root.mainloop()
