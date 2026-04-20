# Ввод двузначного числа
num = int(input("Введите двузначное число: "))

# Проверка, что число действительно двузначное
if 10 <= num <= 99:
    # Выделяем цифры
    first_digit = num // 10      # первая цифра (десятки)
    second_digit = num % 10      # вторая цифра (единицы)

    # а) Какая из цифр больше
    if first_digit > second_digit:
        print(f"Первая цифра ({first_digit}) больше второй ({second_digit})")
    elif second_digit > first_digit:
        print(f"Вторая цифра ({second_digit}) больше первой ({first_digit})")
    else:
        print(f"Цифры равны ({first_digit} = {second_digit})")

    # б) Одинаковы ли цифры
    if first_digit == second_digit:
        print("Цифры числа одинаковы")
    else:
        print("Цифры числа разные")
else:
    print("Ошибка: нужно ввести двузначное число (от 10 до 99)")
