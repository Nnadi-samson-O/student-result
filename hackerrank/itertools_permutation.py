from itertools import permutations

s =input("Enter the value you want to permutate and the number of times you want to \n").split()
string = sorted(s[0])
number = int(s[1])
print(*list(map(''.join, permutations(string, number))), sep='\n')