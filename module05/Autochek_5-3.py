phones = ["    +38(050)123-32-34",
          "     0503451234",
          "(050)8889900",
          "38050-111-22-22",
          "38050 111 22 11   ",]


def sanitize_phone_number(phone:str):
    return phone.strip().replace('(', '').replace(')', '').replace('+', '').replace('-', '').replace(' ', '')

def fix_nunmbers(array):
    res = list()
    for i in array:
         res.append(sanitize_phone_number(i))
    return res
    
print(fix_nunmbers(phones))