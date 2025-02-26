import os

# Get and print the current working directory
result = os.getcwd()
print('This is the location where I am currently working:', result)

# Change to the new directory
os.chdir(r'D:\Kamal Hussain\Data Science')

# Verify and print the new working directory
result2 = os.getcwd()
print('Now, I am working in:', result2)
# List and print files in the new directory
files = os.listdir()
print('Files and folders in the new directory:', files)