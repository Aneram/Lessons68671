import tkinter as tk
import random

# Конфігурація гри
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20

DIRECTIONS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0)
}

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT + 60, bg="black")  # Трохи більша висота для рахунку та кнопки
        self.canvas.pack()

        self.score = 0
        self.game_over = False
        self.create_start_button()

        self.root.bind("<KeyPress>", self.change_direction)
        self.reset_game()

    def create_start_button(self):
        self.start_button = tk.Button(self.root, text="Почати заново", command=self.reset_game)
        self.start_button.pack()

    def reset_game(self):
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        self.update()

    def create_food(self):
        while True:
            food = (random.randint(0, WIDTH // CELL_SIZE - 1),
                    random.randint(0, HEIGHT // CELL_SIZE - 1))
            if food not in self.snake:
                return food

    def change_direction(self, event):
        new_dir = event.keysym
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir == "w" and self.direction != "Down":
            self.direction = "Up"
        elif new_dir == "s" and self.direction != "Up":
            self.direction = "Down"
        elif new_dir == "a" and self.direction != "Right":
            self.direction = "Left"
        elif new_dir == "d" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        head_x, head_y = self.snake[0]
        delta_x, delta_y = DIRECTIONS[self.direction]
        new_head = (head_x + delta_x, head_y + delta_y)

        # Перевірка переходу через стіни
        new_head = (new_head[0] % (WIDTH // CELL_SIZE), new_head[1] % (HEIGHT // CELL_SIZE))

        # Перевірка на зіткнення з тілом
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 10  # +10 балів за їжу
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        # Малюємо змійку
        for x, y in self.snake:
            self.draw_cell(x, y, "green")

        # Малюємо їжу
        fx, fy = self.food
        self.draw_cell(fx, fy, "red")

        # Виводимо рахунок
        self.canvas.create_text(
            WIDTH // 2, HEIGHT + 15,
            text=f"Рахунок: {self.score}",
            fill="white",
            font=("Arial", 14)
        )

        if self.game_over:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))

    def draw_cell(self, x, y, color):
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.draw()
            self.root.after(100, self.update)
        else:
            self.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Змійка з кнопкою та переходом через стіни")
    game = SnakeGame(root)
    root.mainloop()
