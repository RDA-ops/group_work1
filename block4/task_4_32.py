# Ввод четырехзначного числа
num = int(input("Введите четырехзначное число: "))

# Проверка, что число действительно четырехзначное
if 1000 <= num <= 9999:
    # Выделяем цифры
    thousands = num // 1000          # первая цифра (тысячи)
    hundreds = (num // 100) % 10     # вторая цифра (сотни)
    tens = (num // 10) % 10          # третья цифра (десятки)
    units = num % 10                 # четвертая цифра (единицы)
    
    # Суммы цифр
    sum_first_two = thousands + hundreds      # сумма первых двух цифр
    sum_last_two = tens + units               # сумма последних двух цифр
    total_sum = thousands + hundreds + tens + units   # сумма всех цифр
    
    # Произведение всех цифр
    product = thousands * hundreds * tens * units
    
    # Вывод информации о числе
    print(f"\nЧисло: {num}")
    print(f"Цифры: {thousands}, {hundreds}, {tens}, {units}")
    print(f"Сумма первых двух цифр: {sum_first_two}")
    print(f"Сумма последних двух цифр: {sum_last_two}")
    print(f"Сумма всех цифр: {total_sum}")
    print(f"Произведение всех цифр: {product}")
    print("-" * 40)
    
    # а) Равна ли сумма двух первых цифр сумме двух последних
    if sum_first_two == sum_last_two:
        print(f"а) Сумма первых двух цифр ({sum_first_two}) равна сумме последних двух ({sum_last_two})")
    else:
        print(f"а) Сумма первых двух цифр ({sum_first_two}) не равна сумме последних двух ({sum_last_two})")
    
    # б) Кратна ли трем сумма всех цифр
    if total_sum % 3 == 0:
        print(f"б) Сумма цифр ({total_sum}) кратна 3")
    else:
        print(f"б) Сумма цифр ({total_sum}) не кратна 3")
    
    # в) Кратно ли четырем произведение цифр
    if product % 4 == 0:
        print(f"в) Произведение цифр ({product}) кратно 4")
    else:
        print(f"в) Произведение цифр ({product}) не кратно 4")
    
    # г) Кратно ли произведение цифр числу а
    a = int(input("\nВведите число a: "))
    
    if a == 0:
        print("г) На ноль делить нельзя!")
    elif product % a == 0:
        print(f"г) Произведение цифр ({product}) кратно числу {a}")
    else:
        print(f"г) Произведение цифр ({product}) не кратно числу {a}")
else:
    print("Ошибка: нужно ввести четырехзначное число (от 1000 до 9999)")