items = [
    ("product1", 10),
    ("prodct2", 9),
    ("produc3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)