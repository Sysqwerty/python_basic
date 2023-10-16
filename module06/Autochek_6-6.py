def get_recipe(path:str, search_id:str):
    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            records = line.replace('\n', '').split(',')
            
            if records[0] == search_id:
                return {
                    "id": records[0],
                    "name": records[1],
                    "ingredients": records[2:]
                }  
    return None

print(get_recipe('module6/Autochek_6-6.txt', '60b90c4613067a15887e1ae5'))