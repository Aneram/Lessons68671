import tkinter as tk

# Створюємо головне вікно
root = tk.Tk()
root.title("Мій додаток")

# Створюємо меню
menubar = tk.Menu(root)

# Додаємо перший пункт меню
file_menu1 = tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="Відкрити")
file_menu1.add_command(label="Зберегти")
file_menu1.add_command(label="Вийти", command=root.quit)

# Додаємо другий пункт меню
file_menu2 = tk.Menu(menubar, tearoff=0)
file_menu2.add_command(label="Копіювати")
file_menu2.add_command(label="Вирізати")
file_menu2.add_command(label="Вставити")

# Додаємо два підменю в головне меню
menubar.add_cascade(label="Файл", menu=file_menu1)
menubar.add_cascade(label="Редагувати", menu=file_menu2)

# Додаємо головне меню у вікно
root.config(menu=menubar)

root.mainloop()
