'''Лабораторная работа №4
Написать программу, которая читая символы из файла, распознает, преобразует
 и выводит на экран объекты по определенному правилу. Объекты разделены пробелами.
Распознавание и преобразование делать по возможности через регулярные выражения.
Для упрощения под выводом числа прописью подразумевается последовательный
вывод всех цифр числа.
Вариант 19.
Натуральные нечетные восьмеричные числа, начинающиеся с 3.
Для каждого числа повторяющиеся цифры вывести прописью.'''


import re

inter = {
    '1': 'один',
    '3': 'три',
    '5': 'пять',
    '7': 'семь',
}

def valid(word):
    return bool(re.match(r'^-?[3][0-7]*$', word)) and int(word.lstrip('-'), 8) % 2 == 1

def transform_number(num):
    dc = {}
    trans = []
    is_negative = num[0] == '-' 
    if is_negative:
        num = num[1:]  
    for d in num:
        if d in dc and d in inter:
            trans.append(inter[d])
        else:
            trans.append(d)
            dc[d] = 1
    result = ''.join(trans)
    if is_negative:
        result = '-' + result  
    return result 

def proc(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'-?[0-7]+\b', line)
            result = ' '.join(transform_number(word) for word in words if valid(word))
            if result:
                print(result.strip()) 

proc('l4/inp.txt')
