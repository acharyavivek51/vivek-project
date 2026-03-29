import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
	source_folder = filedialog.askdirectory()

	if not source_folder:
		return

	file_types = {
		"Images": [".jpg", ".png"],
		"Documents": [".pdf", ".txt"],
		"Videos": [".mp4", ".mkv"]
	}

	for folder_name, extensions in file_types.items():
		folder_path = os.path.join(source_folder, folder_name)
		os.makedirs(folder_path, exist_ok=True)
	
	for file in os.listdir(source_folder):
		file_path = os.path.join(source_folder, file)

		if os.path.isfile(file_path):
			for folder_name, extensions in file_types.items():
				if file.endswith(tuple(extensions)):
					shutil.copy(file_path, os.path.join(source_folder, folder_name, file))

	messagebox.showinfo("Success", "Files organized successfully!")

# GUI
root = tk.Tk()
root.title("Smart File Organizer")

btn = tk.Button(root, text="Select Folder & Organize", command=organize_files)
btn.pack(pady=20)

root.mainloop()
