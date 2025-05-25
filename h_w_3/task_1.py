""""
Задание 1. Удаление дубликатов из списка
Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.

"""


elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]

unique_list = []

for elem in elements:
    if elem not in unique_list:
        unique_list.append(elem)
        
print(unique_list)