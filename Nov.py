import os
os.chdir(r'D:\OneDerive')
print('These is the current Directory==>',os.getcwd())
print(os.listdir())
print(os.stat('Kamal_3'))
os.rmdir('Kamal_2')
os.rename('Kamal_2','Kamal_3')
for dirpath, dirnames, filenames in os.walk(r'D:\OneDerive'):
    print('Current path',dirpath)
    print('Directories',dirnames)
    print('Filenames',filenames)
    print()

joined_path = os.path.join(os.environ.get('USERPROFILE'),'Kamal_3')  # Removed 'D:\'
print(joined_path)

print(os.getcwd())
