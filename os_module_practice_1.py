import os
import shutil  # Import shutil to use disk_usage

# Step 1: Navigate and organize files based on department
base_path = r"C:\Users\etopi.DESKTOP-51VUFOC\Documents"

departments = ["HR", "Finance", "IT"]

for department in departments:
    department_path = os.path.join(base_path, department)

    # Check if department folder exists, if not, create it
    if not os.path.exists(department_path):
        os.makedirs(department_path)
        print(f"Created directory for {department} at {department_path}")

    # Step 2: Create a new folder for the current month if it doesn't exist
    month_folder = os.path.join(department_path, "October_2024")
    if not os.path.exists(month_folder):
        os.makedirs(month_folder)
        print(f"Created monthly directory for {department}: {month_folder}")

# Step 3: Change file permissions for confidential files (example only)
confidential_file = os.path.join(base_path, "HR", "confidential.txt")
if os.path.exists(confidential_file):
    os.chmod(confidential_file, 0o600)  # Read/write for owner only
    print(f"Permissions updated for {confidential_file}")

# Step 4: Retrieve system info
current_directory = os.getcwd()
platform = os.name

# Use shutil.disk_usage() instead of os.statvfs()
disk_usage = shutil.disk_usage(base_path)
free_space = disk_usage.free / (1024 * 1024)  # Convert to MB

print(f"Current directory: {current_directory}")
print(f"Running on platform: {platform}")
print(f"Free space in {base_path}: {free_space:.2f} MB")

# Step 5: Access environment variables
home_dir = os.environ.get('HOME')
user = os.environ.get('USER')

print(f"User: {user}")
print(f"Home directory: {home_dir}")
