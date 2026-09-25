#PROGRAM TO CREATE A SIMPLE CALCULATOR USING TKINTER
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#202020")

        # String variable to track the expression
        self.expression = ""
        self.display_var = tk.StringVar()

        # Build UI Elements
        self.create_display()
        self.create_buttons()

    def create_display(self):
        """Creates the calculator screen field."""
        display_frame = tk.Frame(self.root, bg="#202020")
        display_frame.pack(expand=True, fill="both")

        entry = tk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            font=("Arial", 28, "bold"), 
            bg="#202020", 
            fg="#ffffff", 
            bd=0, 
            justify="right", 
            insertbackground="white"
        )
        entry.pack(expand=True, fill="both", padx=24, pady=10)

    def create_buttons(self):
        """Creates the grid layout for calculator buttons."""
        buttons_frame = tk.Frame(self.root, bg="#202020")
        buttons_frame.pack(expand=True, fill="both")

        # Grid configuration for uniform sizing
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

        # Layout mapping (Label, Row, Column)
        button_layout = {
            'C': (0, 0), '(': (0, 1), ')': (0, 2), '/': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '*': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3),
            '0': (4, 0), '.': (4, 1), '=': (4, 2)  # '=' spans 2 columns
        }

        for text, grid_pos in button_layout.items():
            # Apply distinct color palettes for styling
            if text in ['/', '*', '-', '+', '=']:
                bg_color, fg_color = "#ff9f0a", "#ffffff"  # Operator Accent
            elif text in ['C', '(', ')']:
                bg_color, fg_color = "#a5a5a5", "#000000"  # Top Utility Row
            else:
                bg_color, fg_color = "#333333", "#ffffff"  # Number Pad

            # Dynamic column spanning for the '=' button
            colspan = 2 if text == '=' else 1

            btn = tk.Button(
                buttons_frame, 
                text=text, 
                font=("Arial", 18), 
                bg=bg_color, 
                fg=fg_color, 
                bd=0, 
                activebackground="#555555",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=grid_pos[0], column=grid_pos[1], columnspan=colspan, sticky="nsew", padx=1, pady=1)

    def on_button_click(self, char):
        """Processes user input events."""
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                # Safe evaluation wrapper
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero.")
                self.expression = ""
            except Exception:
                messagebox.showerror("Error", "Invalid Expression.")
                self.expression = ""
        else:
            self.expression += str(char)
        
        self.display_var.set(self.expression)

if __name__ == "__main__":
    window = tk.Tk()
    app = Calculator(window)
    window.mainloop()