# def print_pairs(numbers):
#     for i in numbers:
#         for j in numbers:
#             print(f"{i} * {j} = {i * j}")

# # Test it
# my_list = [1, 2, 3]
# print_pairs(my_list)

def print_pairs_three_times(lst):
    for i in lst:
        for j in lst:
            print(f"{i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} ")
            print(f"{i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} ")
            print(f"{i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} {i} {j} ")
            
print_pairs_three_times([1,1,1,1,1,1,1])