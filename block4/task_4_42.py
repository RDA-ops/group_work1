# Основные переменные 
a = float(input("Введите число a: ")) 
b = float(input("Введите число b: ")) 
c = float(input("Введите число c: ")) 

# а) Проверка неравенства a < b < c 
inequality_a = (a < b < c) 

# б) Проверка неравенства b > a > c 
inequality_b = (b > a > c) 

# Вывод результатов 
print(f"а) a < b < c: {inequality_a}") 
print(f"б) b > a > c: {inequality_b}") 

# Дополнительный вывод в читаемом формате 
if inequality_a: 
    print(f"а) {a} < {b} < {c} — верно") 
else:
    print(f"а) {a} < {b} < {c} — неверно") 
 
if inequality_b:
    print(f"б) {b} > {a} > {c} — верно") 
else:
    print(f"б) {b} > {a} > {c} — неверно") 
