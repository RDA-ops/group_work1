import math 

S_circle = float(input("Введите площадь круга: "))
S_triangle = float(input("Введите площадь равностороннего треугольника: "))

a = math.sqrt(4 * S_triangle / math.sqrt(3))

r_vpis = math.sqrt(3) / 6 * a
R_opis = math.sqrt(3) / 3 * a

R = math.sqrt(S_circle / math.pi)

if R <= r_vpis:
    print("a) Круг уместится в треугольнике")
else: 
    print("a) Круг НЕ уместится в треугольнике")
    
if R_opis <= R:
    print("б) Треугольник уместится в круге")
else:
    print("б) Треугольник НЕ уместится в круге")
