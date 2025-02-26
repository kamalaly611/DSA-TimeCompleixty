f=open('D:\\OneDerive\\Python series\\test.txt','r')
print(f.name)
f.close()
              Context Manger:::: With
with open('D:\\OneDerive\\Python series\\test.txt','r') as f:
    pass
print(f.read())
with open('D:\\OneDerive\\Python series\\test.txt','r') as f:
    content=f.readline()
    print(content,end='')
    content=f.readline()
    print(content,end='')
                Using Loops:
with open('D:\\OneDerive\\Python series\\test.txt','r') as f:
    for content in f:
        print(content,end='')
      to print the content at specfic level::
with open('D:\\OneDerive\\Python series\\test.txt', 'r') as f:
    content = ''  # Initialize an empty string to accumulate characters
    while len(content) < 100:
        chunk = f.read(10)  # Read 10 characters at a time (or adjust to any smaller chunk size)
        if not chunk:  # If we reach the end of the file, break the loop
            break
        content += chunk  # Add the chunk to the content string

    print(content[:100])  # Print only the first 100 characters

    
    content=f.read(100)
    print(content,end='')
    while True:
        line=f.read(100)
        if not line:
            break
        print(line,end='')

  Write Mode????
with open('test1.txt', 'w') as f:
    f.write('Test')
