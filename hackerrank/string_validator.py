def string_validator():
    s = input("Enter s below:\n")
    
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.isupper() for i in s))
    print(any(i.islower() for i in s))

string_validator()