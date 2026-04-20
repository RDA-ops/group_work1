# Ввод трехзначного числа
three_digit_number = int(input("Введите трехзначное число: "))

# Проверка корректности ввода
if 100 <= three_digit_number <= 999:
    # Выделение цифр числа
    hundreds_digit = three_digit_number // 100          # цифра сотен
    tens_digit = (three_digit_number // 10) % 10        # цифра десятков
    units_digit = three_digit_number % 10               # цифра единиц
    
    # Вывод цифр для наглядности
    print(f"\nЧисло: {three_digit_number}")
    print(f"Цифра сотен: {hundreds_digit}")
    print(f"Цифра десятков: {tens_digit}")
    print(f"Цифра единиц: {units_digit}")
    print("-" * 50)
    
    # а) Проверка: все ли цифры одинаковые?
    all_digits_equal = (hundreds_digit == tens_digit == units_digit)
    
    if all_digits_equal:
        print(f"а) Верно: все цифры числа {three_digit_number} одинаковые.")
    else:
        print(f"а) Неверно: не все цифры числа {three_digit_number} одинаковые.")
    
    # б) Проверка: есть ли среди цифр одинаковые?
    has_duplicate_digits = (hundreds_digit == tens_digit or 
                            hundreds_digit == units_digit or 
                            tens_digit == units_digit)
    
    if has_duplicate_digits:
        print(f"б) Да, среди цифр числа {three_digit_number} есть одинаковые.")
        # Дополнительная информация: какие именно совпадают
        if hundreds_digit == tens_digit == units_digit:
            print("   Все три цифры одинаковы.")
        elif hundreds_digit == tens_digit:
            print(f"   Совпадают сотни и десятки: {hundreds_digit} и {tens_digit}.")
        elif hundreds_digit == units_digit:
            print(f"   Совпадают сотни и единицы: {hundreds_digit} и {units_digit}.")
        elif tens_digit == units_digit:
            print(f"   Совпадают десятки и единицы: {tens_digit} и {units_digit}.")
    else:
        print(f"б) Нет, среди цифр числа {three_digit_number} нет одинаковых (все цифры разные).")

else:
    print("Ошибка: нужно ввести трехзначное число (от 100 до 999).")