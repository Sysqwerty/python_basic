def is_integer(s:str):
    
    if len(s) == 0:
        return False
    return s.strip().replace('+', '').replace('-', '').isdigit()

print(is_integer(' +56- '))