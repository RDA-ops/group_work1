number = input("Введите число ")

if number == number[::-1]:
    print(f"Число {number} является полнидромом")
else:
    print(f"Число {number} полиндромом не является")
