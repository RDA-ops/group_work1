num = int(input("Введите двузначное число: "))
desyatki = num // 10
edinici = num % 10

if num**2 == 4 * (desyatki**3 + edinici**3):
    print("положительный ответ")
else:
    print("отрицательный ответ")
