f = open('test2.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    
    # Debug print to check the line content
    print(f"Debug: Reading line {i}: {line.strip()}")
    
    if not line:
        print("Debug: End of file reached or empty line.")
        break
    
    # Split the line and check if it has exactly 3 items
    parts = line.strip().split(",")
    if len(parts) != 3:
        print(f"Debug: Line {i} does not have exactly 3 comma-separated values.")
        continue  # Skip this line and continue to the next one
    
    try:
        m1 = int(parts[0].strip())
        m2 = int(parts[1].strip())
        m3 = int(parts[2].strip())
        
        print(f"Marks of student {i} in Maths is: {m1 * 2}")
        print(f"Marks of student {i} in English is: {m2 * 2}")
        print(f"Marks of student {i} in SST is: {m3 * 2}")
        
        print(line)
    
    except ValueError as e:
        print(f"Debug: Error converting marks to integers on line {i}: {e}")
        continue  # Skip this line if there's a ValueError

f.close()
