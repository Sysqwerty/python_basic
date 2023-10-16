def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None

res = get_student_grade("grade")("A")
print(res)






# можемо передавати функцію як аргументи для інших функцій;

#   def sum_func(x, y):
#       return x + y

#   def subtraction_func(x, y):
#       return x - y

#   def tricky_func(x, y, func):
#       return func(x, y)

#   sum_result = tricky_func(2, 3, sum_func)
#   min_result = tricky_func(2, 3, subtraction_func)

#   print(sum_result)  # 5
#   print(min_result)  # -1

# ---------------------------------------------------

# можемо повертати з функції інші функції.

#   def sum_func(x, y):
#       return x + y

#   def subtraction_func(x, y):
#       return x - y

#   def get_operator(operator):
#       if operator == '+':
#           return sum_func
#       elif operator == '-':
#           return subtraction_func
#       else:
#           print('Unknown operator')

#   sum_action_function = get_operator("+")
#   print(sum_action_function(2, 3))    # 5

#   sub_action_function = get_operator("-")
#   print(sub_action_function(2, 3))    # -1