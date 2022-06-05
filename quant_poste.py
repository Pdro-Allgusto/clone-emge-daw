while True:
    try:
        quant_poste = 1
        while quant_poste != 0:
            quant_poste = int(input(""))
            poste_string = input("").split()
            postes = [int(x) for x in poste_string]
            zero_original = postes.count(0)
            quebrados = 0

            for x in range(0, quant_poste * 2):
                quebrados += 1
                while postes[x % quant_poste] == 0:
                    quebrados += 1
                    x += 1
                    if quebrados > 2:
                        quebrados = 0
                        postes[x % quant_poste] = 1

            zero_depois = postes.count(0)
            quant_poste_madeira = zero_original - zero_depois
            print(quant_poste_madeira)
    except EOFError:
        break
