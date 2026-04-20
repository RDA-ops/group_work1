minx = int(100)
miny = int(100)
maxx = int(0)
maxy = int(0)
a = 4

while  a != 0:
    x = int(input())
    y = int(input())
    if x < minx and y < miny:
        minx = x
        miny = y
    elif x > maxx and y > maxy:
        maxx = x
        maxy = y
    a = a-1

print(F"{maxx}, {maxy}, {minx}, {miny}")
