def split_list(grade):
    list_1 = []
    list_2 = []
    sum = 0

    def calculate_middle_grade():
        nonlocal sum
        res = 0
        for i in grade:
            sum += i
        try:
            res = sum / len(grade)
        except:
            res = 0
        return res

    middle_grade = calculate_middle_grade()

    for i in grade:
        if i <= middle_grade:
            list_1.append(i)
        else:
            list_2.append(i)

    return (list_1, list_2)


# У нас є список показників студентів групи – це список з отриманими балами з тестування. Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку та ділить його на два списки. У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
