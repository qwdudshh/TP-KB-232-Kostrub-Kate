my_dict = {
    "kind": "cat",
    "age": 3,
    "num of paws": 4
}

print("Початковий словник:", my_dict)

my_dict.update({"tail": 1})
print("Після update():", my_dict)

del my_dict["age"]
print("Після del() для ключа 'age':", my_dict)

my_dict.clear()
print("Після clear():", my_dict)

my_dict = {
    "kind": "dog",
    "age": 5,
    "num of paws": 4,
    "tail": 1
}

keys = my_dict.keys()
print("Ключі словника:", keys)

values = my_dict.values()
print("Значення словника:", values)

items = my_dict.items()
print("Пари ключ-значення у словнику:", items)


