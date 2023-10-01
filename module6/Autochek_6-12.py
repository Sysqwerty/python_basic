import base64

data = ['andry:uyro18890D', 'steve:oppjM13LL9e']


def encode_data_to_base64(data:list):
    res = list()

    for d in data:
        d_bytes = d.encode("utf-8")
        base64_bytes = base64.b64encode(d_bytes)
        base64_d = base64_bytes.decode("utf-8")
        res.append(base64_d)
    
    return res


print(encode_data_to_base64(data))