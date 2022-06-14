from sys import _enablelegacywindowsfsencoding

#This argument accepts two in put, if incase the \first digit is 4 the second will be the tripl of the first argument
n,m = input("Enter integer here: ").split() 

c = "|"
v = "."

n = int(n)
m = int(m)
j = n // 2-1

for i in range(n):
    if i == n // 2:
        print("God bless you".center(m, "-"))

    else:
        if i < n / 2:
            print(((v + c+ v)*(2 * i + 1)).center(m, "-"))

        else:
            print(((v + c + v)*(2 * j + 1)).center(m, "-"))
            j = j-1
