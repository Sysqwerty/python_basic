def get_cats_info(path):
    with open(path, 'r') as fh:
        res = list()

        while True:
            line = fh.readline()
            if not line:
                break
            records = line.replace('\n', '').split(',')

            res.append({
                "id": records[0],
                "name": records[1],
                "age": records[2],
            })


        return res


print(get_cats_info('module6/Autochek_6-5.txt'))
