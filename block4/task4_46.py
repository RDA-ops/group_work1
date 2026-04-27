a, b, c = map(float, input("Введите стороны a, b, c: ").split())

if a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник не равносторонний")