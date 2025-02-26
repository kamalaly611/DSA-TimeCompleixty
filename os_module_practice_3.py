import os
import shutil
from datetime import datetime

def log_action(log_file_path, message):
    """
    Logs a message to the specified log file.

    Args:
        log_file_path (str): Path to the log file.
        message (str): Message to log.
    """
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def manage_project_files(projects_path, backup_path):
    """
    Manages files in the Projects directory by:
    1. Creating a backup folder if it doesn't exist.
    2. Listing all files in the Projects directory.
    3. Moving .txt files to the backup folder.
    4. Logging each action taken in a log.txt file.

    Args:
        projects_path (str): Path to the Projects directory.
        backup_path (str): Path where backup folder should be created.
    """
    # Ensure the paths are valid
    if not os.path.exists(projects_path):
        print(f"Error: Projects directory '{projects_path}' does not exist.")
        return

    if not os.path.exists(backup_path):
        print(f"Error: Backup directory '{backup_path}' does not exist.")
        return

    # 1. Check and create backup folder
    backup_folder = os.path.join(backup_path, "Project_Backups")
    log_file_path = os.path.join(backup_folder, "log.txt")
    
    if not os.path.exists(backup_folder):
        try:
            os.makedirs(backup_folder)
            print(f"Created backup folder: {backup_folder}")
            log_action(log_file_path, f"Created backup folder at {backup_folder}")
        except Exception as e:
            error_message = f"Error creating backup folder: {str(e)}"
            print(error_message)
            log_action(log_file_path, error_message)
            return
    else:
        print(f"Backup folder already exists: {backup_folder}")
        log_action(log_file_path, f"Backup folder already exists at {backup_folder}")

    # 2. List all files in the Projects folder
    print("\nFiles in Projects folder:")
    try:
        files = [f for f in os.listdir(projects_path) if os.path.isfile(os.path.join(projects_path, f))]
        if files:
            for file in files:
                print(f"- {file}")
            log_action(log_file_path, "Listed all files in Projects folder.")
        else:
            print("No files found in the Projects directory.")
            log_action(log_file_path, "No files found in the Projects directory.")
    except Exception as e:
        error_message = f"Error listing files: {str(e)}"
        print(error_message)
        log_action(log_file_path, error_message)
        return

    # 3. Move .txt files to backup folder
    txt_files_moved = False
    for file in files:
        if file.endswith('.txt'):
            source_path = os.path.join(projects_path, file)
            
            # Create a unique filename in case of duplicates
            base_name = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{base_name}_{timestamp}{extension}"
            destination = os.path.join(backup_folder, new_filename)
            
            try:
                shutil.move(source_path, destination)
                print(f"\nMoved '{file}' to backup folder as '{new_filename}'")
                log_action(log_file_path, f"Moved '{file}' to '{new_filename}' in backup folder.")
                txt_files_moved = True
            except Exception as e:
                error_message = f"Error moving {file}: {str(e)}"
                print(error_message)
                log_action(log_file_path, error_message)
    
    if not txt_files_moved:
        print("\nNo .txt files found to move.")
        log_action(log_file_path, "No .txt files found to move.")

if __name__ == "__main__":
    # Your specific paths
    projects_dir = r"D:\OneDerive\Python series"
    backup_dir = r"D:\OneDerive"
    
    manage_project_files(projects_dir, backup_dir)
