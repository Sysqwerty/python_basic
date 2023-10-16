from functools import reduce


numbers = [3, 4, 6, 9, 34, 12]

def sum_numbers(numbers):
    return reduce((lambda x, y: x + y), numbers)


print(sum_numbers(numbers))


# Reduce

# from functools import reduce
# result = reduce((lambda x, y: x * y), [1, 2, 3, 4], 3)
# print(result)  # 72

# reduce(func, iterable[, initial])
