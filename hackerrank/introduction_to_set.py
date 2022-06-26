def average(array):
    array = set(array)
    return sum(array)/ len(array)


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)