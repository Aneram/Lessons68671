import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# Питання: текст, варіанти, правильна відповідь, шлях до зображення
questions = [
    {
        "text": "Чому лід плаває?",
        "options": ["a) Важчий за воду", "b) Менша густина", "c) Гарячий всередині"],
        "answer": "b",
        "image": "ice.png"  # додай файл ice.png у папку
    },
    {
        "text": "Для чого легені?",
        "options": ["a) Травлення їжі", "b) Регулювання температури", "c) Газообмін у тілі"],
        "answer": "c",
        "image": "lungs.png"
    },
    # додай більше питань за потреби
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Вікторина")
        self.score = 0
        self.q_index = 0

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack()

        self.buttons = []
        for i in range(3):
            btn = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.show_question()

    def show_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=q["text"])

        for i, option in enumerate(q["options"]):
            self.buttons[i].config(text=option)

        img = Image.open(q["image"])
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def check_answer(self, choice_index):
        selected = questions[self.q_index]["options"][choice_index][0]
        if selected == questions[self.q_index]["answer"]:
            self.score += 1
            messagebox.showinfo("Результат", "Правильно!")
        else:
            messagebox.showerror("Результат", "Неправильно.")

        self.q_index += 1
        if self.q_index < len(questions):
            self.show_question()
        else:
            messagebox.showinfo("Гру завершено", f"Ваш результат: {self.score} з {len(questions)}")
            self.root.quit()

# Запуск
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
