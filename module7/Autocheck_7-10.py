def make_request(keys, values):
    res = {}

    if len(keys) == len(values):
        for i in range(len(keys)):
            res[keys[i]] = values[i]
    
    return res