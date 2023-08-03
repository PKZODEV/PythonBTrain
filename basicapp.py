import tkinter as tk

def show_message():
    message = entry.get()
    label.config(text=message)

# สร้างหน้าต่างหลักของแอปพลิเคชัน
window = tk.Tk()
window.title("แอปพลิเคชันง่ายๆ")
window.geometry("300x200")

# สร้างส่วนกรอกข้อความ
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=20)

# สร้างปุ่มสำหรับแสดงข้อความ
button = tk.Button(window, text="แสดงข้อความ", command=show_message)
button.pack()

# สร้างป้ายกำกับสำหรับแสดงข้อความ
label = tk.Label(window, font=("Helvetica", 16))
label.pack(pady=20)

# เริ่มการทำงานของแอปพลิเคชัน
window.mainloop()
