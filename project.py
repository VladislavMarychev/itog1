# Ввод исходного массива с клавиатуры
array = input("Введите массив строк через пробел: ").split()

# Создание пустого массива для новых строк
new_array = []

# Перебираем каждую строку в исходном массиве
for string in array:
    # Проверяем длину строки
    if len(string) <= 3:
        # Добавляем строку в новый массив
        new_array.append(string)

# Вывод нового массива строк
print("Новый массив из строк, длина которых меньше или равна 3 символам:")
print(new_array)