import tkinter as tk

class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.expression = ""
        self.result = 0

    def calculate(self):
        if self.expression == '+':
            return self.num1 + self.num2
        elif self.expression == '-':
            return self.num1 - self.num2
        elif self.expression == '*':
            return self.num1 * self.num2
        elif self.expression == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Error"
        else:
            return "Invalid Expression"

    def clear(self):
        self.num1 = 0
        self.num2 = 0
        self.expression = ""
        self.result = 0

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

calculator = Calculator()

# Add the display
display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge")
display.pack(pady=20)

# Button click event
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

# Function to clear the display
def button_clear():
    display.delete(0, tk.END)
    calculator.clear()

# Function to evaluate the expression
def button_equal():
    try:
        calculator.num2 = float(display.get())
        result = calculator.calculate()
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to set the operation
def set_operation(operation):
    try:
        calculator.num1 = float(display.get())
        calculator.expression = operation
        display.delete(0, tk.END)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Define buttons
buttons = [
    ('7', lambda: button_click(7)), ('8', lambda: button_click(8)), ('9', lambda: button_click(9)), ('/', lambda: set_operation('/')),
    ('4', lambda: button_click(4)), ('5', lambda: button_click(5)), ('6', lambda: button_click(6)), ('*', lambda: set_operation('*')),
    ('1', lambda: button_click(1)), ('2', lambda: button_click(2)), ('3', lambda: button_click(3)), ('-', lambda: set_operation('-')),
    ('0', lambda: button_click(0)), ('.', lambda: button_click('.')), ('=', button_equal), ('+', lambda: set_operation('+')),
    ('C', button_clear)
]

# Create and place buttons
row = 0
col = 0
for text, command in buttons:
    btn = tk.Button(button_frame, text=text, font=("Copperplate", 18), height=3, width=6, command=command)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main event loop
root.mainloop()
