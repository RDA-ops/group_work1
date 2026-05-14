num = int(input("Введите трёхзначное число: "))

if 100 <= abs(num) <= 999:
    # Задача (а)
    digits = [abs(num) // 100, (abs(num) // 10) % 10, abs(num) % 10]
    if 6 in digits:
        print("а) Цифра 6 входит в число")
    else:
        print("а) Цифра 6 не входит в число")

    # Задача (б)
    n = int(input("б) Введите цифру n (0–9): "))
    if 0 <= n <= 9:
        if n in digits:
            print(f"б) Цифра {n} входит в число")
        else:
            print(f"б) Цифра {n} не входит в число")
    else:
        print("Ошибка: n должно быть от 0 до 9")
else:
    print("Ошибка: число не трёхзначное")