import os
import shutil
from datetime import datetime
from tqdm import tqdm

def add_file_to_backup(file_path, backup_dir, relative_path):
    """
    Copies a file to the backup directory while maintaining the folder structure.
    """
    try:
        target_path = os.path.join(backup_dir, relative_path)
        target_dir = os.path.dirname(target_path)
        os.makedirs(target_dir, exist_ok=True)  # Create target directories
        shutil.copy(file_path, target_path)  # Copy file
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
    except OSError as e:
        print(f"Error copying file {file_path}: {e}")

def create_backup(source_dir, backup_base_dir):  
    print("Welcome to the iCloud Backup Program!")

    if not os.path.exists(source_dir):
        print(f"Error: Source directory does not exist - {source_dir}")
        return

    timestamp = datetime.now().strftime("%d.%m.%Y-%H.%M")
    backup_dir = os.path.join(backup_base_dir, f"backup_{timestamp}")

    os.makedirs(backup_dir, exist_ok=True)  # Create timestamped folder

    all_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, source_dir)
            all_files.append((full_path, relative_path))

    with tqdm(total=len(all_files), desc="Creating backup...", unit="file") as pbar:  
        for file_path, relative_path in all_files:
            add_file_to_backup(file_path, backup_dir, relative_path)
            pbar.update(1)  # Update progress bar

    zip_file = os.path.join(backup_base_dir, f"{zip_Name}_{timestamp}.zip")
    
    try:
        shutil.make_archive(zip_file.replace('.zip', ''), 'zip', backup_dir)
    except Exception as e:
        print(f"Error creating zip archive: {e}")

    shutil.rmtree(backup_dir)  # Remove folder after zipping
    print(f"Backup successfully created")  

# Example: Backup from "source_folder" to "backup_folder"
zip_Name = "iCloud" #name of the zip file
source_folder = r"D:\01_Coding\04_GitHubProjects\TestFolder"  # Source directory
backup_folder = r"D:\01_Coding\04_GitHubProjects\BackupFolder"  # Backup directory

create_backup(source_folder, backup_folder)

# Wait for user input before closing the program
input()
