import os
import tkinter as tk
from tkinter import messagebox

file_name = "expenses.txt"

def add_expense():
	value = entry.get().strip()

	if value == "":
		messagebox.showerror("Error", "Please enter a number")
		return

	try:
		amount = float(value)
		with open(file_name, "a") as f:
			f.write(str(amount) + "\n")

		entry.delete(0, tk.END)
		messagebox.showinfo("Success", "Expense added!")
	
	except ValueError:
		messagebox.showerror("Error", "Enter numbers only (like 100)")
	
def show_total():
	total = 0
	if os.path.exists(file_name):
		with open(file_name, "r") as f:
			for line in f:
				total += float(line.strip())
	messagebox.showinfo("Total", f"Total spent: {total}")

def show_expenses():
	if not os.path.exists(file_name):
		messagebox.showinfo("Expenses", "No expenses found")
		return
	
	with open(file_name, "r") as f:
		data = f.read()

	if data.strip() == "":
		messagebox.showinfo("Expenses", "No expenses found")
	else:
		messagebox.showinfo("Expenses", data)

def clear_expenses():
	if os.path.exists(file_name):
		open(file_name, "w").close()
		messagebox.showinfo("Success", "All expenses cleared!")
	else:
		messagebox.showinfo("Info", "No expenses to clear")
# GUI
root = tk.Tk()
root.title("Smart Expense Tracker")

title = tk.Label(root, text="Expense Tracker", font=("Arial", 14))
title.pack(pady=10)

label = tk.Label(root,text="Enter Expense Amount")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

btn1 = tk.Button(root, text="Add Expense", command=add_expense)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Show Total", command=show_total)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Show All Expenses", command=show_expenses)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Clear All Expenses", command=clear_expenses)
btn4.pack(pady=5)
root.mainloop()

def show_expenses():
	if not os.path.exists(file_name):
		messagebox.showinfo("Expenses", "No expenses found")
		return
	
	with open(file_name, "r") as f:
		data = f.read()

	if data.strip() == "":
		messagebox.showinfo("Expenses", "No expenses found")
	else:
		messagebox.showinfo("Expenses", data)
