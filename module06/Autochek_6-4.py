def add_employee_to_file(record:str, path:str):
    fh = open(path, 'a')

    try:
        fh.write(f'{record}\n')

    finally:
        fh.close()

print(add_employee_to_file('Drake Mikelsson,19', 'module6/Autochek_6-4.txt'))
