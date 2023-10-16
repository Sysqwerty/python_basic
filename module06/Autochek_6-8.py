source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output = 'module6/Autochek_6-8.txt'

def save_applicant_data(source, output):
    with open(output, 'w') as fh:

        res = list()
        
        for d in source:
            row = list()
            for v in d.values():
                row.append(str(v)) # get list of values for each dict (aka row)
            row_string = ','.join(row) + '\n'
            res.append(row_string)

            print('row =',row)
            print('row_string =',row_string)

        print('res =',res)            
        fh.writelines(res)

save_applicant_data(source, output)