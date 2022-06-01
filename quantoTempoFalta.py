horas = ""
while horas != "0 0 0 0":
    horas = input()
    if horas == "0 0 0 0":
        break
    numStr = horas.split(" ")
    num = []
    for x in numStr:
        num.append(int(x))
    totMin1 = num[0] * 60 + num[1]
    totMin2 = num[2] * 60 + num[3]
    if totMin2 - totMin1 < 0:
        totMin1 = 1440 - totMin1
        dif = totMin1 + totMin2
    else:
        dif = totMin2 - totMin1
    result = dif
    print(result)
