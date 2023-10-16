def encode(data):
    if not data:
        return []

    current_element = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_element:
            count += 1
        else:
            break

    encoded_data = [current_element, count]
    remaining_data = data[count:]
    return encoded_data + encode(remaining_data)

data =  ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z'] # ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]

print(encode(data))