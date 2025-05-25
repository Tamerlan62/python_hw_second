import random       # Импортируем модуль random для генерации случайных чисел
import string       # Импортируем модуль string для работы со строками и символами

length = int(input("Введите длину пароля: "))       # Принимаем длину пароля от пользователя

# Определяем набор символов, из которых будет генерироваться пароль
# Включаем буквы (заглавные и строчные), цифры и специальные символы
characters = string.ascii_letters + string.digits + string.punctuation

# Генерируем случайный пароль заданной длины
# random.choice выбирает случайный символ из набора 'characters' для каждой позиции
password = ''.join(random.choice(characters) for i in range(length))
# Выводим сгенерированный пароль
print(password)