import os
import shutil

source_dir = "/Users/elroeesirak/Downloads"

dir1 = os.path.join(source_dir, "PDFs_or_Docx")
dir2 = os.path.join(source_dir, "Images")
dir3 = os.path.join(source_dir, "html_files")
dir4 = os.path.join(source_dir, "other_files")

os.makedirs(dir1, exist_ok=True)
os.makedirs(dir2, exist_ok=True)
os.makedirs(dir3, exist_ok=True)
os.makedirs(dir4, exist_ok=True)

with os.scandir(source_dir) as files:
    for file in files:
        if file.is_file():
            split_tup = os.path.splitext(file.name)
            file_extension = split_tup[1].lower()

            if file_extension in (".pdf", ".docx"):
                shutil.move(file.path, dir1)
            elif file_extension in (".jpg", ".jpeg"):
                shutil.move(file.path, dir2)
            elif file_extension == ".html":
                shutil.move(file.path, dir3)
            else:
                shutil.move(file.path, dir4)
