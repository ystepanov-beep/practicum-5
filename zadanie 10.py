pin = int(input())
a = pin // 1000
b = (pin // 100) % 10
c = (pin // 10) % 10
d = pin % 10 
if 1900 <= pin <= 2050:
    print("ERROR")
elif 1000 <= pin <= 9999 and a != b and a != c and a != d and b != c and b != d and c != d:
    print("OK")
else:
    print("ERROR")