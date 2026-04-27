chislo = int(input("Введите число: "))

edinicy = (chislo % 10)
desytky = int((chislo % 100) / 10)
sotye = int((chislo / 100))

max_chislo = edinicy
if max_chislo < desytky:
    max_chislo = desytky
elif max_chislo < sotye:
    max_chislo = sotye

print(F"Самое большое число: {max_chislo}")
