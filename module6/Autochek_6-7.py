import re

source = 'module6/Autochek_6-7.txt'
output = 'module6/Autochek_6-7+.txt'

def sanitize_file(source, output):
    with open(source, 'r') as file1:
        file1_text_clear = re.sub(r'\d+', '', file1.read())
        print(file1_text_clear)
    
    

    with open(output, 'w') as file2:
        file2.write(file1_text_clear)

sanitize_file(source, output)
