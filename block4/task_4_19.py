# Данные: (x, y, width, height)
rect1 = (0, 0, 4, 3)
rect2 = (2, 1, 3, 2)

x_left = min(rect1[0], rect2[0])
y_bottom = min(rect1[1], rect2[1])
x_right = max(rect1[0] + rect1[2], rect2[0] + rect2[2])
y_top = max(rect1[1] + rect1[3], rect2[1] + rect2[3])

print(f"({x_left}, {y_bottom})", f"({x_right}, {y_top})")