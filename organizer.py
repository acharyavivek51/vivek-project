import os
import shutil

source_folder = input("Enter folder path: ")

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
			if file.endswith(extensions):
				shutil.copy(file_path, os.path.join(source_folder, folder_name, file))

print("Files organized successfully!")




