import random

P = []  # Глобальна змінна для населення

def gener_matr(a, b):
    """Генерує матрицю випадкових значень"""
    return [[random.randint(100, 1000) for _ in range(b)] for _ in range(a)]

def print_matr(A):
    """Виводить матрицю"""
    for row in A:
        print(' '.join(map(str, row)))

def gener_matr_crime(A):
    """Генерує матрицю злочинності на основі населення"""
    a = len(A)
    b = len(A[0])
    Y = [[(A[i][j] * 10**4) // P[i] for j in range(b)] for i in range(a)]
    return Y

def find_summ(Y):
    """Обчислює суму по стовпцях"""
    return [sum(row[j] for row in Y) for j in range(len(Y[0]))]

def max_list(S):
    """Знаходить максимум у списку"""
    max_i = S.index(max(S))
    return max(S), max_i

def work_with_matrices(a, b):
    """Основна функція роботи з матрицями"""
    global P
    P = [random.randint(50000, 60000) for _ in range(a)]
    
    A = gener_matr(a, b)
    print("\nМатриця:")
    print_matr(A)

    Y = gener_matr_crime(A)
    print("\nМатриця злочинності:")
    print_matr(Y)

    S = find_summ(Y)
    print("\nСума стовпців:", S)

    max_value, max_i = max_list(S)
    print("\nМаксимальне значення:", max_value)
    print("\nРік з максимальною злочинністю:", max_i + 2005)