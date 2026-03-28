import os
import shutil

folder = "test_folder"

if not os.path.exists(folder):
    os.makedirs(folder)

print("Folder ready:", folder)