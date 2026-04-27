x, y = map(float, input("Введите x и y: ").split())

if (x > 0 and y > 0) or (x < 0 and y < 0):
    print("Точка попадает в область I или III")
else:
    print("Точка не попадает в область I или III")