
a, b, c, d = map(int, input("Введите a b c d через пробел: ").split())


if (c + 2 <= a and d + 2 <= b) or (d + 2 <= a and c + 2 <= b):
    print("Да")
else:
    print("Нет")

