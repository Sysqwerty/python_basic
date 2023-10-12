from collections import UserString
import re


class NumberString(UserString):
    def __init__(self, string):
        self.string = string
    
    def number_count(self):
        return len(re.findall(r'\d', self.string))

num = NumberString("s1d2f333")
print(num.number_count())