import random


def are_queens_safe(positions):
    """
    Проверяет, не бьют ли друг друга ферзи на доске 8x8.
    
    Аргументы:
    positions -- список кортежей (строка, столбец) для каждого ферзя.
    
    Возвращает:
    True, если ферзи не бьют друг друга; False в противном случае.
    """
    def is_under_attack(row, col):
        """
        Проверяет, атакуется ли позиция (row, col) другими ферзями.
        
        Аргументы:
        row -- строка ферзя
        col -- столбец ферзя
        
        Возвращает:
        True, если позиция под атакой; False в противном случае.
        """
        for i in range(len(positions)):
            if positions[i] == (row, col):
                continue
            r, c = positions[i]
            if r == row or c == col or abs(r - row) == abs(c - col):
                return True
        return False

    for row, col in positions:
        if is_under_attack(row, col):
            return False
    return True

def generate_random_queens_placement():
    """
    Генерирует случайную расстановку 8 ферзей (по одному в каждой строке).
    
    Возвращает:
    Список из 8 кортежей с координатами ферзей.
    """
    return [(i, random.randint(0, 7)) for i in range(8)]

def print_valid_placements(num_placements=4):
    """
    Выводит указанное количество корректных расстановок ферзей.
    
    Аргументы:
    num_placements -- количество правильных расстановок (по умолчанию 4).
    """
    count = 0
    while count < num_placements:
        placement = generate_random_queens_placement()
        if are_queens_safe(placement):
            print(f"Расстановка {count + 1}: {placement}")
            count += 1

# Пример запуска
if __name__ == "__main__":
    print_valid_placements()
