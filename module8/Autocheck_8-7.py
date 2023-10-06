import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
tup = [Cat("Mick", 5, "Sara"), Cat(
    "Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
di = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


def convert_list(cats):
    res = list()
    for i in cats:
        if isinstance(i, tuple):
            res.append({"nickname": i.nickname,
                       "age": i.age, "owner": i.owner})
        else:
            res.append(Cat(i["nickname"], i["age"], i["owner"]))

    return res


print(convert_list(tup))


# Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# person.name  # 'Mick'
# person.post_index  # '01146'
# person.age  # 35
# person[3]  # 'Boston'
