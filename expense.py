import os

file_name = "expenses.txt"

# load previous expenses
expenses = []
if os.path.exists(file_name):
	with open(file_name, "r") as f:
		for line in f:
			expenses.append(float(line.strip()))

while True:
	print("\n1. Add Expense")
	print("2. Show Total")
	print("3. Exit")

	choice = input("Choose option: ")

	if choice == "1":
		amount = float(input("Enter amount: "))
		expenses.append(amount)

		# save to file
		with open(file_name, "a") as f:
			f.write(str(amount) + "\n")

		print("Expense added!")

	elif choice == "2":
		print("Total spent:", sum(expenses))

	elif choice == "3":
		break
	
	else:
		print("Invalid choice")