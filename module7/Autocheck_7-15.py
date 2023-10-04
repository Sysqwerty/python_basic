def flatten(data):
    # Якщо вхідний список порожній, повертаємо порожній список
    if not data:
        return []

    # Ініціалізуємо результат пустим списком
    result = []

    for item in data:
        if isinstance(item, list):
            # Якщо поточний елемент є списком, рекурсивно викликаємо функцію flatten для нього
            result.extend(flatten(item))
        else:
            # Якщо поточний елемент не є списком, додаємо його до результату
            result.append(item)

    return result

# Приклад використання:
nested_list = [1, 2, [3, 4, [5, 6]], 7]
flat_list = flatten(nested_list)
print(flat_list)