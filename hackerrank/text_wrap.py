import textwrap
from unittest import result

def wrap(string, max_width):
    return textwrap.TextWrapper(width=max_width).fill(text=string)

def text_wrap():
    string, max_width = input("Enter a string here: "),\
         int(input("Enter intiger here for the lenght of the width: "))
    result = wrap(string, max_width)
    print(result)

text_wrap()