import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("calc")
root.geometry("170x225")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    action = lambda x=text: click(x) if x not in ['C'] else clear()
    tk.Button(root, text=text, command=action).grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=2)

tk.Button(root, text="=", width=20, command=calculate).grid(row=5, column=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=2)

root.mainloop()
