def maximum(a):
    m = -100000
    for i in range(len(a)):
        if a[i] > m:
            m=a[i]
    return m

print("Введи размерность массива: ")
n = int(input())
a = [0] * n
print("Введи n чисел массива: ")
for i in range(n):
    a[i] = float(input())
print("Входной массив: ", a)

zamena = a.index(maximum(a)) + 1
a[zamena:] = [0] * (len(a) - zamena)
print("Результат: ", a)
