import tkinter as tk
from tkinter import messagebox
import random
import copy

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики-нулики")
        self.root.configure(bg="#f0e68c")  # світло-жовтий фон
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                command=lambda row=i, col=j: self.player_move(row, col),
                                bg="#fffacd")
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

        restart_btn = tk.Button(self.root, text="Перезапустити гру", font=("Arial", 14), command=self.reset_game,
                                bg="#add8e6")
        restart_btn.grid(row=3, column=0, columnspan=3, pady=10)

    def player_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = "X"
            self.animate_button(row, col, "X", "red")
            if self.check_winner():
                messagebox.showinfo("Гра завершена", "Ви виграли!")
            elif self.is_draw():
                messagebox.showinfo("Гра завершена", "Нічия!")
            else:
                self.root.after(500, self.computer_move)

    def computer_move(self):
        best_score = -float("inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = "O"
            self.animate_button(row, col, "O", "green")
            if self.check_winner():
                messagebox.showinfo("Гра завершена", "Комп'ютер виграв!")
            elif self.is_draw():
                messagebox.showinfo("Гра завершена", "Нічия!")

    def minimax(self, board, depth, is_maximizing):
        if self.evaluate(board) == 1:
            return 1
        elif self.evaluate(board) == -1:
            return -1
        elif self.is_full(board):
            return 0

        if is_maximizing:
            best = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        value = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best = max(best, value)
            return best
        else:
            best = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        value = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best = min(best, value)
            return best

    def evaluate(self, board):
        lines = board + list(zip(*board)) + [
            [board[i][i] for i in range(3)],
            [board[i][2 - i] for i in range(3)]
        ]
        for line in lines:
            if list(line) == ["O"] * 3:
                return 1
            elif list(line) == ["X"] * 3:
                return -1
        return 0

    def is_full(self, board):
        return all(cell != "" for row in board for cell in row)

    def check_winner(self):
        return self.evaluate(self.board) != 0

    def is_draw(self):
        return self.is_full(self.board) and self.evaluate(self.board) == 0

    def animate_button(self, row, col, symbol, color):
        btn = self.buttons[row][col]
        btn.config(state="disabled")
        btn.config(text="", fg=color)
        def fade_in(step=0):
            shades = ["#ffffff", "#f0f0f0", "#e0e0e0", "#d0d0d0", "#c0c0c0", color]
            if step < len(shades):
                btn.config(fg=shades[step])
                self.root.after(30, lambda: fade_in(step + 1))
            else:
                btn.config(text=symbol, fg=color)
        fade_in()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()