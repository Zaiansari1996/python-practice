import os 
import shutil

source_folder = os.getcwd()
print("Current directory:", source_folder)

# List of folders we create (to avoid moving them later)
organized_folders = ["images", "New Documents", "Videos", "Others"]

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    
    # Skip directories and the script itself
    if not os.path.isfile(file_path) or file == os.path.basename(__file__):
        continue
    
    file_lower = file.lower()
    
    # Move Images
    if file_lower.endswith((".png", ".jpg", ".jpeg")):
        target_folder = os.path.join(source_folder, "images")
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        shutil.move(file_path, os.path.join(target_folder, file))
    
    # Move Documents
    elif file_lower.endswith((".pdf", ".docx", ".txt", ".csv", ".doc", ".rtf", ".odt")):
        target_folder = os.path.join(source_folder, "New Documents")
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        shutil.move(file_path, os.path.join(target_folder, file))
    
    # Move Videos
    elif file_lower.endswith((".mp4", ".mov")):
        target_folder = os.path.join(source_folder, "Videos")
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        shutil.move(file_path, os.path.join(target_folder, file))
    
    # Move Others (only files not matching above)
    else:
        target_folder = os.path.join(source_folder, "Others")
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        shutil.move(file_path, os.path.join(target_folder, file))

print("📁 Folder organized successfully!")