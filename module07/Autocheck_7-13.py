path = 'module07/Autocheck_7-13.txt'

def get_employees_by_profession(path, profession):
    res = list()

    with open(path, 'r') as fh:        
        lines = fh.readlines()
        
        for i in lines:
            i = i.strip().replace("\n", "")
            person_name, person_profession = i.split()
            if person_profession == profession:
                res.append(person_name)
        
    return " ".join(res)

print(get_employees_by_profession(path, 'cook'))
