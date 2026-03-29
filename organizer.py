import os
import shutil

source_folder = input("Enter folder path: ")

images = os.path.join(source_folder, "Images")
docs = os.path.join(source_folder, "Documents")
videos = os.path.join(source_folder, "Videos")

os.makedirs(images, exist_ok=True)
os.makedirs(docs, exist_ok=True)
os.makedirs(videos, exist_ok=True)

for file in os.listdir(source_folder):
	file_path = os.path.join(source_folder, file)

	if os.path.isfile(file_path):
		if file.endswith((".jpg", "/png")):
			shutil.copy(file_path, os.path.join(images, file))
		elif file.endswith((".pdf", ".txt")):
			shutil.copy(file_path, os.path.join(docs, file))
		elif file.endswith((".mp4", ".mkv")):
			shutil.copy(file_path, os.path.join(videos, file))

print("Files organized safely (copied)!")