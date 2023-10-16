list_payment = [100, -3, 400, 35, -100]


# def positive_values(list_payment):
#     res = list()

#     for i in filter(lambda p: p > 0, list_payment):
#         res.append(i)

#     return res

def positive_values(list_payment):
    return list(filter(lambda p: p > 0, list_payment))


print(positive_values(list_payment))



# Filter

# for i in filter(lambda x: x % 2, range(1, 10 + 1)):
#     print(i)

# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.islower(), some_str):
#     print(i)