path = 'module6/Autochek_6-11.txt'

def get_credentials_users(path) -> list:
    res = list()

    with open(path, 'rb') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            line = line.decode().replace('\n', '').replace('\r', '')
            print(line)
            res.append(line)
    return res

print(get_credentials_users(path))