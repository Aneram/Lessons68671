import tkinter as tk

# Головне вікно
root = tk.Tk()
root.title("Простий редактор з панеллю інструментів")
root.geometry("400x400")

# Функції для кнопок
def new_file():
    print("Створено новий файл!")

def save_file():
    print("Збережено!")

def open_file():
    print("Відкрито!")

def cut_text():
    print("Вирізано текст!")

def copy_text():
    print("Скопійовано текст!")

def paste_text():
    print("Вставлено текст!")

# Створюємо фрейм для панелі інструментів
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)

# Кнопка "Нове"
new_button = tk.Button(toolbar, text="Нове", command=new_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

# Кнопка "Зберегти"
save_button = tk.Button(toolbar, text="Зберегти", command=save_file)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

# Кнопка "Відкрити"
open_button = tk.Button(toolbar, text="Відкрити", command=open_file)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

# Кнопка "Вирізати"
cut_button = tk.Button(toolbar, text="Вирізати", command=cut_text)
cut_button.pack(side=tk.LEFT, padx=2, pady=2)

# Кнопка "Копіювати"
copy_button = tk.Button(toolbar, text="Копіювати", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=2, pady=2)

# Кнопка "Вставити"
paste_button = tk.Button(toolbar, text="Вставити", command=paste_text)
paste_button.pack(side=tk.LEFT, padx=2, pady=2)

# Відображаємо панель інструментів
toolbar.pack(side=tk.TOP, fill=tk.X)

# Основний контент
content = tk.Text(root)
content.pack(expand=1, fill=tk.BOTH)

root.mainloop()
