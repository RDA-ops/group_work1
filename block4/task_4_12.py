r1 = int(input("Введите r1 "))
r2 = int(input("Введите r2 "))
i1 = 220 / r1
i2 = 220 / r2
c = i1 - i2
if c > 0:
    print("i1 больше чем i2")
else:
    print("i2 больше чем i1")
