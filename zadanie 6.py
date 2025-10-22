print("Сколько подданных видело улыбку волшебницы по дням")
a = int(input("В первый день: "))
b = int(input("В второй день: "))
c = int(input("В третий день: "))
if a == b == c:
    print("3")
elif a == b  or b == c or a == c:
    print("2")
else:
    print("0")