users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
path = 'module6/Autochek_6-10.txt'


def save_credentials_users(path, users_info: dict):
    rows = list()

    with open(path, 'wb') as fh:
        for k,v in users_info.items():
            rows.append(bytes(f'{k}:{v}\n', encoding = 'utf-8'))
            
        fh.writelines(rows)

save_credentials_users(path, users_info)