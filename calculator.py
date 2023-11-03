import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = entry_operation.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operation"

    label_result.config(text="Result: " + str(result))

window = tk.Tk()
window.title("Simple Calculator")


label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_operation = tk.Label(window, text="Operation (+, -, *, /):")
label_operation.pack()
entry_operation = tk.Entry(window)
entry_operation.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()


button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()


label_result = tk.Label(window, text="Result:")
label_result.pack()


window.mainloop()
