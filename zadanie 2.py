xc = int(input("xc = "))
yc = int(input("yx = "))
r = int(input("r = "))
x = int(input("x = "))
y = int(input("y = "))
if (x - xc)**2 + (y - yc)**2 <= r**2:
    print("Точка на окружности")
else:
    print("Точка находится вне окружности")