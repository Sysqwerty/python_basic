name = ["dan", "jane", "steve", "mike"]


def normal_name(list_name: list[str]):
    res = list()
    for i in map(lambda name: name.capitalize(), list_name):
        res.append(i)
    return res

print(normal_name(name))


# Лямбда-функції

# numbers = [1, 2, 3, 4, 5]
# for i in map(lambda x: x ** 2, numbers):
#     print(i)
