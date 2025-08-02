import tkinter as tk
from tkinter import messagebox
import time
import keyboard
import mouse

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
        while running:
            mouse.click()  # тут потім додамо клацання миші замість print
            time.sleep(delay)  # затримка між кліками
            # функція знову викликає сама себе

def exit_app():

# тут буде завершення програми
    root.destroy()

# def start_clicker():
#     # тут буде запуск клікера
#     messagebox.showinfo("Auto Clicker", "Auto Clicker запушено. Натисни 'ESC' щоб зупинити.")


def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

def exit_app():
    print("STOP")
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    root.destroy()

root = tk.Tk()
root.bind('i', show_info)

root.title("Привітання")
root.geometry("570x200")
root.configure(bg="pink")

label = tk.Label(root, text="Автоклікер! (для ледачих хто не хоче клікати)",
                 font=("Segoe Script", 16),fg="#9339E1", bg="pink")

label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# greeting_label = tk.Label(root, text="", font=("Arial", 16))
# greeting_label.pack(pady=20)

exit_button = tk.Button( text="Вийти", font=("SimSun", 14), bg="red", fg="black", width=10)
exit_button.pack(side="left", padx=30)

def exit_app():

    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    root.destroy() # Закриття вікна Tkinter

keyboard.add_hotkey('esc', exit_app)

start_button = tk.Button( text="Почати", font=("Mongolian Baiti", 14), bg="lime green", fg="black", width=10, command=start_clicker)
start_button.pack(side="right", padx=30)

root.mainloop()