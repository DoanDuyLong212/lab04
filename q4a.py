#1
import os
current_file_name = input("Please enter the name of the file you want to rename: ")
if os.path.isfile(current_file_name):
    new_file_name = input("Please enter the new name for the file: ")
    os.rename(current_file_name, new_file_name)
    print(f"The file {current_file_name} has been renamed to {new_file_name}")
else:
    print(f"The file {current_file_name} does not exist")
#2
import os
num_files = int(input("Please enter the number of files you want to rename: "))
current_file_names = []
for i in range(num_files):
    current_file_names.append(input(f"Please enter the name of file #{i+1}: "))
for i, current_file_name in enumerate(current_file_names):
    new_file_name = input(f"Please enter the new name for file #{i+1}: ")
    if os.path.isfile(current_file_name):
        os.rename(current_file_name, new_file_name)
        print(f"The file {current_file_name} has been renamed to {new_file_name}")
    else:
        print(f"The file {current_file_name} does not exist")
#3
import os
folder_path = input("Please enter the path of the folder containing the files you want to rename: ")
if os.path.isdir(folder_path):
    num_files = int(input("Please enter the number of files you want to rename: "))
    current_file_names = []
    for i in range(num_files):
        current_file_names.append(input(f"Please enter the name of file #{i+1}: "))
    for i, current_file_name in enumerate(current_file_names):
        new_file_name = input(f"Please enter the new name for file #{i+1}: ")
        current_file_path = os.path.join(folder_path, current_file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        if os.path.isfile(current_file_path):
            os.rename(current_file_path, new_file_path)
            print(f"The file {current_file_name} in the folder {folder_path} has been renamed to {new_file_name}")
        else:
            print(f"The file {current_file_name} in the folder {folder_path} does not exist")

else:
    print(f"The folder {folder_path} does not exist")
#4
import os
import time
file_name = input("Please enter the name of the file you want to rename: ")
file_path = os.path.abspath(file_name)
if os.path.isfile(file_path):
    timestamp = int(time.time())
    file_ext = os.path.splitext(file_name)[1]
    new_file_name = f"{os.path.splitext(file_name)[0]}_{timestamp}{file_ext}"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
    os.rename(file_path, new_file_path)
    print(f"The file {file_name} has been renamed to {new_file_name}")

else:
    print(f"The file {file_name} does not exist")
#5
import os
file_name = input("Please enter the name of the file you want to rename: ")
file_path = os.path.abspath(file_name)
if os.path.isfile(file_path):
    new_file_ext = input("Please enter the new file extension (without the dot): ")
    file_ext = os.path.splitext(file_name)[1]
    new_file_name = f"{os.path.splitext(file_name)[0]}.{new_file_ext}"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
    os.rename(file_path, new_file_path)
    print(f"The file {file_name} has been renamed to {new_file_name}")

else:
    print(f"The file {file_name} does not exist")
#6
import os
import shutil
file_name = input("Please enter the name of the file you want to rename and move: ")
new_location = input("Please enter the new location where you want to move the file: ")
file_path = os.path.abspath(file_name)
new_location_path = os.path.abspath(new_location)
if os.path.isfile(file_path):
    new_file_name = input("Please enter the new name for the file: ")
    file_ext = os.path.splitext(file_name)[1]
    new_file_name = f"{new_file_name}{file_ext}"
    new_file_path = os.path.join(new_location_path, new_file_name)
    os.rename(file_path, new_file_path)
    print(f"The file {file_name} has been renamed to {new_file_name} and moved to {new_location}")

else:
    print(f"The file {file_name} does not exist")