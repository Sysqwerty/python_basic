def decode(encoded_list):
  if len(encoded_list) < 2:
    return []

  count = encoded_list[1]
  return [encoded_list[0]] * count + decode(encoded_list[2:])

print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))

# def decode(data:list):
#     res = list()
#     for i, val in enumerate(data):
#         if isinstance(val, str):
#             res.extend(val * (data[i + 1]))

#     return res