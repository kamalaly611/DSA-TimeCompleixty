import os

# Set up directory paths
base_path = r'D:\OneDerive\Python series'
backup_path = os.path.join(base_path, 'Project_Backups')

# Create Project_Backups if it doesn't exist
if not os.path.exists(backup_path):
    os.mkdir(backup_path)

# Change to base directory
os.chdir(base_path)

# 1. Rename files in Project_Backups
for filename in os.listdir(backup_path):
    if filename.endswith('.txt'):
        new_name = filename.replace('.txt', '_backup.txt')
        os.rename(os.path.join(backup_path, filename), os.path.join(backup_path, new_name))

# 2. Delete files over 2MB in Project_Backups
for filename in os.listdir(backup_path):
    file_path = os.path.join(backup_path, filename)
    if os.path.getsize(file_path) > 2 * 1024 * 1024:  # 2MB in bytes
        os.remove(file_path)

# 3. Count file types in base path and print summary
file_counts = {}
for filename in os.listdir(base_path):
    if os.path.isfile(os.path.join(base_path, filename)):
        extension = filename.split('.')[-1]
        file_counts[extension] = file_counts.get(extension, 0) + 1

print("File type counts:", file_counts)

# 4. Log actions taken
with open(os.path.join(backup_path, 'log.txt'), 'w') as log_file:
    log_file.write("Actions Taken:\n")
    log_file.write(f"Renamed .txt files with '_backup' suffix in {backup_path}\n")
    log_file.write("Deleted files over 2MB in Project_Backups\n")
    log_file.write("File type counts in base path:\n")
    for file_type, count in file_counts.items():
        log_file.write(f"{file_type}: {count}\n")
