def write_employees_to_file(employee_list:list, path):
    fh = open(path, 'w')

    try:
        for array in employee_list:
            for e in array:
                fh.write(f'{e}\n')

    finally:
        fh.close()

write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'module6/Autochek_6-2.txt')
