from re import L


def mutation():
    string = "coding with chunoxiy"
    print(len(string))
    l = list(string)
    l[19] = "e"
    string = "".join(l)
    print(string)

mutation()