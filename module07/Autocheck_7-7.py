list_data = [[1,2,3],[3,4], [5,6]]

def data_preparation(list_data:list):
    res_list = list()

    for i in list_data:
        if len(i) > 2:
            i.remove(min(i))
            i.remove(max(i))
        res_list.extend(i)
    res_list.sort()
    res_list.reverse()
    return res_list

print(data_preparation(list_data))




# Давайте повторимо методи списків

# Додавання елементу в кінець списку: my_list.append(element)

# chars = ['a', 'b']
# chars.append('c')
# print(chars)  # ['a', 'b', 'c']
# видалення елементу зі списку викличе помилку, якщо такого елементу немає в списку: my_list.remove(element)

# chars = ['a', 'b']
# chars.remove('b')
# print(chars)  # ['a']
# Повернути i-ий елемент та видалити його зі списку i_element = my_list.pop(i). За замовчуванням i = -1

# chars = ['a', 'b']
# last = chars.pop(1)
# print(chars)  # ['a']
# print(last)  # 'b'
# Розширити список a_list елементами із b_list: a_list.extend(b_list)

# chars = ['a', 'b']
# numbers = [1, 2]

# chars.extend(numbers)
# print(chars)  # ['a', 'b', 1, 2]
# Вставити x на позицію з індексом i: my_list.insert(i, x)

# chars = ["a", "b"]
# chars.insert(1, "c")
# print(chars)  # ['a', 'c', 'b']
# Очистити список: my_list.clear()

# chars = ['a', 'b']
# last =  chars.clear() print(chars) # []
# Знайти індекс першого елемента у списку рівного x: index = my_list.index(x)

# chars = ['a', 'b', 'c', 'd']
# c_ind = chars.index('c') print(c_ind) # 2
# Повернути кількість елементів у списку рівних x: x_number = my_list.count(x)

# chars = ['a', 'b', 'c', 'a']
# a_count = chars.count('a')
# print(a_count) # 2
# Відсортувати список за зростанням: my_list.sort(key=None, reverse=False)

# chars = ['z', 'a', 'b']
# chars.sort()
# print(chars) # ['a', 'b', 'z']
# Змінити порядок елементів у списку на зворотний: my_list.reverse()

# chars = ['a', 'b']
# chars.reverse()
# print(chars) # ['b', 'a']
# Повернути копію списку: copy_of_my_list = my_list.copy()

# chars =  ['a', 'b']
# chars_copy = chars.copy()
# chars == chars_copy # True