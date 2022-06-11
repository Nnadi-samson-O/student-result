#for i in [0,1,2]:
#print("the boy is good\n"*3, end="")

# while True:
#     n = int(input("what's n?\n"))
#     if n > 0:
#         break;

# for _ in range(n):
#     print("the boy is good") 


def main():
    number = get_number()
    num(number)

def get_number():
        while True:
            n = int(input("what's n\n"))
            n -=1
            if n > 0:
                break;
        return n

def num(n):
    for t in range(n):
        print(t, "we are good to go")
main()