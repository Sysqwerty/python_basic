from functools import reduce


payment = [1, -3, 4]


def amount_payment(payment):
    return reduce(lambda x, y: x + y, list(filter((lambda x: x > 0), payment)))


print(amount_payment(payment))
