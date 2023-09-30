import re


def find_word(text: str, word: str) -> dict:
    res: re.Match = re.search(word, text)
    res_dict: dict = {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': word,
        'string': text
    }
    if res:
        res_dict['result'] = True
        res_dict['first_index'] = res.start()
        res_dict['last_index'] = res.end()

    return res_dict


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python"))