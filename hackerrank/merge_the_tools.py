# from collections import OrderedDict


# def merge_to_tools(string, k):
#     for i in range(0, len(string), k):
#         print("".join(OrderedDict.fromkeys(string[i:i + k])))

# merge_to_tools("AABCAAADA", 3)

# def merge_the_tools(string, k):
#     split_string = (string[i:i+k] for i in range(0, len(string), k))
#     for i in split_string:
#         u = []
#         u.append(i[0])
#         for j in range(1, len(i)):
#             if i[j] in u:
#                 continue
#             else:
#                 u.append(i[j])
#         print("".join(str(e) for e in u))


# merge_the_tools("AABCAAADA", 3)


def merge_the_string(string, k):
    l = []
    m = 0
    for i in range(len(string)// k):
        l.append(string[m:m+k])
        m += k
    print(l)
    for v in l:
        # print(list(v))
        # print(dict.fromkeys(list(v)))
        # print(dict.fromkeys(list(v), 1))
        # print(dict.fromkeys(list(v)).keys())
        # print(list(dict.fromkeys(list(v)).keys()))
        print(''.join(list(dict.fromkeys(list(v)).keys())))

string = input("Enter string: ")
k = int(input("Enter integer:"))
merge_the_string(string, k)