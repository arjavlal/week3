import tkinter as tk
import pandas as pd

df = pd.read_excel('a.xlsx')
students = dict(zip(df["name"].str.lower(), df["age"]))
 
def search():
    text = entry.get().lower()
    for name in students:
        if name in text:
            result.config(text=f"{name.title()}'s age is {students[name]}")
            return
    result.config(text="Student not found")

root = tk.Tk()
root.title("Student Chatbot")
root.geometry("400x200")
tk.Label(root, text="Ask a question: ").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
tk.Button(root, text="Search", command=search).pack(pady=5)
result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=10)
root.mainloop()