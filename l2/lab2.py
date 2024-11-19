import numpy as np
import matplotlib.pyplot as plt

"""Задание на матрицы №2
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10]. Для отладки использовать
не случайное заполнение, а целенаправленное (ввод из файла и генератором). 

На основе матрицы А формируется матрица  F. 
По матрице F необходимо вывести не менее 3 разных графика. 
Программа должна использовать функции библиотек numpy и matplotlib.

Вариант 19.	Формируется матрица F следующим образом: скопировать в нее А и если в Е 
количество нулей в нечетных столбцах, умноженное на К больше, чем произведение 
чисел в нечетных строках, то поменять местами В и С симметрично, иначе В и Е 
поменять местами несимметрично после чего если 
определитель матрицы А больше суммы диагональных элементов матрицы F, то 
вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-FТ)*K, 
где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А,
 F и все матричные операции последовательно"""


def create_submatrixes_random(s):
    return np.random.randint(-10,10,size=(s,s))

def create_submatrixes_gen(s,num):
    return np.full((s,s),num)

def create_submatrixes_txt():
    with open('text.txt', 'r') as file:
        lines = file.readlines()
        
    matrices = []
    current_matrix = []

    for line in lines:
        if line.strip():
            current_matrix.append([int(num) for num in line.split()])
        else:
            if current_matrix:
                matrices.append(np.array(current_matrix))
                current_matrix = []

    if current_matrix:
        matrices.append(np.array(current_matrix))

    return matrices

def create_matrix_from_sub(b,c,d,e):
    return np.concatenate((np.concatenate((b,e),axis=1),np.concatenate((c,d), axis=1)), axis=0)


def search_zeros(sub,k):
    zerok = 0
    pros = 1
    for i in range(len(sub)):
        for j in range(len(sub)):
            if j % 2 == 0 and sub[i][j] == 0:
                zerok += 1
            if i % 2 != 0:
                pros *= sub[i][j]
    return zerok * k > pros

def createF(b,c,e,d,k):
    if search_zeros(e,k):
        return np.concatenate((np.concatenate((c,e),axis=1),np.concatenate((b,d), axis=1)), axis=0)
    else:
        return np.concatenate((np.concatenate((e,np.sort(b)),axis=1),np.concatenate((c,d), axis=1)), axis=0)


def expr(a,f,k):
    at = np.transpose(a)
    ft = np.transpose(f)
    f_in = np.linalg.inv(f)
    a_in = np.linalg.inv(a)
    g = np.tril(a)
    if np.linalg.det(a) > (sum(np.diagonal(f)) + sum(np.fliplr(f).diagonal())):
        print("A*AT – K * F-1")
        answer = (a*at) - (k * f_in)
        print(answer)
        return answer
    else:
        print("(A-1 +G-FТ)*K")
        answer = (a_in + g - ft )* k
        print(answer)
        return answer
def plots(m):
    col = np.mean(m, axis=0)
    plt.figure(figsize=(6, 4))
    plt.plot(np.arange(len(col)), col)
    plt.title("Среднее значение по столбцам матрицы")
    plt.grid(True)
    row_sum = np.sum(m, axis=1)
    plt.figure(figsize=(6, 4))
    plt.plot(np.arange(len(row_sum)), row_sum)
    plt.title("Сумма значений по строкам матрицы")
    plt.grid(True)
    plt.figure(figsize=(6, 4))
    plt.imshow(m, cmap='plasma', interpolation='nearest')
    plt.colorbar(label='Значения матрицы')
    plt.title("Тепловая карта")
    plt.show()
def print_mat(m):
    [print(m[i]) for i in range(len(m))]
    print("")

print("Создание матрицы")
print("1 Заполнение случайными числами")
print("2 Заполнение с помощью генератора")
print("3 Заполнение из файла .txt")
choice = int(input(": "))
while True:
    if choice == 1:
        try:
            s = int(input("Введите размер подматриц :"))
            b = create_submatrixes_random(s);c = create_submatrixes_random(s)
            d = create_submatrixes_random(s);e = create_submatrixes_random(s)
            break
        except:
            print("Введены неверные данные")
    elif choice == 2:
        try:
            s = int(input("Введите размер подматриц"))
            num = []
            for i in range(4):
                
                temp = int(input(f"Какими числами будет заполнена {i+1}-я подматрица"))
                num.append(temp)
            b = create_submatrixes_gen(s,num[0]);c = create_submatrixes_gen(s,num[1])
            d = create_submatrixes_gen(s,num[2]);e = create_submatrixes_gen(s,num[3])
            break
        except:
            print("Введены неверные данные")
    elif choice == 3:
        try:
            b = create_submatrixes_txt()[0]
            c = create_submatrixes_txt()[1]
            d = create_submatrixes_txt()[2]
            e = create_submatrixes_txt()[3]
        except:
            print("Возникли проблемы с чтением файла")
    else:
        print("Неверный выбор")
        exit(0)
try:
    k = int(input("Введите коэффицент: "))
    print("Ваши подматрицы")
    print_mat(b),print_mat(c),print_mat(d),print_mat(e)
    print("Матрица А")
    a = create_matrix_from_sub(b,c,d,e)
    print_mat(a)
    print("Матрица F")
    f = createF(b,c,d,e,k)
    print_mat(f)
    print("Решаем пример")
    answer = expr(a,f,k)
    plots(answer)
except:
    print("Возникли проблемы в связи с вводом неверных данных")
