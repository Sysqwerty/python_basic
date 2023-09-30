articles_dict:list = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key:str, letter_case=False):
    res = list()
    for i in articles_dict:
        text_in_title:str = i['title']
        text_in_author:str = i['author']

        if letter_case == False:
            text_in_title = text_in_title.lower()
            text_in_author = text_in_author.lower()
            key = key.lower()

        if (text_in_title.find(key) >= 0) or (text_in_author.find(key) >= 0):
            res.append(i)
    return res

print(find_articles('Ocean'))