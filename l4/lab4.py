import re

'''Лабораторная работа №4
Написать программу, которая читая символы из файла, распознает, преобразует
 и выводит на экран объекты по определенному правилу. Объекты разделены пробелами.
Распознавание и преобразование делать по возможности через регулярные выражения.
Для упрощения под выводом числа прописью подразумевается последовательный
вывод всех цифр числа.

Вариант 19.
Натуральные нечетные восьмеричные числа, начинающиеся с 3.
Для каждого числа повторяющиеся цифры вывести прописью.'''
inter = {
    '1': 'один',
    '3': 'три',
    '5': 'пять',
    '7': 'семь',
}


def transform_number(match):
    num = match.group(0)
    dc = {}
    trans = []
    for d in num:
        if d in dc and d in inter:
            trans.append(inter[d])
        else:
            trans.append(d)
            dc[d] = 1

    return ''.join(trans)

def proc(path):
    octal_number_pattern = r'\b3[0-7]+\b'
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            # Заменяем каждое восьмеричное число, подходящее под условия
            transformed_line = re.sub(octal_number_pattern, transform_number, line)
            res.append(transformed_line.strip())
    for r in res:
        print(r)

proc('inp.txt')