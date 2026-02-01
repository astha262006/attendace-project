import tkinter as tk
from tkinter import messagebox

def calculate_attendance():
    all_students = set(entry_all.get().split(","))
    present_students = set(entry_present.get().split(","))
    absent_students = all_students - present_students
    result.set(
        f"Total Students: {all_students}\n"
        f"Present Students: {present_students}\n"
        f"Absent Students: {absent_students}"
    )
app = tk.Tk()
app.title("Student Attendance System")
app.geometry("450x350")
app.config(bg="#f0f0f0")
tk.Label(app, text="Attendance Management App",
         font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(app, text="Enter all students (comma separated):",
         bg="#f0f0f0").pack()
entry_all = tk.Entry(app, width=50)
entry_all.pack(pady=5)
tk.Label(app, text="Enter present students (comma separated):",
         bg="#f0f0f0").pack()
entry_present = tk.Entry(app, width=50)
entry_present.pack(pady=5)
tk.Button(app, text="Check Attendance",
          bg="#4CAF50", fg="white",
          command=calculate_attendance).pack(pady=15)
result = tk.StringVar()
tk.Label(app, textvariable=result, bg="#f0f0f0",
         font=("Arial", 10)).pack()

app.mainloop()
