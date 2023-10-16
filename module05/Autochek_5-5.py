phones = ["    +38(050)123-32-34",
          "     0503451234",
          "(050)8889900",
          "38050-111-22-22",
          "38050 111 22 11   ",
          "+812569548325",
          "+65236584216",
          "+8861111111"]

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    res = {
        'UA': list(),
        'JP': list(),
        'TW': list(),
        'SG': list(),
    }

    for phone in list_phones:
        phone = sanitize_phone_number(phone)

        if phone.startswith('81'):
            res['JP'].append(phone)
        elif phone.startswith('65'):
            res['SG'].append(phone)
        elif phone.startswith('886'):
            res['TW'].append(phone)
        else:
            res['UA'].append(phone)

    return res

print(get_phone_numbers_for_countries(phones))
