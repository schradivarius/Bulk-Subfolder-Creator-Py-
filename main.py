# Created by CS, see my GitHub for more: https://github.com/schradivarius

# This script is meant to look inside each folder inside of the base file path, and then create a new folder inside of each folder in that path.
# For example, the file structure would look something like this:
#
# Base File Path (base_path)
# ├── Folder 1 
# │   ├── Subfolder 1 (subfolder_name)
# │       ├── "New Subfolder Name" (new folder created by this script)
# ├── Employee 2
# │   ├── Subfolder 2 (subfolder_name)
# │       ├── "New Subfolder Name" (new folder created by this script)
#
# ... and so on for each folder in the base file path.
# Hopefully this is as useful to you as it is to me. I have a lot of folders that I need to add subfolders to, and this script saves me a lot of time.

import os

# Base path - update this to the path
base_path = r"FILE_PATH"

# Subfolder to place the new subfolder in. This is the SUBFOLDER that will be inside of each FOLDER in the base path.
subfolder_name = "SUBNAME"

# Name of the new subfolder to create. This folder will go inside of each FOLDER in the base path.
new_subfolder_name = "NEWSUBNAME"

# Counters
already_exists_count = 0
created_count = 0
missing_SUB_count = 0

print("=== CREATING FOLDERS ===\n")

for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    if os.path.isdir(folder_path):
        sub_folder_path = os.path.join(folder_path, subfolder_name)
        
        if os.path.isdir(sub_folder_path):
            new_folder_path = os.path.join(sub_folder_path, new_subfolder_name)
            
            # Create the folder if it doesn't exist
            if os.path.exists(new_folder_path):
                print(f"[EXISTS] {new_folder_path}")
                already_exists_count += 1
            else:
                os.makedirs(new_folder_path)
                print(f"[CREATED] {new_folder_path}")
                created_count += 1
        else:
            print(f"[MISSING I-9] {folder_name}")
            missing_SUB_count += 1

# Summary
print("\n=== SUMMARY ===")
print(f"Folders already existed: {already_exists_count}")
print(f"Folders created: {created_count}")
print(f"Folders missing SUB folder: {missing_SUB_count}")
