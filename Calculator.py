import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()
        
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def create_widgets(self):
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), bd=5, insertwidth=4, width=15, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=('Arial', 18), bd=5, padx=10, pady=10, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew")

        clear_btn = tk.Button(self.root, text="C", font=('Arial', 18), bd=5, padx=10, pady=10, command=lambda: self.on_button_click("C"))
        clear_btn.grid(row=1, column=3, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif char == 'C': # Clear Button
            self.result_var.set("0")
        else:
            if self.result_var.get() == "0" or self.result_var.get() == "Error":
                self.result_var.set(char)
            else:
                self.result_var.set(self.result_var.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()