cache = {}

def caching_fibonacci():
    global cache

    def fibonacci(n):
        # print(f"n: {n}")
        if n in cache.keys():
            return cache.get(n)
        else:
            if n == 0:
                return 0
            if n <= 2:
                return 1
        res = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = res
        print(cache)
        return res
    return fibonacci

print(caching_fibonacci()(5))
print(caching_fibonacci()(6))
print(caching_fibonacci()(5))

# def adder(val):
#     def inner(x):
#         return x + val
#     return inner


# two_adder = adder(2)
# print(two_adder(3)) # 5
# print(two_adder(5)) # 7

# three_adder = adder(3)
# print(three_adder(5))   # 8
# print(three_adder(-3))  # 0

# id(two_adder) == id(three_adder)    # False
