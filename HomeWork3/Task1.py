# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2
size = int(input("Введите размер последовательности чисел: "))
numbers = []
count = 0
step = 0
while step < size:
    el = int(input(f"Введите {step +1}-й элемент: "))
    numbers.append(el)
    step += 1
find = int(input("Введите число для поиска: "))
for el in numbers:
    if el == find:
        count += 1
print(f"Количество повторений числа равно = {count}")