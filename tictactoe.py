import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.resizable(False, False)
        self.master.configure(bg="#2c3e50")
        self.current_player = "X"
        
        self.title_label = tk.Label(master, text="Tic-Tac-Toe", font=('Arial', 20, 'bold'), fg="#ecf0f1", bg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", font=('Arial', 20), width=5, height=2, relief="solid", 
                                   bg="#ecf0f1", activebackground="#bdc3c7", 
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                row.append(button)
            self.buttons.append(row)
        
        self.bottom_frame = tk.Frame(master, bg="#2c3e50")
        self.bottom_frame.grid(row=4, column=0, columnspan=3, pady=10)

        self.reset_button = tk.Button(self.bottom_frame, text="Reset Game", command=self.reset_game, bg="#f39c12", font=('Arial', 12, 'bold'))
        self.reset_button.grid(row=0, column=0, padx=10)

        self.x_score = 0
        self.o_score = 0
        self.score_label = tk.Label(self.bottom_frame, text="X: 0 | O: 0", font=('Arial', 14, 'bold'), fg="#ecf0f1", bg="#2c3e50")
        self.score_label.grid(row=0, column=1)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col].config(fg="#FF5733" if self.current_player == "X" else "#1E90FF")
            
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.update_score()
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        if all(self.buttons[row][c]['text'] == self.current_player for c in range(3)):
            return True
        
        if all(self.buttons[r][col]['text'] == self.current_player for r in range(3)):
            return True
        
        if row == col and all(self.buttons[i][i]['text'] == self.current_player for i in range(3)):
            return True
        
        if row + col == 2 and all(self.buttons[i][2-i]['text'] == self.current_player for i in range(3)):
            return True
        
        return False

    def is_board_full(self):
        return all(self.buttons[i][j]['text'] != "" 
                   for i in range(3) for j in range(3))

    def update_score(self):
        if self.current_player == "X":
            self.x_score += 1
        else:
            self.o_score += 1
        
        self.score_label.config(text=f"X: {self.x_score} | O: {self.o_score}", fg="#ecf0f1")
        self.current_player = "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.buttons[i][j].config(bg="#ecf0f1", fg="black")
        
        self.current_player = "X"

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
