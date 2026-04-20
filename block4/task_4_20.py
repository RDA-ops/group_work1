m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

if m % n == 0:
    print(m // n)
else:
    print(f"{m} на {n} нацело не делится")
