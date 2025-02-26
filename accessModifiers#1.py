# class PublicExample:
#     def __init__(self):
#         self.public_attribute = "I am Public"

#     def public_method(self):
#         return "You can call me from anywhere!"

# # Create an object
# obj = PublicExample()

# # Access directly
# print(obj.public_attribute)  # ✅ Accessible
# print(obj.public_method())   # ✅ Accessible


# class ProtectedExample:
#     def __init__(self):
#         self._protected_attribute = "I am Protected"

#     def _protected_method(self):
#         return "Use me cautiously!"

# class SubProtected(ProtectedExample):
#     def access_protected(self):
#         return self._protected_attribute  # ✅ Accessed in subclass

# # Create an object
# obj = ProtectedExample()
# print(obj._protected_attribute)  # ⚠️ Works but not recommended
# print(obj._protected_method())   # ⚠️ Works but discouraged

# # Subclass access
# sub_obj = SubProtected()
# print(sub_obj.access_protected())  # ✅ Proper access in subclass


class PrivateExample:
    def __init__(self):
        self.__private_attribute = "I am Private"

    def __private_method(self):
        return "Only I can call myself!"

    def access_private(self):
        return self.__private_attribute  # Safe access

# Create an object
obj = PrivateExample()
# print(obj.__private_attribute)  # ❌ Error: Not directly accessible
# print(obj.__private_method())   # ❌ Error: Not directly accessible
print(obj.access_private())       # ✅ Access through a method

# Name mangling to access private (not recommended)
print(obj._PrivateExample__private_attribute)  # ✅ Works but discouraged


