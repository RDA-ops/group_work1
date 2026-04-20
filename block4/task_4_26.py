# Ввод двузначного числа
num = int(input("Введите двузначное число: "))

# Проверка, что число действительно двузначное
if 10 <= num <= 99:
    # Выделяем цифры
    first_digit = num // 10      # первая цифра (десятки)
    second_digit = num % 10      # вторая цифра (единицы)
    
    # Сумма цифр
    digit_sum = first_digit + second_digit
    
    print(f"Число: {num}")
    print(f"Цифры: {first_digit} и {second_digit}")
    print(f"Сумма цифр: {digit_sum}")
    print("-" * 30)
    
    # а) Кратна ли трём сумма его цифр
    if digit_sum % 3 == 0:
        print(f"а) Сумма цифр ({digit_sum}) кратна 3")
    else:
        print(f"а) Сумма цифр ({digit_sum}) не кратна 3")
    
    # б) Кратна ли сумма его цифр числу а
    a = int(input("Введите число a: "))
    
    if a == 0:
        print("б) На ноль делить нельзя!")
    elif digit_sum % a == 0:
        print(f"б) Сумма цифр ({digit_sum}) кратна числу {a}")
    else:
        print(f"б) Сумма цифр ({digit_sum}) не кратна числу {a}")
else:
    print("Ошибка: нужно ввести двузначное число (от 10 до 99)")
