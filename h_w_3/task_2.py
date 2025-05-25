"""
Задача 2. Поиск наибольшего числа в списке
Напишите программу, которая принимает список чисел через строку и
возвращает наибольшее число в этом списке.

"""

numbers = [int(x) for x in input('\n'"Введите числа через пробел: "'\n').split()]

max_number = numbers[0]

for el in numbers:
    if el > max_number:
        max_number = el
        
        
print(max_number)

