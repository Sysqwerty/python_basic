from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    return lifo.appendleft(element)


def pop():
    return lifo.popleft()











# from collections import deque

# d = deque()
# d.append('last')
# d.appendleft('first')
# d.insert(1, 'middle')
# print(d)  # deque(['first', 'middle', 'last'])

# print(d.pop())  # 'last'
# print(d.popleft())  # 'first'
# print(d)  # deque(['middle'])


# d = deque(maxlen=5)
# for i in range(10):
#     d.append(i)

# print(d)  # deque([5, 6, 7, 8, 9], maxlen=5)