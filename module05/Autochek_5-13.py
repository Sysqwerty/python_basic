import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z][\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result

text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'

print(find_all_emails(text))


# . — будь-який символ, крім символу кінця рядка.
# \d — число або [0-9].
# \D — не число, або [^0-9].
# \s — будь-який символ, що позначає пробіл або табуляцію, перенесення рядка та ін.
# \w — будь-яке число або літера, включаючи нижнє підкреслення, або [a-zA-Z0-9_].
# \W — не буква, не число і нижнє підкреслення.
# \S — збігається із не пробільними символами.
# \b — збіги шукатимуться лише на межах слів (на початку або в кінці).
# \B — збіги шукатимуться тільки не на межах слів.
# \n — збігається із символом переводу рядка.
# ? 0 або 1 раз
# + 1 або більше разів
# * 0 або більше разів
# {n} суворо n разів (n ціле число)
# {n, m} від n до m разів
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fitforce.ua%2Fblog%2Freguljarnye-vyrazhenija%2F&psig=AOvVaw1fwjvUCWYxZRS995A6DT6y&ust=1696188580400000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLD9yv-I04EDFQAAAAAdAAAAABAJ