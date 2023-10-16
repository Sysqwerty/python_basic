students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    res = list()
    for i, key in enumerate(students):
        val = students[key]
        res.append(f'{i+1:>4}|{key:<10}|{val:^5}|{grades[val]:^5}')
        # res.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(i+1, key, val, grades[val]))
    return res

for el in formatted_grades(students):
    print(el)