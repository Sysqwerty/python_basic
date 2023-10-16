def format_phone_number(func) -> str:
    def inner(phone) -> str:
        old_format:str = func(phone)
        if len(old_format) >= 12:
            return f"+{old_format}"
        return f"+38{old_format}"
    return inner

@format_phone_number
def sanitize_phone_number(phone:str) -> str:
    new_phone:str = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

# print(sanitize_phone_number("+38(050)123-32-34"))
print(sanitize_phone_number("(050)8889900"))