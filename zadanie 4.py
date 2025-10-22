parrot = int(input())
if parrot % 10 == 1:
    skl = "попугай"
elif 2 <= parrot % 10 <= 4:
    skl = "попугая"
else:
    skl = "попугаев"
print(f"{parrot} {skl}")