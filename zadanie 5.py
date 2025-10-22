weight = float(input("Введите свой вес в кг.: "))
height = float(input("Введите свой рост в cм.: "))
IMT = weight / (height / 100)**2
if IMT < 16:
    print(f"Выраженный дефицит массы тела: {IMT}")
elif 16 <= IMT < 18.5:
    print(f"Недостаточная масса тела: {IMT}")
elif 18.5 <= IMT < 25:
    print(f"Норма: {IMT}")
elif 25 <= IMT < 30:
    print(f"Избыточная масса тела: {IMT}")
elif 30 <= IMT < 35:
    print(f"Ожирение первой степени: {IMT}")
elif 35 <= IMT < 40:
    print(f"Ожирение второй степени: {IMT}")
else:
    print(f"Ожирение третьей степени: {IMT}")