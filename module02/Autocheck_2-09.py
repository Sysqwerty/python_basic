first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if (first < second) else second
while (first % gcd) or (second % gcd):
    gcd = gcd - 1



# На співбесідах часто люблять запитувати про алгоритми. Наприклад, розрахуйте найбільший спільний дільник (НД) двох додатних чисел. НСД — це найбільше число, на яке без залишку діляться обидва числа.

# Є кілька алгоритмів знаходження НСД, але ми розберемо циклічний алгоритм

# Хай є два початкових числа first та second.
# Виберемо менше з них та привласнимо значення змінній gcd.
# Поки first або second не діляться на gcd без залишку, треба виконувати цикл, в якому зменшуємо змінну gcd на одиницю.
# Коли цикл закінчиться в змінній gcd буде НСД для чисел first та second
# Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.

# Примітка: Для умови циклу в пункті 3 необхідно пам'ятати, що цикл while виконується за умови True, а наш цикл повинен закінчитися, тільки якщо gcd поділив обидва числа без залишку.