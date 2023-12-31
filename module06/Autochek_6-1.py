def total_salary(path):
    fh = open(path, 'r')
    total_salary = 0

    try:
        while True:
            line = fh.readline()
            if not line:
                break
            total_salary += float(line.split(',')[1])

    finally:
        fh.close()

    return total_salary

print(total_salary('module6/Autochek_6-1.txt'))



# Режим	Визначення
# 'r'	відкриття на читання (є значенням за замовчуванням).
# 'w'	відкриття на запис, вміст файлу видаляється, якщо файлу не існує, створюється новий.
# 'x'	відкриття на запис, якщо файлу не існує, інакше виключення.
# 'a'	відкриття на дозапис, інформація додається в кінець файлу.
# 'b'	відкриття у двоїчному режимі.
# 't'	відкриття в текстовому режимі (є значенням за замовчуванням).
# '+'	відкриття на читання та запис
