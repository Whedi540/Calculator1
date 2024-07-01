import tkinter as tk
from tkinter import messagebox
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except Exception as e:
        return "Error! Invalid input."
def on_button_click(character):
    current_text = entry.get()
    new_text = current_text + str(character)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)
def on_equals_click():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)
def on_clear_click():
    entry.delete(0, tk.END)
# Create the main window
root = tk.Tk()
root.title("Calculator")
# Create an entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)
# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
# Create the buttons and place them on the grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=on_equals_click)
    elif button == 'C':
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18), command=on_clear_click)
    else:
        btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 18),
                        command=lambda b=button: on_button_click(b))

    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# Clear button
clear_btn = tk.Button(root, text='Clear', width=4, height=1, font=('Arial', 18), command=on_clear_click)
clear_btn.grid(row=row_val, column=0, columnspan=2)

# Run the main loop
root.mainloop()