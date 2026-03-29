import os
import shutil

source_folder = "test_folder"

images = os.path.join(source_folder, "Images")
docs = os.path.join(source_folder, "Documents")

os.makedirs(images, exist_ok=True)
os.makedirs(docs, exist_ok=True)

# create test files
open(os.path.join(source_folder, "photo.jpg"), "w").close()
open(os.path.join(source_folder, "file.pdf"), "w").close()

# move files
for file in os.listdir(source_folder):
	file_path = os.path.join(source_folder, file)

	if file.endswith(".jpg"):
		shutil.move(file_path, os.path.join(images, file))
	elif file.endswith(".pdf"):
		shutil.move(file_path, os.path.join(docs, file))

print("Files organized successfully!")
