# Is Vs == in python
# These  both are comparison Operators
# 'is' Checks if two objects refer to the same memory location (identity)
# = Behavior: Compares the objects themselves, not their values
scores1 = (85, 90, 75)
scores2 = (85, 90, 75)
print(scores2==scores1)
print(scores2 is scores1)
scores3=scores2
print(scores3 is scores2)
print(scores3==scores2)
