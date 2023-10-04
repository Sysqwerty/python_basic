source_file = "module7/Autocheck_7-14.txt"
output_file = "module7/Autocheck_7-14+.txt"

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:        
        lines = fh.readlines()
        res_list = list()
        
        for i, value in enumerate(lines):
            res_list.append(f"{i}: {value}")
        
    with open(output_file, 'w') as fh:
        fh.writelines(res_list)

to_indexed(source_file, output_file)
        