data = [4, 6, 1, 3]

def all_sub_lists(data:list):
    res = [[]]

    for i in range(len(data)):
        current_sublist = []
        for j in range(i, len(data)):
            current_sublist.append(data[j])
            res.append(current_sublist.copy())

    res.sort(key=len)
    return res


print(all_sub_lists(data))