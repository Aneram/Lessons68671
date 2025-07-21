

def exit_app():

# тут буде завершення програми
    root.destroy()


import tkinter as tk
from tkinter import messagebox
import time

running = False # змінна, що зберігатиме стан: програма зараз працює або ні
delay = 0 # змінна, що зберігатиме тривалість перерви після кожного кліку

def start_clicker():
    global running, delay  # "знаходимо" змінні, що існують поза функцією
    clicks_per_second = int(entry.get())
    delay = 1 / clicks_per_second  # рахуємо затримку між кліками
    messagebox.showinfo("Auto Clicker", "Auto Clicker розпочинає роботу. Натисни 'ESC' щоб зупинити.")
    running = True

# Запуск процесу кліків
    schedule_click()

def schedule_click():
    if running:
        print("Клац!")  # тут потім додамо клацання миші замість print
    time.sleep(delay)  # затримка між кліками
    schedule_click()  # функція знову викликає сама себе

def exit_app():

# тут буде завершення програми
    root.destroy()

# def start_clicker():
#     # тут буде запуск клікера
#     messagebox.showinfo("Auto Clicker", "Auto Clicker запушено. Натисни 'ESC' щоб зупинити.")


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

root = tk.Tk()
root.bind('i', show_info)

root.title("Привітання")
root.geometry("450x200")
root.configure(bg="pink")

label = tk.Label(root, text="Автоклікер! (для ледачих хто не хоче клікати)",
                 font=("Arial", 16),fg="#9339E1", bg="pink")

label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# greeting_label = tk.Label(root, text="", font=("Arial", 16))
# greeting_label.pack(pady=20)

exit_button = tk.Button( text="Вийти", font=("Arial", 14), bg="red", fg="black", width=10)
exit_button.pack(side="left", padx=30)

start_button = tk.Button( text="Почати", font=("Arial", 14), bg="lime green", fg="black", width=10, command=start_clicker)
start_button.pack(side="right", padx=30)

root.mainloop()