from collections import Counter


def get_count_visits_from_ip(ips:list):
    count = Counter(ips)
    return count
    
print(get_count_visits_from_ip(["85.157.172.253", "85.157.172.253", "85.157.172.254"]))

def get_frequent_visit_from_ip(ips:list):
    count = Counter(ips)
    return count.most_common(1)[0]

print(get_frequent_visit_from_ip(["85.157.172.253", "85.157.172.253", "85.157.172.254"]))



# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1
# print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}

# ===> use collenstions ===>

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts.most_common(1))  # [(4, 4)]
# print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]

# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)
# print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})