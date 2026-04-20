a, b, c = float(input()), float(input()), float(input())

if a == 0:
    print("a ≠ 0")
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Нет вещественных корней")
    else:
        sqrt_d = d ** 0.5
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        print(x1, x2)
