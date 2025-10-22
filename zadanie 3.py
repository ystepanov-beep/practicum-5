number = int(input().strip())
a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
borba = bool(a == d and c == b)
result = "настоящее" * borba + "кривое" * (not borba)
print(result)