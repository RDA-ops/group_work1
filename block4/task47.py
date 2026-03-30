a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a > b:
    maximum = a
    minimum = b
else:
    maximum = b
    minimum = a

print("Максимум:", maximum)
print("Минимум:", minimum)
