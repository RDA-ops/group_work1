# Ввод трехзначного числа
number = int(input("Введите трехзначное число: "))

# Проверяем, что число действительно трехзначное (100-999)
if 100 <= number <= 999:
    # Находим цифры числа
    hundreds = number // 100      # цифра сотен
    tens = (number // 10) % 10    # цифра десятков
    units = number % 10           # цифра единиц

    # Вычисляем квадрат числа
    square = number ** 2

    # Вычисляем сумму кубов цифр
    sum_of_cubes = hundreds**3 + tens**3 + units**3

    # Проверяем равенство
    if square == sum_of_cubes:
        print(f"Да, квадрат числа {number} ({square}) равен сумме кубов"
              "его цифр ({sum_of_cubes}).")
    else:
        print(f"Нет, квадрат числа {number} ({square}) НЕ равен сумме кубов"
              "его цифр ({sum_of_cubes}).")

    # Дополнительный вывод для наглядности
    print(f"Цифры числа: {hundreds}, {tens}, {units}")
    print(f"Куб {hundreds}³ = {hundreds**3}")
    print(f"Куб {tens}³ = {tens**3}")
    print(f"Куб {units}³ = {units**3}")
    print(f"Сумма кубов = {sum_of_cubes}")
    print(f"Квадрат числа = {square}")

else:
    print("Ошибка: нужно ввести трехзначное число (от 100 до 999).")
