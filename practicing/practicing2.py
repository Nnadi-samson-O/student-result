def main():
    x = get_int()
    print(f"x is {x}") 
def get_int():

    while True:
        try:

            x = int(input("Enter a value here: "))
            
        except ValueError:
            print("insert a valid data")
        else:
            break
    return x
main()