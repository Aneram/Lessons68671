import tkinter as tk

# Функції для зміни кольору фону

def change_to_red():

    root.config(bg="red")

def change_to_blue():

    root.config(bg="blue")

def change_to_green():

    root.config(bg="green")

def change_to_yellow():

    root.config(bg="yellow")

def change_to_purple():

    root.config(bg="purple")

def change_to_orange():

    root.config(bg="orange")


# Головне вікно
root = tk.Tk()
root.title("Додаток художника")
root.geometry("400x400")

# Створюємо меню
menubar = tk.Menu(root)

# Створюємо підменю
color_menu = tk.Menu(menubar, tearoff=0)
color_menu.add_command(label="Червоний", command=change_to_red)
color_menu.add_command(label="Синій", command=change_to_blue)
color_menu.add_command(label="Зелений", command=change_to_green)
color_menu.add_command(label="Жовтий", command=change_to_yellow)
color_menu.add_command(label="Фіолетовий", command=change_to_purple)
color_menu.add_command(label="Помаранчевий", command=change_to_orange)

# Додаємо підменю в головне меню
menubar.add_cascade(label="Вибір кольору", menu=color_menu)

# Додаємо головне меню до вікна
root.config(menu=menubar)

root.mainloop()