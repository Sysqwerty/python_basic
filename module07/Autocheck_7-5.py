def capital_text(s):
    result = ''
    capitalize_next = True

    for char in s:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char.lower()
        else:
            if char == '.' or char == '!' or char == '?':
                capitalize_next = True
            result += char

    return result


print(capital_text(' its a . n!ew . so ? me. thing '))