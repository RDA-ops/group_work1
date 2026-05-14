import math

a = float(input("Введите a (a ≠ 0): "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a == 0:
    print("Ошибка: a не может быть равно 0")
else:
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Два различных корня: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Один корень (два равных): x = {x}")
    else:
        print("Действительных корней нет")