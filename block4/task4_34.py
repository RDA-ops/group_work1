chislo = int(input("Введите первое число:"))
chislo2 = int(input("Введите второе число:"))

if chislo % chislo2 == 0:
    print("Да, может, 1 число делитель для 2")
else:
    print("Нет, не может")

if chislo2 % chislo == 0:
    print("Да, может, 2 число делитель для 1")
else:
    print("Нет, не может")
