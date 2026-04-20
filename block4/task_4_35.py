# Ввод размеров стола
print("Введите размеры стола (a > b):")
table_long_side = int(input("Длинная сторона a: "))
table_short_side = int(input("Короткая сторона b: "))

# Корректировка, если условие a > b нарушено
if table_long_side < table_short_side:
    table_long_side, table_short_side = table_short_side, table_long_side
    print(f"(Примечание: стороны стола автоматически скорректированы: {table_long_side} x {table_short_side})")

# Ввод размеров прямоугольника
print("\nВведите размеры прямоугольника (c > d):")
rect_long_side = int(input("Длинная сторона c: "))
rect_short_side = int(input("Короткая сторона d: "))

# Корректировка, если условие c > d нарушено
if rect_long_side < rect_short_side:
    rect_long_side, rect_short_side = rect_short_side, rect_long_side
    print(f"(Примечание: стороны прямоугольника автоматически скорректированы: {rect_long_side} x {rect_short_side})")

# Проверка возможности размещения
if rect_long_side > table_long_side or rect_short_side > table_short_side:
    print("\nВнимание: Прямоугольник не помещается на стол ни при каком размещении!")
    print(f"Нужно, чтобы {rect_long_side} ≤ {table_long_side} И {rect_short_side} ≤ {table_short_side}")
else:
    # Расчет количества для каждого варианта
    # Вариант 1: длинная сторона прямоугольника вдоль длинной стороны стола
    count_option1 = (table_long_side // rect_long_side) * (table_short_side // rect_short_side)
    
    # Вариант 2: длинная сторона прямоугольника вдоль короткой стороны стола
    count_option2 = (table_long_side // rect_short_side) * (table_short_side // rect_long_side)
    
    # Вывод результатов
    print("\n" + "=" * 50)
    print(f"Размеры стола: {table_long_side} x {table_short_side}")
    print(f"Размеры прямоугольника: {rect_long_side} x {rect_short_side}")
    print("=" * 50)
    print(f"Вариант 1 (вдоль длинной стороны): {count_option1} шт.")
    print(f"Вариант 2 (вдоль короткой стороны): {count_option2} шт.")
    print("=" * 50)
    
    if count_option1 > count_option2:
        print(f"\nОтвет: Лучше размещать длинной стороной вдоль ДЛИННОЙ стороны стола.")
        print(f"(Можно разместить {count_option1} прямоугольников, что на {count_option1 - count_option2} больше.)")
    elif count_option2 > count_option1:
        print(f"\nОтвет: Лучше размещать длинной стороной вдоль КОРОТКОЙ стороны стола.")
        print(f"(Можно разместить {count_option2} прямоугольников, что на {count_option2 - count_option1} больше.)")
    else:
        print(f"\nОтвет: Оба способа одинаковы — по {count_option1} прямоугольников.")