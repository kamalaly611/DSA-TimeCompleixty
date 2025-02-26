# For Seek Functions:
with open('seek_tell','r') as f:
    f.seek(5)
    data=f.read(5)
    print(data)
# For Tell Fucntiona
with open('seek_tell', 'r') as f:
    posi = f.tell()
    print(f"File pointer is at position: {posi}")  

    data = f.read(5) 
    posi = f.tell()
    print(f"File pointer is now at position: {posi}")
    print(f"File Data Now: {data}")  

# Truncate For Resize the bytes
with open('seek_tell','w+') as f:
    f.write("Python Programming")  # File contains "Python Programming"
    f.seek(6)                      # Move file pointer to position 6
    f.truncate()                   # Truncate from the current position
    f.seek(6)
    print(f.read())                # Output: "Python"
