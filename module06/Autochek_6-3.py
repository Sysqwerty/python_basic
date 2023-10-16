def read_employees_from_file(path):
    fh = open(path, 'r')
    res = list()

    try:
        while True:
            line = fh.readline()
            if not line:
                break
            res.append(line.replace('\n', ''))

    finally:
        fh.close()
    
    return res


print(read_employees_from_file('module6/Autochek_6-3.txt'))
