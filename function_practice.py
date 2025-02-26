def find_totat(exp):
    total=0
    for item in exp:
        total+=item
    return total

mishal_expenses=[10,20,30]
mishal_total=find_totat(mishal_expenses)

zoya_expenses=[40,50,70]
zoya_total=find_totat(zoya_expenses)

print(mishal_total)
print(zoya_total)

