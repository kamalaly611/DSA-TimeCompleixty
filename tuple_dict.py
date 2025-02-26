infor = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}

n1 = input("Enter 'All' to view all countries and their populations, 'Add' to add a country, 'Remove' to remove a country, or 'Query' to check population of a country: ")

if n1 == 'All':
    for team in infor:
     print(team,"==>" ,infor[team])
elif n1 == 'Add':
    n2 = input("Enter the country you want to add: ")
    n3 = int(input("Enter the population of the country: "))
    infor[n2] = n3
    print(infor)
elif n1 == 'Remove':
    n4 = input("Enter the country you want to remove: ")
    if n4 in infor:
        del infor[n4]
        print(infor)
    else:
        print("Country doesn't exist in the dictionary.")
elif n1 == 'Query':
    n5 = input('Enter which country you want to query: ')
    if n5 in infor:
        print(infor[n5])
    else:
        print("Country doesn't exist in the dictionary.")
else:
    print("Invalid input.")
