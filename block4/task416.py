import math

S_kruga = float(input("Введите площадь круга: "))
S_kvadrata = float(input("Введите площадь квадрата: "))

r = math.sqrt(S_kruga / math.pi)
a = math.sqrt(S_kvadrata)
if 2 * r <= a:
    print("а) Круг уместится в квадрате: Да")
else:
    print("а) Круг уместится в квадрате: Нет")

if a * math.sqrt(2) <= 2 * r:
    print("б) Квадрат уместится в круге: Да")
else:
    print("б) Квадрат уместится в круге: Нет")