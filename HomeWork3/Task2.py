# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

size = int(input("Введите количество элементов: "))
numbers = []
step = 0
while step < size:
    el = int(input(f"Введите {step +1}-й элемент: "))
    numbers.append(el)
    step += 1
check = int(input("Введите число для проверки: "))
minDelta = abs(numbers[0] - check)
find = numbers[0]
for el in numbers:
    delta = abs(el - check)
    if delta < minDelta:
        minDelta = delta
        find = el
print(f"Ближайшее число к {check} это - {find}")