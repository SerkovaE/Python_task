# # Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# # return sum(a, b) + 1 - такое использовать нельзя
# # *Пример:* 2 ; 2 ; 4

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))

def sum(a,b):
    if b==0:
        return a
    if b>0:
        return sum(a+1,b-1)
print(sum(a,b))