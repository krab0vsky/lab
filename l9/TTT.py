import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog

def check_win(player):
    for i in range(3):
        if all(buttons[i * 3 + j]["text"] == player for j in range(3)):
            return True
        if all(buttons[i + j * 3]["text"] == player for j in range(3)):
            return True
    if all(buttons[i]["text"] == player for i in [0, 4, 8]):
        return True
    if all(buttons[i]["text"] == player for i in [2, 4, 6]):
        return True
    return False

def check_draw():
    return all(button["text"] != "" for button in buttons)

def button_click(row, col):
    global current_player
    index = row * 3 + col
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        if check_win(current_player):
            messagebox.showinfo("Победа!", f"Игрок {current_player} победил!")
            disable_buttons()
            game_over()
        elif check_draw():
            messagebox.showinfo("Ничья!", "Ничья!")
            disable_buttons()
            game_over()
        else:
            current_player = bot_player  
            label.config(text=f"Ход игрока: {current_player}")
            bot_move()  # Ход бота

def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

def get_empty_cells():
    return [i for i in range(9) if buttons[i]["text"] == ""]

def minimax(board, depth, is_maximizing):
    if check_win(bot_player):
        return 10 - depth
    if check_win(player_choice):
        return depth - 10
    if check_draw():
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in get_empty_cells():
            board[i]["text"] = bot_player
            eval = minimax(board, depth + 1, False)
            board[i]["text"] = ""
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in get_empty_cells():
            board[i]["text"] = player_choice
            eval = minimax(board, depth + 1, True)
            board[i]["text"] = ""
            min_eval = min(min_eval, eval)
        return min_eval

def bot_move():
    best_score = -float('inf')
    best_move = -1
    for i in get_empty_cells():
        buttons[i]["text"] = bot_player
        score = minimax(buttons, 0, False)
        buttons[i]["text"] = ""
        if score > best_score:
            best_score = score
            best_move = i

    if best_move != -1:
        buttons[best_move]["text"] = bot_player
        if check_win(bot_player):
            messagebox.showinfo("Победа!", f"Бот ({bot_player}) победил!")
            disable_buttons()
            game_over()
        elif check_draw():
            messagebox.showinfo("Ничья!", "Ничья!")
            disable_buttons()
            game_over()
        else:
            global current_player
            current_player = player_choice
            label.config(text=f"Ход игрока: {current_player}")

def game_over():
    result = messagebox.askyesno("Игра окончена", "Хотите сыграть ещё раз?")
    if result:
        get_player_choice()
    else:
        root.destroy()

def get_player_choice():
    global player_choice, current_player, bot_player
    root.withdraw()
    player_choice = simpledialog.askstring("Выбор игрока", "Выберите, чем хотите играть (X или O):", initialvalue="X").upper()
    if player_choice not in ("X", "O"):
        messagebox.showerror("Ошибка", "Неверный ввод. Пожалуйста, введите X или O.")
        get_player_choice()

        # Установка значений для игрока и бота
    if player_choice == "O":
        bot_player = "X"
    else:
        bot_player = "O"

    current_player = player_choice
    root.deiconify()
    start_new_game()


def start_new_game():
    global current_player
    for button in buttons:
        button['text'] = ""
        button.config(state=tk.NORMAL)
    label.config(text=f"Ход игрока: {current_player}")


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Крестики-нолики")
root.configure(bg="lightblue") 
buttons = []
bot_player = "X"  

label = tk.Label(root, text=f"Ход игрока: ", font=("Helvetica", 16), bg="lightblue") 
label.grid(row=0, column=0, columnspan=3, pady=10)

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=5, font=("Helvetica", 32),
                           command=lambda row=i, col=j: button_click(row, col), bg="white")  
        button.grid(row=i + 1, column=j, padx=5, pady=5)
        buttons.append(button)

get_player_choice()
center_window(root)  
root.mainloop()
