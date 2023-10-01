import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"https?:\/\/\w+\.?\w+\.\w+", text)
    for match in iterator:
        result.append(match.group())
    return result

print(find_all_links('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com'))






# regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"

# test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"

# matches = re.finditer(regex, test_str)

# for match in matches:
#     print(f"{match.group()} start: {match.start()} end: {match.end()}")