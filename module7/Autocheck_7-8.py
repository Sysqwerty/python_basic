import re

s = "2+ 34-5 * 3" #['2', '+', '34', '-', '5', '*', '3']

def token_parser(s):
    res = re.findall(r"\d+|[\(\)\+\-\*\/]", s)
    print(res)
    return res

token_parser(s)