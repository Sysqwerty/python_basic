import re
string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."


def generator_numbers(string=""):
    numbers = re.findall(r"\d+", string)
    numbers = [int(n) for n in numbers]
    for n in numbers:
        yield n


def sum_profit(string):
    res = []
    numbers = re.findall(r"\d+", string)
    numbers = [int(n) for n in numbers]
    # for i in map(lambda n: int(n), numbers):
    #     res.append(i)

    return sum(numbers)

# for i in generator_numbers(string):
#     print(i)


print(sum_profit(string))


# Ітератори та генератори

# def interval_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1

# five_to_ten_generator = interval_generator(5, 10)

# next(five_to_ten_generator) # 5
# next(five_to_ten_generator) # 6
# next(five_to_ten_generator) # 7
# next(five_to_ten_generator) # 8
# next(five_to_ten_generator) # 9
# next(five_to_ten_generator) # 10

# ------------------------------------------------

# def interval_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1

# five_to_ten_generator = interval_generator(5, 10)
# for i in five_to_ten_generator:
#     print(i)
