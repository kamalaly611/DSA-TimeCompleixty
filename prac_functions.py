# def add_total(exp):
#     total = 0
#     for item in exp:
#         total += int(item)
#     return total
def mult_total(exp):
    mult_total=1
    for item in exp:
        mult_total*=int(item)
    return mult_total

n1 = input("Enter the expense list for addition: ").split(',')
n2 = input("Enter the expense list for addition: ").split(',')

addition_total = mult_total(n1)
print("Total expense for list 1:", addition_total)

addition_total = mult_total(n2)
print("Total expense for list 2:", addition_total)
print(help(mult_total))


