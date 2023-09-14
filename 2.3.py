import numpy

while 1:
    rows = input("Введите количество строк матрицы: ")
    if rows.isdigit():
        rows = int(rows)
        break
    else:
        print("Введите натуральное число")
while 1:
    columns = input("Введите количество столбцов матрицы: ")
    if columns.isdigit():
        columns = int(columns)
        break
    else:
        print("Введите натуральное число")
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        while True:
            try:
                element = float(input(f"Введите элемент матрицы [{i + 1}][{j + 1}]: "))
                break
            except ValueError:
                print("Введите число")
        row.append(element)
    matrix.append(row)
num = 0
for row in matrix:
    is_first_pos = 1
    for elem in row:
        if elem > 0 and is_first_pos:
            num += 1
            is_first_pos = 0
if num == rows:
    for row in matrix:
        for elem in row:
            print(-elem, end=' ')
        print()
else:
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()
