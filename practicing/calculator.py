# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# print(x+y)

# x = float(input("Enter x: "))
# y = float(input("Enter y: "))

# z = round(x+y)

# print(f"{z:,}")
# x = float(input("Enter x: "))
# y = float(input("Enter y: "))

# z = x/y

# print(f"{z:.2f}")

from tkinter import N


def main():
    num = int(input("Enter num: "))
    print("squares of num is", sqare(num))

def sqare(n):
    return n * n


main()