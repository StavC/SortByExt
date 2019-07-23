import os
import shutil

path = input("> ")
dirs = os.listdir(path)
files_extensions = set()

for dir in dirs:

    curr_path = path + "\\" + dir
    if os.path.isfile(curr_path):
        curr_ext = dir.split('.')[-1]
        files_extensions.add(curr_ext)
print(files_extensions)

for exten in files_extensions:
    new_path = path + "\\" + exten
    os.mkdir(new_path)

for dir in dirs:
    curr_path = path + "\\" + dir
    curr_ext = dir.split('.')[-1]
    curr_path_to_move = path + "\\" + curr_ext
    if os.path.isfile(curr_path):
        shutil.move(curr_path, curr_path_to_move)
