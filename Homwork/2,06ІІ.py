import tkinter as tk
from tkinter import messagebox

# Дані вікторини
questions = [
    {
        "text": "Чому лід плаває?",
        "options": ["a) Важчий за воду", "b) Менша густина", "c) Гарячий всередині"],
        "answer": "b"
    },
    {
        "text": "Для чого легені?",
        "options": ["a) Травлення їжі", "b) Регулювання температури", "c) Газообмін у тілі"],
        "answer": "c"
    },
    {
        "text": "5² = ?",
        "options": ["a) 10", "b) 25", "c) 52"],
        "answer": "b"
    }
]

current_question = 0
score = 0

# Обробка відповіді
def check_answer(option):
    global current_question, score
    if option.startswith(questions[current_question]["answer"]):
        score += 1

    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Результат", f"Ви набрали {score} з {len(questions)} балів!")
        root.destroy()

# Показати поточне питання
def show_question():
    question_label.config(text=questions[current_question]["text"])
    for i, btn in enumerate(option_buttons):
        btn.config(text=questions[current_question]["options"][i])

# Вікно
root = tk.Tk()
root.title("Вікторина")
root.geometry("500x300")
root.config(bg="#e1f5fe")  # Блакитний фон

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450, bg="#e1f5fe")
question_label.pack(pady=20)

option_buttons = []
for _ in range(3):
    btn = tk.Button(root, text="", font=("Arial", 14), width=40, command=lambda b=_: check_answer(option_buttons[b].cget("text")))
    btn.pack(pady=5)
    option_buttons.append(btn)

show_question()
root.mainloop()
