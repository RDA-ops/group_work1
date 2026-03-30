from math import pi, sqrt

S_kruga = float(input("Введите площадь круга: "))
S_kvadrata = float(input("Введите площадь квадрата: "))

r = sqrt(S_kruga / pi)
a = sqrt(S_kvadrata)
if 2 * r <= a:
    print("Круг уместится в квадрате: Да")
else:
    print("Круг уместится в квадрате: Нет")

if a * sqrt(2) <= 2 * r:
    print("Квадрат уместится в круге: Да")
else:
    print("Квадрат уместится в круге: Нет")
    