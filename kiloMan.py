while True:
    try:
        repeticoes = int(input(""))
        for c in range(0, repeticoes):
            quant_tiro = int(input(""))
            tiros_array = input("").split()
            pulos = input("")
            acertos = 0
            tiros = ""
            for bala in tiros_array:
                tiros += bala

            for x in range(0, quant_tiro):
                if pulos[x] == "S" and (tiros[x] == "1" or tiros[x] == "2"):
                    acertos += 1
                elif pulos[x] == "J" and int(tiros[x]) > 2:
                    acertos += 1
            print(acertos)

    except EOFError:
        break
