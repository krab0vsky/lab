'''Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
Ввод данных из файла с контролем правильности ввода. 
Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами. 
Для GUI и визуализации использовать библиотеку tkinter.
Объекты – звезды
Функции:	сегментация
визуализация
раскраска
перемещение на плоскости
'''
import tkinter as tk
from tkinter import ttk

class Star:
    def __init__(self, name, x, y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
    def visualize(self, canvas): self.canvas_id = canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill=self.color)
    def move(self, dx, dy, canvas):
        self.x += dx
        self.y += dy
        canvas.coords(self.canvas_id, self.x - 5, self.y - 5, self.x + 5, self.y + 5)
class StarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Визуализация звезд")
    
        self.canvas = tk.Canvas(master, width=600, height=400, bg='black')
        self.canvas.pack()

        self.name_label = tk.Label(master, text="Имя:")
        self.name_label.place(x=20,y=420)
        self.name_entry = tk.Entry(master)
        self.name_entry.place(x=20,y=440)

        self.x_label = tk.Label(master, text="X Координата:")
        self.x_label.place(x=20,y=475)
        self.x_entry = tk.Entry(master)
        self.x_entry.place(x=20,y=495)

        self.y_label = tk.Label(master, text="Y Координата:")
        self.y_label.place(x=20,y=530)
        self.y_entry = tk.Entry(master)
        self.y_entry.place(x=20,y=550)

        self.color_label = tk.Label(master, text="Цвет:")
        self.color_label.place(x=20,y=575)
        self.color_entry = tk.Entry(master)
        self.color_entry.place(x=20,y=595)

        self.add_button = tk.Button(master, text="Добавить звезду", command=self.add_star)
        self.add_button.place(x=20,y=630)
        self.selected_star_label = tk.Label(master, text="Выбрать звезду:")
        self.selected_star_label.place(x=220,y=420)
        self.star_selector = ttk.Combobox(master)
        self.star_selector.place(x=220,y=440)

        self.dx_label = tk.Label(master, text="Move X (dx):")
        self.dx_label.place(x=220,y=475)
        self.dx_entry = tk.Entry(master)
        self.dx_entry.place(x=220,y=495)

        self.dy_label = tk.Label(master, text="Move Y (dy):")
        self.dy_label.place(x=220,y=530)
        self.dy_entry = tk.Entry(master)
        self.dy_entry.place(x=220,y=550)

        self.move_button = tk.Button(master, text="Передвинуть", command=self.move_star)
        self.move_button.place(x=220,y=595)

        self.segment_button = tk.Button(master, text="Сегменты", command=self.segment_stars)
        self.segment_button.place(x=420,y=440)

        self.segment_output = tk.Text()
        self.segment_output.place(x=420,y=475,width= 150,height=200)

        self.stars = []

    def add_star(self):
        name = self.name_entry.get()
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            color = self.color_entry.get()
            new_star = Star(name, x, y, color)
            self.stars.append(new_star)
            new_star.visualize(self.canvas)
            self.update_star_selector()
            self.name_entry.delete(0, tk.END)
            self.x_entry.delete(0, tk.END)
            self.y_entry.delete(0, tk.END)
            self.color_entry.delete(0, tk.END)

        except ValueError:
            print("Неверный ввод")
    def update_star_selector(self):
        star_names = [star.name for star in self.stars]
        self.star_selector['values'] = star_names
        if star_names:
            self.star_selector.current(0)  
    def move_star(self):
        try:
            dx = float(self.dx_entry.get())
            dy = float(self.dy_entry.get())
            selected_star_name = self.star_selector.get()
            selected_star = next((star for star in self.stars if star.name == selected_star_name), None)
            if selected_star:
                selected_star.move(dx, dy, self.canvas)
            self.dx_entry.delete(0, tk.END)
            self.dy_entry.delete(0, tk.END)
        except ValueError:
            print("Неверный ввод")
    def segment_stars(self):
        quadrants = {1: [], 2: [], 3: [], 4: []}
        for star in self.stars:
            if star.x >= 0 and star.y >= 0:
                quadrants[1].append(star)
            elif star.x < 0 and star.y >= 0:
                quadrants[2].append(star)
            elif star.x < 0 and star.y < 0:
                quadrants[3].append(star)
            elif star.x >= 0 and star.y < 0:
                quadrants[4].append(star)
        output = ""
        for quadrant, stars in quadrants.items():
            output += f"Квадрат {quadrant}: {[star.name for star in stars]}\n"
        self.segment_output.delete(1.0, tk.END) 
        self.segment_output.insert(tk.END, output)
root = tk.Tk()
root.geometry("600x800")
root.resizable(False,False)
app = StarApp(root)
root.mainloop()