a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a == b or b == c or a == c:
    print("Есть хотя бы одна пара равных чисел")
else:
    print("Нет равных чисел")