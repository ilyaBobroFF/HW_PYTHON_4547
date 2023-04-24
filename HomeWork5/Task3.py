# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., 
# где: a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

number = int(input("Введите количество элементов: "))
def Fibo(n):
    if (n <= 1):
        return n
    else:
        return (Fibo(n-1) + Fibo(n-2))
list_fibo = []
for i in range(number):
    list_fibo.append(Fibo(i))
print(f"Последовательность Фибоначчи: {list_fibo}")    
