def formatted_numbers() -> list:
    res = list()
    res.append(f'|{"decimal":^10}|{"hex":^10}|{"binary":^10}|')
    for i in range(16):
        res.append(f'|{i:<10}|{i:^10x}|{i:>10b}|')

    return res
    
for el in formatted_numbers():
    print(el)