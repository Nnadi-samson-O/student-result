# string = "python pool"
# print("original string:")
# print(string)
# print("After capitalization first leeter:")
# print(string.capitalize())


# string = "python pool"
# print("original string:")
# print(string)
# result = string[0].upper() + string[1:]
# print("After capitalization first letter:")
# print(result)


# string = "python pool"
# print("Original string:")
# print(string)
# print("After capitalizing:")
# print(str.title(string))

# string = "python pool"
# print("Original string:")
# print(string)
# print("After capitalizing first letter:")
# result = ' '.join(elem.capitalize() for elem in string.split())
# print(result)


import string
txt = "python pool"
print("Original string:")
print(txt)
print("After capitalizing first letter:")
result = string.capwords(txt)
print(result)