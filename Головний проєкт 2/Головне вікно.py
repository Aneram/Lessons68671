import tkinter as tk

# Створюємо головне вікно
root = tk.Tk()
root.title("Мій Проєкт по 3 Модулю")
root.geometry("500x500")

# Створюємо меню
menubar = tk.Menu(root)

# Додаємо перший пункт меню
file_menu1 = tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="Цікаві кнопки")
file_menu1.add_command(label="Зміна теми")
file_menu1.add_command(label="Вийти", command=root.quit)

# Додаємо другий пункт меню
file_menu2 = tk.Menu(menubar, tearoff=0)
file_menu2.add_command(label="Автоклікер")
file_menu2.add_command(label="Конвентер Валют")
file_menu2.add_command(label="Фізичний Калькулятор")
file_menu2.add_command(label="Гра вибор")

# Додаємо два підменю в головне меню
menubar.add_cascade(label="Допомога й Знання", menu=file_menu1)
menubar.add_cascade(label="Програми", menu=file_menu2)

# Додаємо головне меню у вікно
root.config(menu=menubar)

root.mainloop()