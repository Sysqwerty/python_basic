import sys


def parse_args():
    argvs = sys.argv
    argvs.remove(argvs[0])
    return " ".join(argvs)


# Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, розділених пробілами. Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція parse_args повинна повернути рядок наступного виду 'first second'.