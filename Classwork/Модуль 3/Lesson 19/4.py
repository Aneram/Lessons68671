import tkinter as tk

# Створюємо головне вікно
root = tk.Tk()
root.title("Додаток художника")

# Створюємо меню
menubar = tk.Menu(root)

# Додаємо перший пункт меню
file_menu1 = tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="Червоний", command=)
file_menu1.add_command(label="Синій")
file_menu1.add_command(label="Чорний")
file_menu1.add_command(label="Білий")
file_menu1.add_command(label="Зелений")
file_menu1.add_command(label="Фіолетовий")
file_menu1.add_command(label="Жовтий")
file_menu1.add_command(label="Рожевий")
file_menu1.add_command(label="Вийти", command=root.quit)

# Підв'язання до кольору щоб працювало

def red():
    root.config(bg="red")
def blue():
    root.config(bg="blue")
def green():
    root.config(bg="green")
def red():
    root.config(bg="red")
def red():
    root.config(bg="red")
def red():
    root.config(bg="red")
def red():
    root.config(bg="red")
def red():
    root.config(bg="red")


# Додаємо два підменю в головне меню
menubar.add_cascade(label="Вибір кольору", menu=file_menu1)


# Додаємо головне меню у вікно
root.config(menu=menubar)

#color_menu.add_command(label="Зелений", command=change_to_green)

root.mainloop()

