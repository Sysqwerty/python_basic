numbers = "1234567890"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lover = "abcdefghijklmnopqrstuvwxyz"


def is_valid_password(password: str) -> bool:
    def is_pass_length() -> bool:
        return len(password) == 8

    def is_there_nums() -> bool:
        for ch in password:
            if ch in numbers:
                return True
        return False

    def is_there_lover() -> bool:
        for ch in password:
            if ch in lover:
                return True
        return False

    def is_there_upper() -> bool:
        for ch in password:
            if ch in upper:
                return True
        return False

    return (
        is_there_nums() and is_pass_length() and is_there_lover() and is_there_upper()
    )


print(is_valid_password("z,qrE*IE"))


# Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

# Критерії надійного пароля:

# Довжина рядка пароля вісім символів.
# Містить хоча б одну літеру у верхньому регістрі.
# Містить хоча б одну літеру у нижньому регістрі.
# Містить хоча б одну цифру.
# Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False.
