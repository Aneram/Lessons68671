# import random as r
#
# card = ["❤️", "♦️", "♣️", "♠️", "⭐"]
# card_random = ["❤️", "♦️", "♣️", "♠️", "⭐"]
# r.shuffle(card)
# sum = 0
# while card_random != card:
#     r.shuffle(card)
#     print(card)
#     sum = sum + 1
# print(card_random)
# print(sum)

import tkinter as tk
import random as r

colors = ["aquamarine", "blue3", "black", "blue violet", "chartreuse", "dark red",
         "DeepPink", "goldenrod1", "grey18", "OrangeRed1", "salmon", "SlateBlue2", "snow",
         "SpringGreen", "violet red", "SteelBlue1", "red", "purple3", "PeachPuff", "OliveDrab"]
fg_color = r.choice(colors)
bg_color = r.choice(colors)
root = tk.Tk()

root.title("Привітання")
root.geometry("800x500")

label = tk.Label(root, text="Напишить своє чудове ім'я!",
                 font=("Arial", 16),fg=fg_color, bg=bg_color)


label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

greeting_label = tk.Label(root, text="", font=("Arial", 16))
greeting_label.pack(pady=20)

def say_hello(event=None):  # event=None дозволяє викликати і з кнопки, і через Enter
    name = entry.get()
    if name.strip():  # перевірка, що щось введено
        fg_color = r.choice(colors)
        bg_color = r.choice(colors)
        greeting_label.config(text=f"Вітаю, {name}! Ваше ім'я схоже на ім'я яке може бути лише в чудової людини!!!", fg=fg_color, bg=bg_color)

magic_button = tk.Button(root, text="🪄 Магічна зміна кольору", font=("Arial", 14), command=say_hello)
magic_button.pack(pady=10)

entry.bind("<Return>", say_hello)

root.mainloop()