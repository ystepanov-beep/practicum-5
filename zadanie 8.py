N = int(input())
galleon = int(N / 17 // 29)
sikkle = int(N // 17 - galleon*29)
knats = int(N % 29)
if sikkle != 0 and galleon != 0 and knats != 0:
    print(f"{galleon} галлеонов \n {sikkle} сикклей \n {knats} кнатов ")
elif sikkle != 0 and galleon != 0 and knats == 0:
    print(f"{galleon} галлеонов \n {sikkle} сикклей \n")
elif galleon != 0 and knats != 0 and sikkle == 0:
    print(f"{galleon} галлеонов \n {knats} кнатов ")
elif galleon == 0 and knats != 0 and sikkle != 0:
    print(f"{sikkle} сикклей \n {knats} кнатов ")
elif sikkle != 0 and galleon == 0 and knats == 0:
    print(f"{sikkle} сикклей")
elif sikkle == 0 and galleon != 0 and knats == 0:
    print(f"{galleon} галлеонов")
elif sikkle == 0 and galleon == 0 and knats != 0:
    print(f"{knats} кнатов ")
elif sikkle == 0 and galleon == 0 and knats == 0:
    print()