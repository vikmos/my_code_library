"""Функция возвращает массив чисел Фибоначчи заданной длины. Начинающихся с 0"""

def fibonachi(n: int) -> list:
    result = []
    a = 0
    b = 1
    for _ in range(n):
        if _ == a:
            result.append(a)
        else:
            a, b = b, a + b
            result.append(a)
    return result

print(fibonachi(9))
