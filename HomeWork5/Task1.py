# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
number = int(input("Введите число N: "))
def Factorial (n):
    if n == 1: return 1
    else: return n * Factorial(n-1)
print(f"Факториал числа {number} равен: {Factorial(number)}")
