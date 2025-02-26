with open("D:\\OneDerive\\Python series\\value.txt",'r') as f:
    i=0
    while True:
        i+=1
        line=f.readline()
        if not line:
            break
        m1=int(line.split(" ")[0])
        m2=int(line.split(" ")[1])
        m3=int(line.split(" ")[2])
        print(f'Marks of the Student {i} in English  {m1}')
        print(f'Marks of the Student {i} in Maths  {m2}')
        print((f'Marks of the Student {i} in SST  {m3}'))

        
