from decimal import Decimal, getcontext


def decimal_average(number_list:list, signs_count:int):
    getcontext().prec = signs_count
    dec_list = [Decimal(i) for i in number_list]
    average = sum(dec_list) / Decimal(len(number_list))
    return average


print(decimal_average([3, 5, 77, 23, 0.57], 6)) # 21.714

# print(decimal_average([31, 55, 177, 2300, 1.57], 9)) # 512.91400