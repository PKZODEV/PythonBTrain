import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("เครื่องคิดเลข")

# สร้างช่องข้อความสำหรับแสดงผล
entry = tk.Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# สร้างปุ่มตัวเลขและเครื่องหมาย
buttons = [
    ("7", 1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1),
    ("4", 2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1),
    ("1", 3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1),
    ("0", 4, 0, 2)
]

for button in buttons:
    number, row, column, columnspan = button
    button = tk.Button(root, text=number, padx=20, pady=10, command=lambda num=number: button_click(num))
    button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

# สร้างปุ่มคำนวณ
button_equal = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
button_equal.grid(row=4, column=2, padx=5, pady=5)

button_clear = tk.Button(root, text="C", padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
