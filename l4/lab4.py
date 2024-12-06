"""Написать программу, которая читая символы из файла, распознает,преобразует и выводит на экран объекты по определенному правилу.
 Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения.
 Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
 Вариант 19.
Натуральные нечетные восьмеричные числа, начинающиеся с 3. Для каждого числа повторяющиеся цифры вывести прописью."""
import re
inter = {
    '1': 'один',
    '3': 'три',
    '5': 'пять',
    '7': 'семь',
}
def transform_number(num):
    dc = {}
    trans = []
    for d in num:
        if d in dc and d in inter:
            trans.append(inter[d])
        else:
            trans.append(d)
            dc[d] = 1
    result = ''.join(trans)
    return result 
def proc(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'(?<!-)\b3[0-7]*[1357]\b', line)  
            result = ' '.join(transform_number(word) for word in words)
            if result:
                print(result.strip())
proc('text.txt')
