import re


def replace_spam_words(text: str, spam_words: list) -> str:
    res = text

    for spam_word in spam_words:
        res = re.sub(spam_word, '*'*len(spam_word), res, re.IGNORECASE)
    
    return res


print(replace_spam_words(
    'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))


# p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes', re.IGNORECASE)
# print(p)  # color socks and color shoes
