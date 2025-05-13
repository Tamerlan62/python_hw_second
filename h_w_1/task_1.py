a = int(input('Введите ширину рамки: ')) # hundurluyu
b = int(input('Введите высоту рамки: ')) # eni

for elem in range(b + 1):
    for el in range(a + 1):
        if el == a or el == 0:
            print('|', end='')
        elif elem == b or elem == 0:
            print('-', end='')
        else:
            print(' ', end='')
    print()