from random import randrange


def get_numbers_ticket(min, max, quantity):
    res = []
    if min < quantity and quantity < max and min >=1 and max <=1000:
        while len(res) < quantity:
            random_int = randrange(min, max)
            if random_int not in res:
                res.append(random_int)
        res.sort()
    return res
    

print(get_numbers_ticket(1, 100, 5))