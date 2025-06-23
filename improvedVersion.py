import random
import tkinter as tk
from tkinter import messagebox, font

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("21 Number Game")
        self.master.geometry("800x600")
        self.master.configure(bg='#f0f0f0')
        
        # Configure fonts
        self.title_font = font.Font(family='Helvetica', size=24, weight='bold')
        self.button_font = font.Font(family='Helvetica', size=16)
        self.entry_font = font.Font(family='Helvetica', size=18)
        self.text_font = font.Font(family='Helvetica', size=16)
        
        self.level = None
        self.n_list = []
        self.current_frame = None
        self.create_welcome_screen()

    def clear_window(self):
        if self.current_frame:
            self.current_frame.destroy()

    def create_welcome_screen(self):
        self.clear_window()
        self.current_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.current_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

        tk.Label(self.current_frame, text="Welcome to the 21 Number Game", 
                font=self.title_font, bg='#f0f0f0').pack(pady=30)
        
        rules_btn = tk.Button(self.current_frame, text="Show Rules", 
                            font=self.button_font, command=self.show_rules,
                            bg='#4CAF50', fg='white', padx=20, pady=10)
        rules_btn.pack(pady=20)
        
        tk.Label(self.current_frame, text="Choose your level (1, 2, or 3):", 
               font=self.text_font, bg='#f0f0f0').pack(pady=10)
        
        self.level_entry = tk.Entry(self.current_frame, font=self.entry_font, 
                                  justify='center', width=10)
        self.level_entry.pack(pady=10)
        
        start_btn = tk.Button(self.current_frame, text="Start Game", 
                            font=self.button_font, command=self.start_game,
                            bg='#2196F3', fg='white', padx=20, pady=10)
        start_btn.pack(pady=30)

    def show_rules(self):
        rules = (
            "The rules are:\n"
            "1. You can enter 1-3 numbers (space-separated)\n"
            "2. The first number must be 1\n"
            "3. Numbers must be consecutive\n"
            "4. If you reach 21 on your turn, you lose"
        )
        messagebox.showinfo("Game Rules", rules)

    def start_game(self):
        level = self.level_entry.get().lower()
        if level in ['1', '2', '3', 'one', 'two', 'three']:
            self.level = int(level) if level.isdigit() else {'one':1, 'two':2, 'three':3}[level]
            self.create_turn_selection_screen()
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid level (1, 2, or 3).")

    def create_turn_selection_screen(self):
        self.clear_window()
        self.current_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.current_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

        tk.Label(self.current_frame, text="Select who goes first:", 
                font=self.title_font, bg='#f0f0f0').pack(pady=30)
        
        first_btn = tk.Button(self.current_frame, text="I go first", 
                            font=self.button_font,
                            command=lambda: self.create_player_turn_screen(True),
                            bg='#FF9800', fg='white', padx=20, pady=15, width=20)
        first_btn.pack(pady=20)
        
        second_btn = tk.Button(self.current_frame, text="Computer goes first", 
                             font=self.button_font,
                             command=lambda: self.create_player_turn_screen(False),
                             bg='#FF9800', fg='white', padx=20, pady=15, width=20)
        second_btn.pack(pady=20)
        
        back_btn = tk.Button(self.current_frame, text="Back", 
                           font=self.button_font, command=self.create_welcome_screen,
                           bg='#607D8B', fg='white', padx=20, pady=10)
        back_btn.pack(pady=30)

    def create_player_turn_screen(self, is_player_first):
        self.clear_window()
        self.current_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.current_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        self.n_list = []
        self.player_first = is_player_first
        
        if not is_player_first:
            self.computer_turn(is_start=True)
        
        self.create_player_turn_content()

    def create_player_turn_content(self):
        for widget in self.current_frame.winfo_children():
            widget.destroy()
        
        # Show game status
        status = f"Numbers so far: {self.n_list}" if self.n_list else "Numbers so far: None"
        tk.Label(self.current_frame, text=status, font=self.text_font, 
                bg='#f0f0f0').pack(pady=20)
        
        # Input field with instructions
        tk.Label(self.current_frame, 
                text="Enter 1-3 consecutive numbers (space-separated):\nFirst number must be 1 if starting",
                font=self.text_font, bg='#f0f0f0').pack(pady=10)
        
        self.numbers_entry = tk.Entry(self.current_frame, font=self.entry_font, 
                                    justify='center', width=30)
        self.numbers_entry.pack(pady=10)
        
        submit_btn = tk.Button(self.current_frame, text="Submit", 
                             font=self.button_font, command=self.handle_player_move,
                             bg='#4CAF50', fg='white', padx=20, pady=10)
        submit_btn.pack(pady=30)
        
        back_btn = tk.Button(self.current_frame, text="Back", 
                           font=self.button_font, command=self.create_turn_selection_screen,
                           bg='#607D8B', fg='white', padx=20, pady=10)
        back_btn.pack(pady=10)

    def handle_player_move(self):
        try:
            # Get and validate input
            input_text = self.numbers_entry.get().strip()
            if not input_text:
                raise ValueError("Please enter at least one number")
            
            numbers = list(map(int, input_text.split()))
            n = len(numbers)
            
            if n < 1 or n > 3:
                raise ValueError("You must enter 1-3 numbers")
            
            if not self.n_list and numbers[0] != 1:
                raise ValueError("First number must be 1")
            
            if self.n_list and numbers[0] != self.n_list[-1] + 1:
                raise ValueError("Numbers must be consecutive")
            
            # Add player's numbers
            self.n_list.extend(numbers)
            
            # Check if player lost
            if self.n_list[-1] >= 21:
                self.lose()
                return
            
            # Clear input field for next turn
            self.numbers_entry.delete(0, tk.END)
            
            # Computer's turn after player
            self.computer_turn()
            
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

    def computer_turn(self, is_start=False):
        last_number = self.n_list[-1] if self.n_list else 0
        
        if self.level == 1:
            comp = random.randint(1, 3)
        elif self.level == 2:
            comp = 4 - (len(self.n_list) % 4) if not is_start else random.randint(1, 3)
        elif self.level == 3:
            if not is_start:
                near = self.n_list[-1] + (4 - (self.n_list[-1] % 4)) if self.n_list[-1] >= 4 else 4
                comp = near - self.n_list[-1]
                comp = 3 if comp == 4 else comp
            else:
                comp = random.randint(1, 3)
        
        # Add computer's numbers
        for i in range(1, comp+1):
            self.n_list.append(last_number + i)
        
        # Update status label
        for widget in self.current_frame.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text").startswith("Computer played"):
                widget.destroy()
        
        status = f"Computer played: {self.n_list[-comp:]}\nNumbers so far: {self.n_list}"
        tk.Label(self.current_frame, text=status, font=self.text_font, 
                bg='#f0f0f0').pack(pady=20)
        
        # Check if computer lost
        if self.n_list[-1] >= 21:
            self.won()

    def won(self):
        messagebox.showinfo("Congratulations", "YOU WON! Thank you for playing.")
        self.create_welcome_screen()

    def lose(self):
        messagebox.showinfo("Game Over", "YOU LOSE! Better luck next time.")
        self.create_welcome_screen()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
