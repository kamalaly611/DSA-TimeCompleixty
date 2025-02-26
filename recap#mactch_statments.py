x = input("What is your priorty level: , (Medium/Low/High): ")

match x:
    case _ if x == "Medium":
        print("it's scheduled for resolution in 3 days")
    case _ if x=="Low":
        print("it needs attention within 24 hours.")
    case _ if x=="High":
        print("it must be addressed immediately.")
    case _:
        print("Invalid priority level.")


