def mat_cr():
    size = 0
    mat = []
    with open('mat.txt', 'r') as f:
        for line in f:
            row = list(map(int, line.split(',')))
            mat.append(row)
            size += 1
    return mat,size
def mat_part(mat, size, ar,k = 0, ce=False):
    area = []
    pros = 1
    isK = 0

    for i in range(size):
        for j in range(size):
            if in_area(i, j, size, ar):
                area.append(mat[i][j])
                if ce:
                    if ar == 1 and j % 2 == 0 and mat[i][j] == k:
                        isK += 1
                    if ar == 4 and j % 2 != 0:
                        pros *= mat[i][j]
    if ce:
        return area, isK if ar == 1 else pros
    return area
def in_area(i, j, size, ar):
    if ar == 1:
        return i > j and i + j < size - 1
    elif ar == 2: 
        return i < j and i + j < size - 1
    elif ar == 3:  
        return i < j and i + j > size - 1
    elif ar == 4:  
        return i > j and i + j > size - 1
    return False
def f_create(mat, size, result,part1, part2, part3 ):
    if result > 0:  
        replacer(mat, size, part3, 2)
        replacer(mat, size, part2, 3)
    else:  
        part1 = list(reversed(part1))
        part2 = sorted(part2)
        replacer(mat, size, part2, 1)
        replacer(mat, size, part1, 2)
    return mat
def replacer(mat, size, new_values, ar):
    idx = 0
    for i in range(size):
        for j in range(size):
            if in_area(i, j, size, ar):
                mat[i][j] = new_values[idx]
                idx += 1
def ex(a,f,k,size):
    """(k*(A*F))*Ft"""
    print("Матрица Ft:")
    ft = [[f[j][i] for j in range(size)] for i in range(size)]
    print_mat(ft,size)
    print("A*F:")
    amultf = [[a[i][j] * f[i][j] for i in range(size)] for j in range(size)]
    print_mat(amultf,size)
    print("k*(A*F): ")
    kmultaf = [[k * amultf[i][j] for i in range(size)] for j in range(size)]
    print_mat(kmultaf,size)
    print("(k*(A*F))*Ft")
    answer = [[kmultaf[i][j] * ft[i][j] for i in range(size)] for j in range(size)]
    print_mat(answer,size)
def print_mat(m,s):
    for i in range(s):
        print(m[i])
k = int(input("Введите коэффицент: "))
a,size = mat_cr()
print("Матрица А: ")
print_mat(a,size)
print(f"Размер матрицы: {size}")
print("Матрица F:")
f = a.copy()
p1, isK = mat_part(f,size,1,k,ce=True)
p2 = mat_part(f,size,2)
p3 = mat_part(f,size,3)
_, pros = mat_part(f,size,4,ce=True)
f = f_create(f,size,isK-pros,p1,p2,p3)
print_mat(f,size)
print("Решаем пример (k*(A*F))*Ft")
ex(a,f,k,size)
