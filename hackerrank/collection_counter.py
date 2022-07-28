from collections import Counter
n = int(input("Enter the number: "))

stock = list(map(int, input("Enter the list of numbers: ").split(' ')))
#print(stock)
Dict = Counter(stock)
#x represnts the number of times that you would like to loop over
x = int(input("Enter x: "))

p = 0
for i in range(x):
    size, price = map(int, input("Enter your sure size, press shift and then enter the price: ").split(' '))
    if(Dict[size]):
        Dict[size] -= 1
        p += price

print(p)
print(size)