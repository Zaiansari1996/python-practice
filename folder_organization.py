import os
import shutil

source_folder = os.getcwd()
script_name = os.path.basename(__file__)  # Gets the current script's filename (e.g., "folder_organization.py")

file_types = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif'],
    "Documents": ['.pdf', '.docx', '.txt'],
    "Videos": ['.mp4', '.mov'],
    "Others": []
}

for file in os.listdir(source_folder):
    # Skip directories AND the script itself
    if os.path.isdir(os.path.join(source_folder, file)) or file == script_name:
        continue  # ⚠️ Prevents moving folders + the script
    
    filename, ext = os.path.splitext(file)
    found = False
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            if not os.path.exists(os.path.join(source_folder, folder)):
                os.makedirs(os.path.join(source_folder, folder))
            shutil.move(os.path.join(source_folder, file), os.path.join(source_folder, folder, file))
            found = True
            break
    if not found:
        if not os.path.exists(os.path.join(source_folder, "Others")):
            os.makedirs(os.path.join(source_folder, "Others"))
        shutil.move(os.path.join(source_folder, file), os.path.join(source_folder, "Others", file))

print("📁 Folder organized! (Script stayed in place)")