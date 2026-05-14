def check_brick(a, b, c, x, y):
    # Пары сторон граней
    faces = [(a, b), (a, c), (b, c)]
    
    for side1, side2 in faces:
        if (side1 <= x and side2 <= y) or (side1 <= y and side2 <= x):
            return True
    return False

# Ввод данных
a = float(input("Введите a (ребро 1): "))
b = float(input("Введите b (ребро 2): "))
c = float(input("Введите c (ребро 3): "))
x = float(input("Введите x (ширина отверстия): "))
y = float(input("Введите y (высота отверстия): "))

if check_brick(a, b, c, x, y):
    print("Кирпич пройдёт в отверстие")
else:
    print("Кирпич не пройдёт")