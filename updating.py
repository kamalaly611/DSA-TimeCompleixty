try:
    with open('diary.txt', 'r') as f:
        data=f.read(100)
        print(data)
        f.seek(0)
        i=0
        while True:
            i=i+1
            line=f.readline()
            if not line:
                break
            print(f'{i}:{line.strip()}')
except FileNotFoundError:
    print("Error: 'diary.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
try:
    with open('diary.txt','a') as f:
        ask=f.write('Hello janu')
        print("\nContent appended successfully!")
except Exception as e:
    print(f"Error while writing to the file: {e}")
try:
    with open('diary.txt','r') as f:
        Position=f.seek(170)
        data=f.read()
        print(f'The Given Position is now at {Position} and content is {data}')
except Exception as e:
    print(f"Error during seek operation: {e}")
# For Position Tracking: Display the current file position before and after each operation using tell()
try:
    with open('diary.txt','r') as f:
        Position=f.tell()
        print(f"\nInitial position of the file pointer: {Position}")
        f.read(50)
        position = f.tell()
        print(f"Position after reading 50 characters: {position}")
except Exception as e:
    print(f"Error while tracking position: {e}")