from unicodedata import name


def main():
    name = input("what's your name? ")
    hello(name.title().strip())


def hello(to ="world"):
    print("hello,",to )


main()