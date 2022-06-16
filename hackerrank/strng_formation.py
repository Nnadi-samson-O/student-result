def srting_formation(number):
    """PRINTS NUMBER IN DECIMAL, OCTAL, HEXADECIMAL AND BINARY"""
    for i in range(1, number + 1):
        width = len(f"number:b")
        print(f"{i:{width}} {i:{width}o} {i:{width}x} {i:{width}b}")

srting_formation(17)