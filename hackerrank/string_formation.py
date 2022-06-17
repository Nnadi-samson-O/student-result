# def srting_formation(number):
#     """PRINTS NUMBER IN DECIMAL, OCTAL, HEXADECIMAL.upper AND BINARY"""
#     for i in range(1, number + 1):
#         width = len(f"number:b")
#         print(f"{i:{width}}  {i:{width}o} {i:{width}x} {i:{width}b}",)

# srting_formation(17)

import math

n = int(input("Enter a number here: "))
max_length = math.floor(math.log(n,2))+1

for i in range(1, n+1):
    d = str(i).rjust(max_length)
    o = str(oct(i))[2:].rjust(max_length)
    h = str(hex(i))[2:].upper().rjust(max_length)
    b = bin(i)[2:].rjust(max_length)
    print("{} {} {} {}".format(d, o, h, b))